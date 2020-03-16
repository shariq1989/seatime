<template>
    <v-app id="inspire">
        <v-content>
            <v-container>
                <v-navigation-drawer
                        v-model="drawer"
                        dark
                >
                    <v-list
                            dense
                            nav
                            class="py-0"
                    >
                        <v-list-item two-line>
                            <v-list-item-avatar>
                                <img src="../assets/seatime.png">
                            </v-list-item-avatar>

                            <v-list-item-content>
                                <v-list-item-title>Seatime</v-list-item-title>
                                <v-list-item-subtitle>User</v-list-item-subtitle>
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
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Profile', icon: 'mdi-account-box'},
                    {title: 'Log Seatime', icon: 'mdi-file-document-box'},
                ],
            }
        },
    }
</script>