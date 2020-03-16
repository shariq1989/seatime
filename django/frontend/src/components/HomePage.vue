<template>
    <v-app id="inspire">
        <v-content>
            <v-container>
                <v-row class="text-center">
                    <v-col class="mb-4">
                        <h2 class="display-2 font-weight-bold mb-3">
                            Welcome to SeaTime
                        </h2>
                    </v-col>
                </v-row>
                <v-card
                        height="400"
                        class="overflow-hidden"
                >
                    <v-navigation-drawer
                            permanent
                    >
                        <v-list
                                dense
                                nav
                                class="py-0"
                        >
                            <v-list-item two-line :class="'px-0'">
                                <v-list-item-avatar>
                                    <img src="../assets/seatime.png" alt="">
                                </v-list-item-avatar>

                                <v-list-item-content>
                                    <v-list-item-title>Seatime</v-list-item-title>
                                    <v-list-item-subtitle>User</v-list-item-subtitle>
                                </v-list-item-content>
                            </v-list-item>

                            <v-divider></v-divider>

                            <v-list-item
                                    v-for="item in drawerOptions"
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
                </v-card>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        name: 'Home',
        date() {
            return {
                drawerOptions: [
                    {title: 'Dashboard', icon: 'mdi-view-dashboard'},
                    {title: 'Photos', icon: 'mdi-image'},
                    {title: 'About', icon: 'mdi-help-box'},
                ]
            }
        }
    };
</script>
