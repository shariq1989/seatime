<template>
    <v-dialog v-model="show" max-width="500px">
        <v-card>
            <v-card-title class="text-left">
                {{dialogHeader}}
            </v-card-title>
            <v-card-text class="text-left">
                <div class="text--primary">{{dialogMessage}}</div>
            </v-card-text>
            <v-card-actions>
                <v-spacer/>
                <v-btn color=" primary
            " @click.stop="onBtnClick(false)">Cancel
                </v-btn>
                <v-btn color="error" @click.stop="onBtnClick(false)">Confirm</v-btn>
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
            }
        }, methods: {
            onBtnClick(value) {
                this.$emit('input', value)
            }
        }
    }
</script>