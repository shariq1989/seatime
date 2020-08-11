<template>
    <div class="confirmModal">
        <ConfirmModalComponent/>
    </div>
</template>

<script>
    // @ is an alias to /src
    import ConfirmModalComponent from '@/components/ConfirmModalComponent.vue'

    export default {
        name: 'ConfirmModal',
        components: {
            ConfirmModalComponent
        }
    }
</script>
