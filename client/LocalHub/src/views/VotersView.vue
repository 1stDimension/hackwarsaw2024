<template>
  <div v-if="error">{{ error }}</div>
  <div class="about">
    <h1>Voters List</h1>
  </div>
<table>
  <tr>
    <th>present</th>
    <th>first name</th>
    <th>last name</th>
    <th>local number</th>
  </tr>
  <tr v-for="voter in voters" :key="voter.id">
    <td><input type="checkbox" :value="voter.id" @change="presentChange(voter.id, $event.target.checked)"></td>
    <td>{{ voter.first_name }}</td>
    <td>{{ voter.last_name }}</td>
    <td>{{ voter.local }}</td>
  </tr>
</table>
</template>

<script>
import getApiUrl from '@/composable/getPath.js'
import getVoters from '@/composable/getVoters'

export default {
  name: 'voters',
  setup() {
    const { voters, error, load } = getVoters()
    load()
    return { voters, error }
  },
  data() {
    return {
      // presentChange: ''
    }
  },
  methods: {
    async presentChange(voterId, state) {
      let presentChangeUrl = getApiUrl() + 'voter/' + voterId
      if (state) {
        presentChangeUrl += "/present"
      } else {
        presentChangeUrl += "/absent"
      }
      try {
        let data = await fetch(
          presentChangeUrl,
          {
            method: "POST",
            redirect: "follow"
          }
        )
        if (!data.ok) {
          throw Error('ERROR: fetching voters')
        }
        voters.value = await data.json()
      }
      catch (err) {
        error.value = err.message
      }
    }
  }
}

</script>

<style>

</style>
