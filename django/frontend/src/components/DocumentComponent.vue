<!--suppress JSUnusedGlobalSymbols -->
<template>
    <v-app id="inspire">
        <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
        <v-content>
            <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                                   @input="updateModalStatus"/>
            <v-container fluid class="grey lighten-4 fill-height">
                <v-row class="mb-6">
                    <v-col>
                        <v-card class="pa-2">
                            <v-card-title>
                                Documents
                            </v-card-title>
                            <div v-if="pageLoading">
                                <v-progress-circular
                                        indeterminate
                                        color="primary"
                                />
                                <v-card-text>
                                    Loading
                                </v-card-text>
                            </div>
                            <div v-if="!pageLoading">
                                <v-card-text>
                                </v-card-text>
                            </div>
                            <v-card-actions>
                                <v-spacer/>
                                <v-btn color="primary">Save</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {funcLogout} from "../_services/user.service";
    import ConfirmModalComponent from "./ConfirmModalComponent"
    import NavDrawerComponent from "./NavDrawerComponent";

    export default {
        components: {NavDrawerComponent, ConfirmModalComponent},
        data() {
            return {
                drawer: 'true',
                color: 'primary',
                pageLoading: true,
                dateModal: false,
                displayErrorMessage: false,
                snackbar: false,
                snackbarText: null,
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                },
                APIMethod: 'POST',
            }
        },
        methods: {
            loadPage: function () {
            },
            logout() {
                this.logoutDialog = true;
            },
            displayLogoutDialog() {
                this.logoutDialog.displayStatus = true;
            },
            updateModalStatus(value) {
                this.logoutDialog.displayStatus = false;
                if (value === true) {
                    funcLogout();
                }
            },
        },
        mounted() {
            this.loadPage();
        }
    }
</script>