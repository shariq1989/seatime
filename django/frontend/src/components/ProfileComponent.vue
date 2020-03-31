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
                            <div v-if="!profileLoading">
                                <v-card-text>
                                    <v-text-field
                                            v-model=userProfile.first_name
                                            label="First Name"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=userProfile.middle_name
                                            label="Middle Name"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=userProfile.last_name
                                            label="Last Name"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=userProfile.birth_date
                                            label="Birth Date"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=userProfile.citizenship_cntry
                                            label="Citizenship"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=userProfile.residence_state
                                            label="Residence"
                                    ></v-text-field>
                                </v-card-text>
                            </div>
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
                },
            }
        },
        methods: {
            loadProfile: function () {
                getProfile().then((resp) => {
                    console.log(resp.data);
                    this.profileLoading = false;
                    this.$set(this.userProfile, resp.data[0]);
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