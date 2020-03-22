<template>
    <v-app id="modal">
        <p>hi</p>
    </v-app>
</template>
<script>
    export default {
        data() {
        },
    }
</script>
<!--
<template>
    <div class="text-left">
        <v-dialog v-model="confirmDialog" width="500">
            <v-card>
                <v-card-title class="headline grey lighten-2" primary-title>
                    Confirm Action
                </v-card-title>
                <v-card-text>
                    Are you sure you want to proceed?
                </v-card-text>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="confirmDialog = false">
                        Cancel
                    </v-btn>
                    <v-btn color="red darken-1" text @click="confirmDialog = false">
                        Confirm
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>
<script>
    Vue.component('confirmModal', {
        props: ['title'],
        template: '<h3>{{ title }}</h3>'
    })
</script>
-->