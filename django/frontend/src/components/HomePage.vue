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
                            <div v-if="documentsLoading">
                                <v-progress-circular
                                        indeterminate
                                        color="primary"
                                />
                                <v-card-text>
                                    Documents Loading
                                </v-card-text>
                            </div>
                            <div v-if="!documentsLoading && !documents">
                                <v-card-text>
                                    You need to complete this section
                                </v-card-text>
                            </div>
                            <div v-if="!documentsLoading && documents">
                                <v-card-text>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Mariner Ref
                                    </p>
                                    <p class="text-left">{{documents["mariner_ref_num"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        MMC Document Number
                                    </p>
                                    <p class="text-left">{{documents["mmc_doc_num"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        MMC Issue
                                    </p>
                                    <p class="text-left">{{documents["mmc_issue_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        MMC Expiration
                                    </p>
                                    <p class="text-left">{{documents["mmc_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Medical National Expiration
                                    </p>
                                    <p class="text-left">{{documents["med_ntl_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Medical STCW Expiration
                                    </p>
                                    <p class="text-left">{{documents["med_stcw_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Medical Pilot Expiration
                                    </p>
                                    <p class="text-left">{{documents["med_pilot_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        TWIC Expiration
                                    </p>
                                    <p class="text-left">{{documents["twic_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Basic Training Expiration
                                    </p>
                                    <p class="text-left">{{documents["basic_training_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Advanced Firefighting Expiration
                                    </p>
                                    <p class="text-left">{{documents["advanced_fire_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        First Aid & CPR Expiration
                                    </p>
                                    <p class="text-left">{{documents["first_aid_cpr_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Passport Expiration
                                    </p>
                                    <p class="text-left">{{documents["passport_expr_date"]}}</p>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Drug Test Expiration
                                    </p>
                                    <p class="text-left">{{documents["drug_test_compliant"]}}</p>
                                </v-card-text>
                            </div>
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
    import {getDocuments, getProfile} from "../_services/profile.service";
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
                documentsLoading: true,
                userProfile: {},
                documents: {},
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                }
            }
        },
        methods: {
            loadData: function () {
                getProfile().then((resp) => {
                    console.log(resp.data);
                    this.profileLoading = false;
                    this.userProfile = resp.data[0];
                }).catch(() => {
                    this.profileLoading = false;
                    this.userProfile = {error: 'Error loading profile'};
                });
                getDocuments().then((resp) => {
                    console.log(resp.data);
                    this.documentsLoading = false;
                    this.documents = resp.data[0];
                }).catch(() => {
                    this.documentsLoading = false;
                    this.documents = {error: 'Error loading profile'};
                });
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
            this.loadData();
        }
    }
</script>

<style>
    .tag-title {
        color: gray;
    }

</style>