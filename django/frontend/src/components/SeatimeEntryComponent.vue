<!--suppress JSUnusedGlobalSymbols, JSUnfilteredForInLoop -->
<template>
    <v-app id="inspire" style="background-color: #bbdefb;">
        <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
        <v-content>
            <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                                   @input="updateModalStatus"/>
            <v-container fluid class="#bbdefb lighten-4 fill-height">
                <v-row class="mb-6">
                    <v-col cols="12" sm="1"></v-col>
                    <v-col cols="12" sm="10">
                        <v-snackbar v-model="snackbar">
                            {{ snackbarText }}
                        </v-snackbar>
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
                            <v-data-table
                                    :headers="headers"
                                    :items="trip_list"
                                    sort-by="depart_date"
                                    class="elevation-1"
                            >
                                <template v-slot:top>
                                    <v-toolbar flat color="white">
                                        <h1 style="font-family: serif" class="primary--text">
                                            Trip Log
                                        </h1>
                                        <v-spacer></v-spacer>
                                        <v-dialog v-model="dialog" max-width="800px">
                                            <template v-slot:activator="{ on, attrs }">
                                                <v-btn
                                                        color="primary"
                                                        dark
                                                        class="mb-2"
                                                        v-bind="attrs"
                                                        v-on="on"
                                                >New Trip
                                                </v-btn>
                                            </template>
                                            <v-card>
                                                <div class="pa-2">
                                                    <v-alert type="error" v-if="displayErrorMessage">
                                                        <span class="text-left" v-html="errorMessage"></span>
                                                    </v-alert>
                                                </div>
                                                <v-card-title>
                                                    <h1 style="font-family: serif" class="primary--text">
                                                        {{ formTitle }}</h1>
                                                </v-card-title>

                                                <v-card-text>
                                                    <v-row>
                                                        <v-col cols="12" sm="1"></v-col>
                                                        <v-col cols="12" sm="4">
                                                            <v-row>
                                                                <v-autocomplete
                                                                        v-model="editedItem.vessel"
                                                                        :items="vessel_list"
                                                                        hide-no-data
                                                                        item-text="name"
                                                                        item-value="id"
                                                                        label="Vessel"
                                                                        placeholder="Start typing to Search"
                                                                        :rules="[v => !!v || 'This is a required field']"
                                                                        required
                                                                ></v-autocomplete>
                                                            </v-row>
                                                            <v-row>
                                                                <v-autocomplete
                                                                        v-model="editedItem.rank"
                                                                        :items="positions_list"
                                                                        item-text="name"
                                                                        item-value="id"
                                                                        return-object
                                                                        label="Sailing Position"
                                                                        :rules="[v => !!v || 'This is a required field']"
                                                                        required
                                                                ></v-autocomplete>
                                                            </v-row>
                                                            <v-row>
                                                                <v-autocomplete
                                                                        v-model="editedItem.designation"
                                                                        v-if="editedItem.rank && editedItem.rank['designation'].length > 0"
                                                                        :items="editedItem.rank['designation']"
                                                                        item-text="name"
                                                                        item-value="id"
                                                                        label="Rating"
                                                                        :rules="[v => !!v || 'This is a required field']"
                                                                        required
                                                                ></v-autocomplete>
                                                            </v-row>
                                                        </v-col>
                                                        <v-col cols="12" sm="2"></v-col>
                                                        <v-col cols="12" sm="4">
                                                            <v-row>
                                                                <v-menu
                                                                        v-model="dateModal_depart"
                                                                        :close-on-content-click="false"
                                                                        :nudge-right="40"
                                                                        transition="scale-transition"
                                                                        offset-y
                                                                        min-width="290px"
                                                                >
                                                                    <template v-slot:activator="{ on }">
                                                                        <v-text-field
                                                                                v-model="editedItem.depart_date"
                                                                                label="Departure Date"
                                                                                readonly
                                                                                :rules="[v => !!v || 'This is a required field']"
                                                                                required
                                                                                v-on="on"
                                                                        ></v-text-field>
                                                                    </template>
                                                                    <v-date-picker v-model="editedItem.depart_date"
                                                                                   @input="dateModal_depart = false"></v-date-picker>
                                                                </v-menu>
                                                            </v-row>
                                                            <v-row>
                                                                <v-menu
                                                                        v-model="dateModal_arrival"
                                                                        :close-on-content-click="false"
                                                                        :nudge-right="40"
                                                                        transition="scale-transition"
                                                                        offset-y
                                                                        min-width="290px"
                                                                >
                                                                    <template v-slot:activator="{ on }">
                                                                        <v-text-field
                                                                                v-model="editedItem.arrival_date"
                                                                                label="Arrival Date"
                                                                                readonly
                                                                                :rules="[v => !!v || 'This is a required field']"
                                                                                required
                                                                                v-on="on"
                                                                        ></v-text-field>
                                                                    </template>
                                                                    <v-date-picker v-model="editedItem.arrival_date"
                                                                                   @input="dateModal_arrival = false"></v-date-picker>
                                                                </v-menu>
                                                            </v-row>
                                                            <v-row>
                                                                <v-autocomplete
                                                                        v-model="editedItem.voyage_type"
                                                                        :items="voyage_type_list"
                                                                        item-text="type"
                                                                        item-value="id"
                                                                        label="Voyage Type"
                                                                        :rules="[v => !!v || 'This is a required field']"
                                                                        required
                                                                ></v-autocomplete>
                                                            </v-row>
                                                            <v-row>
                                                                <v-autocomplete
                                                                        v-model="editedItem.workday_type"
                                                                        :items="workday_type_list"
                                                                        item-text="type"
                                                                        item-value="id"
                                                                        label="Workday Type"
                                                                        :rules="[v => !!v || 'This is a required field']"
                                                                        required
                                                                ></v-autocomplete>
                                                            </v-row>
                                                        </v-col>
                                                        <v-col cols="12" sm="1"></v-col>
                                                    </v-row>
                                                </v-card-text>
                                                <v-card-actions>
                                                    <v-spacer></v-spacer>
                                                    <v-btn color="primary" type="submit" @click.stop="editSeatime">Save
                                                    </v-btn>
                                                    <v-btn color="accent" @click.stop="close">Cancel</v-btn>
                                                </v-card-actions>
                                            </v-card>
                                        </v-dialog>
                                    </v-toolbar>
                                </template>
                                <template v-slot:item.actions="{ item }">
                                    <v-icon
                                            small
                                            class="mr-2"
                                            @click="editItem(item)"
                                    >
                                        mdi-pencil
                                    </v-icon>
                                    <v-icon
                                            small
                                            @click="deleteItem(item)"
                                    >
                                        mdi-delete
                                    </v-icon>
                                </template>
                                <template v-slot:no-data>
                                    <v-btn color="primary" @click="initialize">Reset</v-btn>
                                </template>
                            </v-data-table>
                        </div>
                    </v-col>
                    <v-col cols="12" sm="1"></v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {funcLogout} from "../_services/user.service";
    import ConfirmModalComponent from "./ConfirmModalComponent"
    import NavDrawerComponent from "./NavDrawerComponent";
    import {
        getSeatimeEntries, getStaffPositions, getVessels, getVoyageTypes, getWorkdayType, updateSeatimeEntries
    } from "../_services/seatime_entry.service";

    export default {
        components: {NavDrawerComponent, ConfirmModalComponent},
        data() {
            return {
                drawer: 'true',
                color: 'primary',
                pageLoading: true,
                dateModal_depart: false,
                dateModal_arrival: false,
                displayErrorMessage: false,
                errorMessage: '',
                snackbar: false,
                snackbarText: null,
                vessel_list: null,
                positions_list: [],
                voyage_type_list: null,
                workday_type_list: null,
                trip_list: null,
                seatime_entries: {
                    vessel: null,
                    depart_date: null,
                    arrival_date: null,
                    voyage_type: null,
                    workday_type: null,
                    position: null,
                    rating: null,
                    id: null
                },
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                },
                APIMethod: 'POST',

                dialog: false,
                headers: [
                    {text: 'Vessel', value: 'vessel.name'},
                    {text: 'Departure', value: 'depart_date'},
                    {text: 'Arrival', value: 'arrival_date'},
                    {text: 'Voyage', value: 'voyage_type.type'},
                    {text: 'Workday', value: 'workday_type.type'},
                    {text: 'Position', value: 'rank.name'},
                    {text: 'Rating', value: 'designation.name'},
                    {text: 'Actions', value: 'actions', sortable: false},
                ],
                editedIndex: -1,
                editedItem: {
                    vessel: null,
                    depart_date: null,
                    arrival_date: null,
                    voyage_type: null,
                    workday_type: null,
                    rank: null,
                    designation: null
                },
                defaultItem: {
                    vessel: null,
                    depart_date: null,
                    arrival_date: null,
                    voyage_type: null,
                    workday_type: null,
                    rank: null,
                    designation: null
                },
            }
        },
        methods: {
            loadPage: function () {
                getVessels().then((resp) => {
                    this.vessel_list = resp.data;
                })
                getStaffPositions().then((resp) => {
                    console.log(resp);
                    this.positions_list = resp.data;
                })
                getVoyageTypes().then((resp) => {
                    this.voyage_type_list = resp.data;
                })
                getWorkdayType().then((resp) => {
                    this.workday_type_list = resp.data;
                })
                getSeatimeEntries().then((resp) => {
                    console.log(resp);
                    this.trip_list = resp.data;
                    this.pageLoading = false;
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
                if (this.editedItem.depart_date !== null &&
                    this.editedItem.arrival_date !== null &&
                    this.editedItem.rank !== null &&
                    this.editedItem.vessel !== null &&
                    this.editedItem.voyage_type !== null &&
                    this.editedItem.workday_type !== null
                ) {
                    if (this.editedItem.rank.designation.length === 0) {
                        this.editedItem.designation = null;
                    }
                    let seatimeFields = {
                        user: localStorage.getItem('id'),
                        vessel: this.editedItem.vessel,
                        depart_date: this.editedItem.depart_date,
                        arrival_date: this.editedItem.arrival_date,
                        voyage_type: this.editedItem.voyage_type,
                        workday_type: this.editedItem.workday_type,
                        rank: this.editedItem.rank.id,
                        designation: this.editedItem.designation
                    };
                    if (!Number.isInteger(seatimeFields.voyage_type)) {
                        seatimeFields.voyage_type = this.editedItem.voyage_type.id;
                    }
                    if (!Number.isInteger(seatimeFields.workday_type)) {
                        seatimeFields.workday_type = this.editedItem.workday_type.id;
                    }
                    if (!Number.isInteger(seatimeFields.vessel)) {
                        seatimeFields.vessel = this.editedItem.vessel.id;
                    }
                    console.log(seatimeFields);
                    this.pageLoading = true;
                    if (this.editedIndex === -1) {
                        this.APIMethod = 'POST';
                    } else {
                        this.APIMethod = 'PUT';
                    }
                    updateSeatimeEntries([this.APIMethod, seatimeFields, this.editedItem.id]).then(
                        () => {
                            this.snackbarText = 'Trip saved successfully';
                            this.snackbar = true;
                            this.dialog = false
                            this.loadPage();
                            this.pageLoading = false;
                        }
                    ).catch(err => {
                            console.log(err.response.data);
                            this.displayErrorMessage = true;
                            this.errorMessage = 'Error updating documents';
                            this.pageLoading = false;
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
                } else {
                    this.displayErrorMessage = true;
                    this.errorMessage = 'Please complete all fields before saving.';
                }
            },
            editItem(item) {
                this.editedIndex = this.trip_list.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            }
            ,
            deleteItem(item) {
                if (confirm('Are you sure you want to delete this trip?')) {
                    this.pageLoading = true;
                    updateSeatimeEntries(['DELETE', item, item.id]).then(
                        () => {
                            this.snackbarText = 'Trip deleted';
                            this.snackbar = true;
                            this.loadPage().then(
                                this.pageLoading = false
                            );
                        }
                    ).catch(err => {
                            this.pageLoading = false;
                            console.log(err.response);
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
            close() {
                this.dialog = false
                this.$nextTick(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                })
            }
            ,
        },
        mounted() {
            this.loadPage();
        },
        computed: {
            formTitle() {
                return this.editedIndex === -1 ? 'New Trip' : 'Edit Trip'
            },
        },
        watch: {
            dialog(val) {
                val || this.close()
            },
        },

    }
</script>