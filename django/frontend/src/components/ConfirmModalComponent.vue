<template>
    <v-dialog max-width="500px">
        <v-card>
            <v-card-title>
                {{dialogHeader}}
            </v-card-title>
            <v-card-text>
                {{dialogMessage}}
            </v-card-text>
            <v-card-actions>
                <v-spacer/>
                <v-btn color="primary" @click.stop="displayStatus=false">Cancel</v-btn>
                <v-btn color="error" @click.stop="displayStatus=false">Confirm</v-btn>
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
                    return this.displayStatus;
                },
                set(value) {
                    this.$emit('input', value)
                }
            }
        }
    }
</script>