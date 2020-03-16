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
                        :src="bg"
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
                                <v-list-item-title>Application</v-list-item-title>
                                <v-list-item-subtitle>Subtext</v-list-item-subtitle>
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
            }
        },
        computed: {
            bg() {
                return this.background ? 'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg' : undefined
            },
        },
    }
</script>