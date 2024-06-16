<template>
  <div v-if="error">{{ error }}</div>
  <div class="about">
    <h1>Create Voter</h1>
    <form @submit="saveVoter">
      <input name="first_name">
      <input name="last_name">
      <input name="local">
      <br>
      <input type="submit" value="Register">
    </form>
    
  </div>
</template>

<script>
import getApiUrl from '@/composable/getPath.js'

export default {
  name: 'voterCreate',
  data() {
    return {
      error: null,
    }
  },
  methods: {
    async saveVoter(submitEvent) {
      submitEvent.preventDefault()
      const data = {
        'first_name': submitEvent.target.first_name.value,
        'last_name': submitEvent.target.last_name.value,
        'local': submitEvent.target.local.value
      }
      if (data.first_name && data.last_name && data.local) {
        try {
          let response = await fetch(
            getApiUrl() + 'voter',
            {
              method: "POST",
              headers: {"Content-Type": "application/json"},
              body: JSON.stringify(data)
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
