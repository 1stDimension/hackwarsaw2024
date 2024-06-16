<template>
  <div v-if="error">{{ error }}</div>
  <div class="about">
    <h1>Add bill</h1>
    <form @submit="saveBill">
      <textarea name="contents"></textarea>
      <br>
      <input type="submit" value="Submit">
    </form>
    
  </div>
</template>

<script>
import getApiUrl from '@/composable/getPath.js'

export default {
  name: 'billAdd',
  data() {
    return {
      error: null,
    }
  },
  methods: {
    async saveBill(submitEvent) {
      submitEvent.preventDefault()
      let contents = submitEvent.target.contents.value

      console.log(contents)
      if (contents) {
        try {
          let response = await fetch(
            getApiUrl() + 'bill',
            {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify({contents})
            }
          )
        } catch (err) {
          this.error = err.message
        }
      }
    }
  }
}

</script>

<style>

</style>
