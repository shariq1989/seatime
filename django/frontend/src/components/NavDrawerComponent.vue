<template>
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

            <v-divider/>

            <v-list-item
                    v-for="item in items"
                    :key="item.title"
                    link
                    :to="item.link"
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
            <v-list-item v-on:click.stop="onLogoutClick(false)">
                <v-list-item-icon>
                    <v-icon style="color: #0f0f0f">mdi-logout</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                    <v-list-item-title style="color: #0f0f0f">Logout</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </template>
    </v-navigation-drawer>
</template>
<script>
    export default {
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Profile', icon: 'mdi-account', link: '/profile'},
                    {title: 'Documents', icon: 'mdi-file-document', link: '/document'},
                    {title: 'Log Seatime', icon: 'mdi-ferry', link: '/seatime_entry'},
                ],
                color: 'primary',
            }
        },
        methods: {
            onLogoutClick(action) {
                this.$emit('input', action)
            }
        }
    }
</script>