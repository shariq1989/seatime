<template>
    <v-dialog v-model="show" max-width="500px">
        <v-card>
            <v-card-title>
                {{dialogHeader}}
            </v-card-title>
            <v-card-text>
                {{dialogMessage}}
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" flat @click.stop="show=false">Cancel</v-btn>
                <v-btn color="primary" flat @click.stop="show=false">Confirm</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        props: {
            displayStatus: Boolean,
            dialogHeader: String,
            dialogMessage: String
        },
        computed: {
            show: {
                get() {
                    return this.value
                },
                set(value) {
                    this.$emit('input', value)
                }
            }
        }
    }
</script>