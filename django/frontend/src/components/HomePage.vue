<!--suppress JSUnusedGlobalSymbols -->
<template>
    <v-app id="inspire">
        <NavDrawerComponent/>
        <v-content>
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
    import NavDrawerComponent from "./NavDrawerComponent";

    export default {
        components: {NavDrawerComponent},
        data() {
            return {
                color: 'primary',
                profileLoading: true,
                userProfile: {},
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