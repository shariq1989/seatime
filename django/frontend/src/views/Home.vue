<template>
  <div class="home">
    <img alt="Seatime Logo" src="../assets/seatime.png">
    <HomePage msg="Welcome to Seatime"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HomePage from '@/components/HomePage.vue'

export default {
  name: 'Home',
  components: {
    HomePage
  }
}
</script>
