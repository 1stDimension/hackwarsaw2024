<template>
  <div v-if="error">{{ error }}</div>
  <div class="about">
    <h1>Bills</h1>
  </div>
<table>
  <tr>
    <th>bills</th>
  </tr>
  <tr v-for="bill in bills" :key="bill.id">
    <td>{{ bill.contents }}</td>
  </tr>
</table>
</template>

<script>
import getApiUrl from '@/composable/getPath.js'
import getBills from '@/composable/getBills'

export default {
  name: 'bills',
  setup() {
    const { bills, error, load } = getBills()
    load()
    return { bills, error }
  },
  data() {
    return {
      data: [],
    }
  },
  methods: {
    async presentChange(voterId, state) {
      console.log(voterId, state)
      try {
        let data = await fetch(
          getApiUrl() + "bills/",
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
