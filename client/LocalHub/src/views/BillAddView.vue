<template>
  <div v-if="error">{{ error }}</div>
  <div class="about">
    <h1>Add bill</h1>
    <form @submit="saveBill">
      <textarea name="context"></textarea>
      <br>
      <input type="submit" value="Submit">
    </form>
    
  </div>
</template>

<script>

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
      let context = submitEvent.target.context.value

      console.log(context)
      if (context) {
        try {
          let response = await fetch(
            `http://localhost:8000/bill`,
            {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify({
                "context": context
              })
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
