<template>
  <div class="login">
    <LoginForm/>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginForm from "../components/LoginForm";

export default {
  name: 'Login',
  components: {
    LoginForm
  }
}
</script>
