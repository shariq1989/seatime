<!--suppress JSUnusedGlobalSymbols, JSUnfilteredForInLoop -->
<template>
    <v-app id="inspire" style="background-color: #bbdefb;">
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
                                    <div class="pa-2">
                                        <v-alert type="error" v-if="displayErrorMessage">
                                            <span class="text-left" v-html="errorMessage"></span>
                                        </v-alert>
                                        <v-snackbar v-model="snackbar">
                                            {{ snackbarText }}
                                        </v-snackbar>
                                    </div>
                                    <v-row>
                                        <v-col>
                                            <v-text-field
                                                    v-model=documents.mariner_ref_num
                                                    label="Mariner Reference Number"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model=documents.mmc_doc_num
                                                    label="MMC Document Number"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model=documents.mmc_issue_date
                                                    label="MMC Issue Date"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model=documents.mmc_expr_date
                                                    label="MMC Expiration"
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-text-field
                                            v-model=documents.med_ntl_expr_date
                                            label="Medical National Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.med_stcw_expr_date
                                            label="Medical STCW Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.med_pilot_expr_date
                                            label="Medical Pilot Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.twic_expr_date
                                            label="TWIC Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.basic_training_expr_date
                                            label="Basic Training Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.advanced_fire_expr_date
                                            label="Advanced Firefighting Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.first_aid_cpr_expr_date
                                            label="First Aid & CPR Expiration"
                                    ></v-text-field>
                                    <v-text-field
                                            v-model=documents.passport_expr_date
                                            label="Passport Expiration"
                                    ></v-text-field>
                                    <v-checkbox v-model="documents.drug_test_compliant"
                                                label="Drug Test Compliance"></v-checkbox>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer/>
                                    <v-btn color="primary" @click.stop="editDocuments">Save Changes</v-btn>
                                </v-card-actions>
                            </div>
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
    import {getDocuments, updateDocuments} from "../_services/profile.service";

    export default {
        components: {NavDrawerComponent, ConfirmModalComponent},
        data() {
            return {
                drawer: 'true',
                color: 'primary',
                pageLoading: true,
                dateModal: false,
                displayErrorMessage: false,
                errorMessage: '',
                snackbar: false,
                snackbarText: null,
                documents: {
                    mariner_ref_num: null,
                    mmc_doc_num: null,
                    mmc_issue_date: null,
                    mmc_expr_date: null,
                    med_ntl_expr_date: null,
                    med_stcw_expr_date: null,
                    med_pilot_expr_date: null,
                    twic_expr_date: null,
                    basic_training_expr_date: null,
                    advanced_fire_expr_date: null,
                    first_aid_cpr_expr_date: null,
                    passport_expr_date: null,
                    drug_test_compliant: false,
                    id: null
                },
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
                getDocuments().then((resp) => {
                    if (resp.data[0]) {
                        this.APIMethod = 'PUT';
                    }
                    this.pageLoading = false;
                    this.documents.id = resp.data[0]['id'];
                    this.documents.mariner_ref_num = resp.data[0]['mariner_ref_num'];
                    this.documents.mmc_doc_num = resp.data[0]['mmc_doc_num'];
                    this.documents.mmc_issue_date = resp.data[0]['mmc_issue_date'];
                    this.documents.mmc_expr_date = resp.data[0]['mmc_expr_date'];
                    this.documents.med_ntl_expr_date = resp.data[0]['med_ntl_expr_date'];
                    this.documents.med_stcw_expr_date = resp.data[0]['med_stcw_expr_date'];
                    this.documents.med_pilot_expr_date = resp.data[0]['med_pilot_expr_date'];
                    this.documents.twic_expr_date = resp.data[0]['twic_expr_date'];
                    this.documents.basic_training_expr_date = resp.data[0]['basic_training_expr_date'];
                    this.documents.advanced_fire_expr_date = resp.data[0]['advanced_fire_expr_date'];
                    this.documents.first_aid_cpr_expr_date = resp.data[0]['first_aid_cpr_expr_date'];
                    this.documents.passport_expr_date = resp.data[0]['passport_expr_date'];
                    this.documents.drug_test_compliant = resp.data[0]['drug_test_compliant'];
                }).catch(() => {
                    this.pageLoading = false;
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
            },
            editDocuments() {
                this.displayErrorMessage = false;
                let documentFields = {
                    mariner_ref_num: this.documents.mariner_ref_num,
                    mmc_doc_num: this.documents.mmc_doc_num,
                    mmc_issue_date: this.documents.mmc_issue_date,
                    mmc_expr_date: this.documents.mmc_expr_date,
                    med_ntl_expr_date: this.documents.med_ntl_expr_date,
                    med_stcw_expr_date: this.documents.med_stcw_expr_date,
                    med_pilot_expr_date: this.documents.med_pilot_expr_date,
                    twic_expr_date: this.documents.twic_expr_date,
                    basic_training_expr_date: this.documents.basic_training_expr_date,
                    advanced_fire_expr_date: this.documents.advanced_fire_expr_date,
                    first_aid_cpr_expr_date: this.documents.first_aid_cpr_expr_date,
                    passport_expr_date: this.documents.passport_expr_date,
                    drug_test_compliant: this.documents.drug_test_compliant,
                    user: localStorage.getItem('id'),
                };
                updateDocuments([this.APIMethod, documentFields, this.documents.id]).then(
                    () => {
                        this.snackbarText = 'Documents updated successfully';
                        this.snackbar = true;
                        this.loadPage();
                    }
                ).catch(err => {
                        console.log(err.response.data);
                        this.displayErrorMessage = true;
                        this.errorMessage = 'Error updating documents';
                        if (err.response.data) {
                            for (const field in err.response.data) {
                                for (const error of err.response.data[field]) {
                                    this.errorMessage += '<br/>';
                                    this.errorMessage += error;
                                }
                            }
                        }
                    }
                )
            }
        },
        mounted() {
            this.loadPage();
        }
    }
</script>