<template>
    <div class="signup">
        <SignUpForm/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import SignUpForm from "../components/SignUpForm";

    export default {
        name: 'SignUp',
        components: {
            SignUpForm
        }
    }
</script>
