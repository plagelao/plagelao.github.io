---
layout: page
title: OpenAI
excerpt_separator: <!--more-->
---

Demo integrating OpenAI in your site.

<!--more-->

Because this is just a demo, the OpenAI account is probably out of credit, so don't be surprise if you get that error.

{% raw %}
<div id="demo"></div>
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script>
const { createApp, ref } = Vue
const apiKey = "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"
const endpoint = "https://api.openai.com/v1/engines/davinci-002/completions"
const createInteraction = (text, answer) => {
    return { id: Date.now(), content: text, answer: answer }
}
const createQuestion = (text) => {
    return createInteraction(text, false)
}
const createAnswer = (text) => {
    return createInteraction(text, true)
}
const demo = {
  data() {
    return {
      conversation: [],
      text: "",
      error: "",
    };
  },
  template: `
  <div>
      <div v-for="interaction in conversation" :key="interaction.id">
          <p v-if="interaction.answer">Answer: {{interaction.content}}</p>
          <p v-else>Question: {{interaction.content}}</p>
      </div>
      <input v-model="text" placeholder="Ask me anything"/>
  </div>`,
  watch: {
    async text(newText) {
      this.conversation.push(createQuestion(newText))
      try {
          const response = await axios.post(endpoint,
          { prompt: newText, max_tokens: 150 },
          {
            headers: { Authorization: `Bearer ${apiKey}` },
          })
          this.conversation.push(createAnswer(response.data.choices[0].text.trim()));
      } catch (error) {
          this.conversation.push(createAnswer(error.response.data.error.message));
      }
    }
  },
}
createApp(demo).mount('#demo');
</script>
{% endraw %}
