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
                                    <div class="pa-2">
                                        <v-alert type="error" v-if="displayErrorMessage">
                                            <span class="text-left" v-html="errorMessage"></span>
                                        </v-alert>
                                        <v-snackbar v-model="snackbar">
                                            {{ snackbarText }}
                                        </v-snackbar>
                                    </div>
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
                                    <v-menu
                                            v-model="dateModal"
                                            :close-on-content-click="false"
                                            :nudge-right="40"
                                            transition="scale-transition"
                                            offset-y
                                            min-width="290px"
                                    >
                                        <template v-slot:activator="{ on }">
                                            <v-text-field
                                                    v-model="userProfile.birth_date"
                                                    label="Birth Date"
                                                    readonly
                                                    v-on="on"
                                            ></v-text-field>
                                        </template>
                                        <v-date-picker v-model="userProfile.birth_date"
                                                       @input="dateModal = false"></v-date-picker>
                                    </v-menu>
                                    <v-autocomplete
                                            v-model="userProfile.citizenship_cntry"
                                            :items="countries"
                                            label="Citizenship"
                                    ></v-autocomplete>
                                    <v-autocomplete
                                            v-model=userProfile.residence_state
                                            :items="us_states"
                                            label="Residence State (US)"
                                    ></v-autocomplete>
                                </v-card-text>
                            </div>
                            <v-card-actions>
                                <v-spacer/>
                                <v-btn color="primary" @click.stop="editProfile">Save Changes
                                </v-btn>
                                <!-- TODO -- have to discuss account deletion
                                <v-btn color="error" @click.stop="deleteAccount">Confirm</v-btn>
                                -->
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {getProfile, updateProfile} from "../_services/profile.service";
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
                dateModal: false,
                displayErrorMessage: false,
                snackbar: false,
                snackbarText: null,
                countries: [
                    "Afghanistan", "Aland Islands", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Barbuda", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Trty.", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Caicos Islands", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "French Polynesia", "French Southern Territories", "Futuna Islands", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard", "Herzegovina", "Holy See", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Jamaica", "Jan Mayen Islands", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea", "Korea (Democratic)", "Kuwait", "Kyrgyzstan", "Lao", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "McDonald Islands", "Mexico", "Micronesia", "Miquelon", "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "Nevis", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Palestinian Territory, Occupied", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Principe", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Barthelemy", "Saint Helena", "Saint Kitts", "Saint Lucia", "Saint Martin (French part)", "Saint Pierre", "Saint Vincent", "Samoa", "San Marino", "Sao Tome", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia", "South Sandwich Islands", "Spain", "Sri Lanka", "Sudan", "Suriname", "Svalbard", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "The Grenadines", "Timor-Leste", "Tobago", "Togo", "Tokelau", "Tonga", "Trinidad", "Tunisia", "Turkey", "Turkmenistan", "Turks Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "US Minor Outlying Islands", "Uzbekistan", "Vanuatu", "Vatican City State", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (US)", "Wallis", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
                ],
                us_states: ["N/A", "Alaska",
                    "Alabama",
                    "Arkansas",
                    "American Samoa",
                    "Arizona",
                    "California",
                    "Colorado",
                    "Connecticut",
                    "District of Columbia",
                    "Delaware",
                    "Florida",
                    "Georgia",
                    "Guam",
                    "Hawaii",
                    "Iowa",
                    "Idaho",
                    "Illinois",
                    "Indiana",
                    "Kansas",
                    "Kentucky",
                    "Louisiana",
                    "Massachusetts",
                    "Maryland",
                    "Maine",
                    "Michigan",
                    "Minnesota",
                    "Missouri",
                    "Mississippi",
                    "Montana",
                    "North Carolina",
                    " North Dakota",
                    "Nebraska",
                    "New Hampshire",
                    "New Jersey",
                    "New Mexico",
                    "Nevada",
                    "New York",
                    "Ohio",
                    "Oklahoma",
                    "Oregon",
                    "Pennsylvania",
                    "Puerto Rico",
                    "Rhode Island",
                    "South Carolina",
                    "South Dakota",
                    "Tennessee",
                    "Texas",
                    "Utah",
                    "Virginia",
                    "Virgin Islands",
                    "Vermont",
                    "Washington",
                    "Wisconsin",
                    "West Virginia",
                    "Wyoming"],
                userProfile: {
                    first_name: null,
                    middle_name: null,
                    last_name: '',
                    birth_date: null,
                    citizenship_cntry: null,
                    residence_state: 'N/A',
                    id: null
                },
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                },
                profileAPIMethod: 'POST',
            }
        },
        methods: {
            loadProfile: function () {
                getProfile().then((resp) => {
                    if (resp.data[0]) {
                        this.profileAPIMethod = 'PUT';
                    }
                    this.profileLoading = false;
                    this.userProfile.id = resp.data[0]['id'];
                    this.userProfile.first_name = resp.data[0]['first_name'];
                    this.userProfile.middle_name = resp.data[0]['middle_name'];
                    this.userProfile.last_name = resp.data[0]['last_name'];
                    this.userProfile.birth_date = resp.data[0]['birth_date'];
                    this.userProfile.citizenship_cntry = resp.data[0]['citizenship_cntry'];
                    this.userProfile.residence_state = resp.data[0]['residence_state'];
                }).catch(() => {
                    this.profileLoading = false;
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
            editProfile() {
                let profileFields = {
                    first_name: this.userProfile.first_name,
                    middle_name: this.userProfile.middle_name,
                    last_name: this.userProfile.last_name,
                    birth_date: this.userProfile.birth_date,
                    citizenship_cntry: this.userProfile.citizenship_cntry,
                    residence_state: this.userProfile.residence_state,
                    user: localStorage.getItem('id'),
                };
                updateProfile([this.profileAPIMethod, profileFields, this.userProfile.id]).then(
                    () => {
                        this.snackbarText = 'Profile updates successfully';
                        this.snackbar = true;
                    }
                ).catch(err => {
                        console.log(err.response.data);
                        this.displayErrorMessage = true;
                        this.errorMessage = 'Error updating profile';
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
            this.loadProfile();
        }
    }
</script>