import { ref } from 'vue'

const getBills = () => {
  const bills = ref([])
  const error = ref(null)

  const load = async () => {
    try {
      let data = await fetch(
        'http://localhost:8000/bill',
        {
          method: "GET",
          redirect: "follow"
        }
      )
      if (!data.ok) {
        throw Error('ERROR: fetching bill')
      }
      bills.value = await data.json()
    }
    catch (err) {
      error.value = err.message
    }
  }
  return { bills, error, load }
}

export default getBills
