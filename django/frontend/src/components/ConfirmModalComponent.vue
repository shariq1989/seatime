<template>
    <v-dialog v-model="show" max-width="500px">
        <v-card>
            <v-card-title>
                {{dialogDetails.header}}
            </v-card-title>
            <v-card-text>
                {{dialogDetails.body}}
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
            dialogDetails: {
                show: Boolean,
                header: String,
                body: String,
            }
        },
        computed: {
            show: {
                get() {
                    return this.dialogDetails['show']
                },
                set(value) {
                    this.$emit('input', value)
                }
            }
        }
    }
</script>