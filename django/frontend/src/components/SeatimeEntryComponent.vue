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
                                Seatime Log
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
                                                    v-model="seatime_entries.vessel"
                                                    label="Vessel"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model="seatime_entries.depart_date"
                                                    label="Departure Date"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model="seatime_entries.arrival_date"
                                                    label="Arrival Date"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model="seatime_entries.position"
                                                    label="Position"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model="seatime_entries.voyage_type"
                                                    label="Voyage Type"
                                            ></v-text-field>
                                        </v-col>
                                        <v-col>
                                            <v-text-field
                                                    v-model="seatime_entries.workday_type"
                                                    label="Workday Type"
                                            ></v-text-field>
                                        </v-col>
                                    </v-row>
                                    <v-text-field
                                            label="Passport Expiration"
                                    ></v-text-field>
                                    <v-checkbox
                                            label="Drug Test Compliance"></v-checkbox>
                                </v-card-text>
                                <v-card-actions>
                                    <v-spacer/>
                                    <v-btn color="primary" @click.stop="editSeatime">Save Changes</v-btn>
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
    import {getSeatimeEntries, updateSeatimeEntries} from "../_services/seatime_entry.service";

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
                seatime_entries: {
                    vessel: null,
                    depart_date: null,
                    arrival_date: null,
                    voyage_type: null,
                    workday_type: null,
                    position: null,
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
                getSeatimeEntries().then((resp) => {
                    if (resp.data[0]) {
                        this.APIMethod = 'PUT';
                    }
                    this.pageLoading = false;
                    this.seatime_entries.id = resp.data[0]['id'];
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
            editSeatime() {
                this.displayErrorMessage = false;
                let seatimeFields = {
                    user: localStorage.getItem('id'),
                };
                updateSeatimeEntries([this.APIMethod, seatimeFields, this.seatime_entries.id]).then(
                    () => {
                        this.snackbarText = 'Seatime updated successfully';
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