<template>
    <v-app id="inspire">
        <v-navigation-drawer v-model="drawer" expand-on-hover permanent app>
            <v-list>
                <v-list-item class="px-2">
                    <v-list-item-avatar>
                        <img src="../assets/seatime.png" alt="">
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title>Seatime</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>

                <v-divider></v-divider>

                <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        link
                >
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
            <template v-slot:append>
                <v-list-item>
                    <v-list-item-icon>
                        <v-icon style="color: #0f0f0f">mdi-logout</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title style="color: #0f0f0f">Logout</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </template>
        </v-navigation-drawer>
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
                                ></v-progress-circular>
                                <v-card-text>
                                    User Profile Loading
                                </v-card-text>
                            </div>
                            <div v-if="!profileLoading">
                                <v-card-text>
                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Name
                                    </p>
                                    <p class="text-left">{{userProfile["first_name"]}} {{userProfile["middle_name"]}}
                                        {{userProfile["last_name"]}}</p>

                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Birth Date
                                    </p>
                                    <p class="text-left">{{userProfile["birth_date"]}}</p>

                                    <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                                        Mariner Reference Number
                                    </p>
                                    <p class="text-left">{{userProfile["mariner_ref_num"]}}</p>

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
                            ></v-progress-circular>
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
                            ></v-progress-circular>
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

    export default {
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Profile', icon: 'mdi-account'},
                    {title: 'Log Seatime', icon: 'mdi-ferry'},
                ],
                color: 'primary',
                colors: [
                    'primary',
                    'blue',
                    'success',
                    'red',
                    'teal',
                ],
                right: false,
                miniVariant: false,
                expandOnHover: false,
                background: false,
                profileLoading: true,
                userProfile: {},
                logoutDialog: false
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
                this.logoutDialog = false;
                funcLogout();
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