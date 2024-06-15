import { ref } from 'vue'

const getVoters = () => {
  const voters = ref([])
  const error = ref(null)

  const load = async () => {
    try {
      let data = await fetch(
        'http://localhost:8000/voter',
        {
          method: "GET",
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
  return { voters, error, load }
}

export default getVoters
