---
title: Feature toggles
excerpt_separator: <!--more-->
layout: post
categories: [Articles, Software development, Continuous delivery, Tutorials]
tags: [continuous delivery, developer experience]
tools:
  - label: Flagsmith
    link: https://flagsmith.com
---
Releasing new software can be a source of considerable stress. The magnitude of stress tends to increase with the size of the release, and this stress is directly linked to issues such as burnout, high turnover, and reduced job satisfaction. This underscores the significance of prioritizing developer experience.

Among the various methods available to enhance the developer experience for both you and your team, one of the most straightforward is the use of feature toggles. The concept behind feature toggles is to separate the deployment of new code from the actual release of a new feature.

This article describes the key advantages of employing feature toggles and includes a brief demonstration using one of the many third-party services that offer feature toggles.

With that in mind, let’s get on with it!

<!--more-->

### What are feature toggles

Feature toggles is a set of techniques that allow developers to have control over what code is released, when it's released, and to whom it's released, independently of deploying or changing the code.

Usually, they're used as part of continuous delivery. The idea is that you can merge any code into your main branch as long as you have some method to control when that code is active (released).

An example can help clarify the concept. Imagine that you want to release a new feature in an existing application. Without feature toggles, the change flow usually goes like this: write and test the code in a branch, merge it, and deploy it. The change looks like this:

```diff
 some_old_code
+ code_for_the_new_feature
- old_code
 some_more_old_code
```

Inevitably, you have to release the new code in production as soon as you deploy.

With feature toggles, you can change this flow. You can, for example, release the code only to some users:

```diff
 some_old_code
+  if user.feature_enabled?(:allow_access_to_new_feature)
+    code_for_the_new_feature
+  else
    old_code
+ end
 some_more_old_code
```

In a basic way, this use case is how A/B testing works.

But you can also choose to hide the feature for all users until you switch the feature on:

```ruby
 some_old_code
 if feature_enabled?(:allow_access_to_new_feature)
    code_for_the_new_feature
 else
    some_more_old_code
 end
```

This pattern allows you to deploy incomplete code, in this case `code_for_the_new_feature`, because **you are decoupling the release from the deployment**.

### What are the benefits of adding this complexity

There are many!

The most important one is probably the ability to switch a feature on and off at demand, making releases and rollbacks fast and simple.

It also reduces the conflicts between features because everyone works on the latest code.

Another benefit is removing the stress from a release. With feature toggles you can release the new feature only to a 10% of your user and, when you are sure it performs well both technically and from a business perspective, expand it to the rest of users.

In general, it gives the team more control over what's in production.

### Problems

Developers need to be strict with removing feature toggles when they become obsolete. Otherwise, it can be a burden to maintainability. If you are not careful, you can end up with many `if` clauses and a lot of dead code.

A good practice is to always remove both the old code and the feature toggle when you don't need them. Usually, that is after you are comfortable with the new release.

### Integrating Flagsmith

Although you can develop your own feature toggle framework, there are many products already there that can help you minimse your efforts.

This article shows how [Flagsmith](https://flagsmith.com) works.

First, set up your account. Flagsmith has a free plan, so you can get this example running at no cost. After setting up your account you land on your dashboard:

![Set up Flagsmith account](/assets/flagsmith/1-setup.png)

You start with two environments, one for development and one for production. This article uses the development environment to create a new feature toggle:

![Create your first feature toggle](/assets/flagsmith/2-create-flag.png)

After setting up your feature toggle, it stays inactive by default:

![First feature toggle created](/assets/flagsmith/3-flag-created.png)

Now, in your demo application, you can start using your feature toggle. For the Javascript SDK it look like this:

```javascript
<script src="https://cdn.jsdelivr.net/npm/flagsmith/index.js"></script>

<script>
flagsmith.init({
    environmentID:"YOUR-ENVIRONMENT-ID",
    onChange: (oldFlags, params) => { // Occurs whenever flags are changed
        // Determines if the update came from the server or local cached storage
        const { isFromServer } = params;

        // Check for a feature
        if (flagsmith.hasFeature("demo")) {
            console.log('Feature is active')
        } else {
            console.log('Feature is not active')
        }
    }
});
</script>
```

With the feature toggle inactive, the console will look like this:

![Browser console output when feature toggle is off](/assets/flagsmith/6-console-output-when-off.png)

This demonstrates that the code is executing the path where the feature toggle is turn off.

If you turn the toggle on:

![Activate your first feature toggle](/assets/flagsmith/4-activate-flag.png)

And confirm the activation:

![Feature toggle active](/assets/flagsmith/5-flag-activated.png)

Then the console output looks like this:

![Browser console output when feature toggle is on](/assets/flagsmith/7-console-output-when-on.png)


Demonstrating that the code is executing the path where the feature toggle is turn on.

This simple integration is allowing you to release and rollback code without deploying. Many more features that any of the providers of this type of services offer help with other use cases like A/B Testing, user segmentation, etc.

That's all!
