---
title: AWS ALB, node.js, and fixing intermittent issues
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, AWS, Explanations]
tags: [clarity, aws, node.js, k6]
tools:
  - label: AWS ALB
    link: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
  - label: node.js
    link: https://nodejs.org
  - label: k6
    link: https://grafana.com/docs/k6/latest/
---
Using new technologies can come with huge benefits, but it usually also comes with unexpected problems. While working with the [AWS application load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) and [node.js](https://nodejs.org), you can hit a nasty issue where the end users can get a 502 error intermittently.


This article explains why that issue happens and ways to solve it.

With that in mind, let's get on with it!

<!--more-->

### The architecture

To reproduce this issue you need to deploy a node.js app to AWS and you need to serve that app via an application load balancer:

![Architecture diagram](/assets/alb-node/diagram.png)

In this case, the node.js server is deployed to ECS, but that's just a detail.

### The problem

In some load conditions, depending on your app, you will end that with 502 errors. The issue is related to the configuration of the AWS load balancer and the node.js server.

The AWS load balancer has a default connection idle timeout of 1 minute. The node.js server has a default keep alive timeout of 5 seconds. This combination makes the load balancer use connections that are no longer valid in the server. When that closed connection is used, the load balancer will fail, raising a 502 error.

In order to fix this, you need to change the default configurations.

That's all good, you have way to fix it but, how can you make sure you have fix your intermittent issue for real?

### Intermittent issues

Intermittent errors are difficult to fix mostly because reproducing them isn't easy. The consequence of this is that you can't be sure if you have fixed the problem.

The first step is to reproduce the problem in a consistent way. After that, implement your fix and, if the consistent way of reproducing the problem doesn't show errors, you're done!

For this particular problem, given that the error only happens under some load conditions, a load test is a good way to start.

### The test

For load testing, you can use [k6](https://grafana.com/docs/k6/latest/), for example:

```js
import { sleep, check } from 'k6'
import http from 'k6/http'
import { Counter } from 'k6/metrics'

export const options = {
  scenarios: {
    basic: {
      executor: 'constant-vus',
      exec: 'basic',
      vus: 20,
      duration: '2m',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.001'], // http errors (timeouts or 5XX) should be less than 1%
  },
}

const counterTimeout = new Counter('response_timeout')
const counter5XX = new Counter('response_5xx')

export function basic() {
  // This does a simple HTTP get to the URL defined in the TARGET_BASE_URL environment variable
  const res = http.get(__ENV.TARGET_BASE_URL)

  // This checks if the request is a succesful
  check(res, {
    'status is 200': r => r.status === 200,
  })

  // This counts if there is a timeout
  if (res.status === 0) {
    counterTimeout.add(1)
  }
  // This counts if there is a 5XX error
  if (res.status >= 500 && res.status < 600) {
    counter5XX.add(1)
  }

  sleep(1)
}
```

With this test, you can make sure that the URL you are hitting fails less than a 0.1%, which is enough to reproduce the 502 issue. Running the test will show a failure if you have the problem with the ALB and the node.js server.

### The solution

The solution is to increase the node.js server keep alive timeout so it's larger than the AWS load balancer connection idle timeout.

If you make the change to your node.js app to make the keep alive timeout 61 seconds, and then run the load test, it will be successful.

That's all!
