<template>
    <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                           @input="updateModalStatus"/>
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
            <v-list-item v-on:click.stop="logoutDialog.displayStatus=true">
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
    import {funcLogout} from "../_services/user.service";
    import ConfirmModalComponent from "./ConfirmModalComponent";

    export default {
        components: {ConfirmModalComponent},
        data() {
            return {
                drawer: true,
                items: [
                    {title: 'Profile', icon: 'mdi-account'},
                    {title: 'Log Seatime', icon: 'mdi-ferry'},
                ],
                color: 'primary',
                logoutDialog: {
                    displayStatus: false,
                    dialogHeader: 'Confirm Logout',
                    dialogMessage: 'Are you sure you would like to proceed?'
                }
            }
        },
        logout() {
            this.logoutDialog = true;
        },
        methods: {
            updateModalStatus(value) {
                this.logoutDialog.displayStatus = false;
                if (value === true) {
                    funcLogout();
                }
            }
        }
    }
</script>