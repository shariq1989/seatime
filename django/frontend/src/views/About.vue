<template>
    <div class="about">
        <h1>SeaTime Web Application for Mariners</h1>
        <p>The App (For lack of a better title)</p>
        <div id="app">
            {{ info }}
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import HomePage from '@/components/HomePage.vue'

    export default {
        name: 'Home',
        components: {
            HomePage
        },
        data() {
            return {
                info: null
            }
        },
        mounted() {
            axios
                .get('https://api.coindesk.com/v1/bpi/currentprice.json')
                .then(response => (this.info = response))
        }
    }
</script>
