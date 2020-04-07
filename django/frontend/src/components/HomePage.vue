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
                                Profile
                            </v-card-title>
                            <div v-if="profileLoading">
                                <v-progress-circular
                                        indeterminate
                                        color="primary"
                                />
                                <v-card-text>
                                    User Profile Loading
                                </v-card-text>
                            </div>
                            <div v-if="!profileLoading && !userProfile">
                                <v-card-text>
                                    You need to complete this section
                                </v-card-text>
                            </div>
                            <div v-if="!profileLoading && userProfile">
                                <v-card-text>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Name
                                    </p>
                                    <p class="text-left">{{userProfile["first_name"]}}
                                        {{userProfile["middle_name"]}}
                                        {{userProfile["last_name"]}}</p>

                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Birth Date
                                    </p>
                                    <p class="text-left">{{userProfile["birth_date"]}}</p>

                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Citizenship
                                    </p>
                                    <p class="text-left">{{userProfile["citizenship_cntry"]}}</p>

                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Residence
                                    </p>
                                    <p class="text-left">{{userProfile["residence_state"]}}</p>
                                </v-card-text>
                            </div>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card class="pa-2">
                            <v-card-title>
                                Documents
                            </v-card-title>
                            <v-progress-circular
                                    indeterminate
                                    color="primary"
                            />
                            <v-card-text>
                                User Documents Loading
                            </v-card-text>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card class="pa-2">
                            <v-card-title>
                                Seatime Logged
                            </v-card-title>
                            <v-progress-circular
                                    indeterminate
                                    color="primary"
                            />
                            <v-card-text>
                                Voyages Loading
                            </v-card-text>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {getProfile} from "../_services/profile.service";
    import {funcLogout} from "../_services/user.service";
    import ConfirmModalComponent from "./ConfirmModalComponent"
    import NavDrawerComponent from "./NavDrawerComponent";

    export default {
        components: {NavDrawerComponent, ConfirmModalComponent},
        data() {
            return {
                drawer: 'true',
                color: 'primary',
                profileLoading: true,
                userProfile: {},
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                }
            }
        },
        methods: {
            loadProfile: function () {
                getProfile().then((resp) => {
                    console.log(resp.data);
                    this.profileLoading = false;
                    this.userProfile = resp.data[0];
                }).catch(() => {
                    this.profileLoading = false;
                    this.userProfile = {error: 'Error loading profile'};
                })
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
            }
        },
        mounted() {
            this.loadProfile();
        }
    }
</script>

<style>
    .tag-title {
        color: gray;
    }

</style>