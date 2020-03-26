<template>
    <div class="navDrawer">
        <NavDrawerComponent/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import NavDrawerComponent from "@/components/NavDrawerComponent";

    export default {
        name: 'NavDrawer',
        components: {
            NavDrawerComponent,
        }
    }
</script>
