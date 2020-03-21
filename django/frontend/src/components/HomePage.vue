<template>
    <v-app id="inspire">
        <v-content>
            <v-container>
                <v-navigation-drawer
                        v-model="drawer"
                        :color="color"
                        :expand-on-hover="expandOnHover"
                        :mini-variant="miniVariant"
                        :right="right"
                        absolute
                        dark
                >
                    <v-list
                            dense
                            nav
                            class="py-0"
                    >
                        <v-list-item two-line :class="miniVariant && 'px-0'">
                            <v-list-item-avatar>
                                <img src="../assets/seatime.png">
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
                </v-navigation-drawer>
                <v-card>
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
                            <li v-for="(prop, val) in userProfile" :key="prop">{{prop}} : {{val}}</li>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="primary">Edit Profile</v-btn>
                        </v-card-actions>
                    </div>
                </v-card>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {getProfile} from "../_services/profile.service";

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
                userProfile: {}
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
            }
        },
        mounted() {
            this.loadProfile();
        }
    }
</script>