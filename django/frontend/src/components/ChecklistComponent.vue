<!--suppress JSUnusedGlobalSymbols, JSUnfilteredForInLoop -->
<template>
  <v-app id="inspire" style="background-color: #bbdefb;">
    <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
    <v-main>
      <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                             @input="updateModalStatus"/>
      <v-container fluid class="#bbdefb lighten-4 fill-height">
        <v-row class="mb-6">
          <v-col cols="12" sm="2"></v-col>
          <v-col cols="12" sm="8">
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Checklists
              </h1>
              <div v-if="!pageLoading">
                <v-card-text>
                  <div class="pa-2">
                    <v-alert type="error" v-if="displayErrorMessage">
                      <span class="text-left" v-html="errorMessage"></span>
                    </v-alert>
                    <v-snackbar v-model="snackbar">
                      {{ snackbarText }}
                    </v-snackbar>
                  </div>
                  <v-row>
                    <v-col cols="12" sm="6" offset-sm="3">
                      <v-card>
                        <v-list two-line>
                          <template v-for="(item, index) in items.slice(0, 6)">
                            <v-subheader v-if="item.header" :key="item.header">{{ item.header }}</v-subheader>
                            <v-divider v-else-if="item.divider" :key="index" :inset="item.inset"></v-divider>
                            <v-list-item v-else :key="item.title" @click="">
                              <v-list-item-avatar>
                                <img :src="item.avatar">
                              </v-list-item-avatar>
                              <v-list-item-content>
                                <v-list-item-title v-html="item.title"></v-list-item-title>
                                <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
                              </v-list-item-content>
                            </v-list-item>
                          </template>
                        </v-list>
                      </v-card>
                    </v-col>
                  </v-row>
                </v-card-text>
                <v-card-actions>
                  <v-spacer/>
                </v-card-actions>
              </div>
            </v-card>
          </v-col>
          <v-col cols="12" sm="2"></v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import {funcLogout} from "../_services/user.service";
import ConfirmModalComponent from "./ConfirmModalComponent"
import NavDrawerComponent from "./NavDrawerComponent";

export default {
  components: {NavDrawerComponent, ConfirmModalComponent},
  data() {
    return {
      drawer: 'true',
      color: 'primary',
      pageLoading: true,
      displayErrorMessage: false,
      errorMessage: '',
      snackbar: false,
      snackbarText: null,
      logoutDialog: {
        displayStatus: false,
        dialogHeader: 'Confirm Logout',
        dialogMessage: 'Are you sure you would like to proceed?'
      },
      APIMethod: 'POST',

      items: [
        {header: 'Today'},
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Brunch this weekend?',
          subtitle: "<span class='font-weight-bold'>Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?"
        },
        {divider: true, inset: true},
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ <span class="grey--text text--lighten-1">4</span>',
          subtitle: "<span class='font-weight-bold'>to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend."
        },
        {divider: true, inset: true},
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: "<span class='font-weight-bold'>Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?"
        },
      ],
    }
  },
  methods: {
    loadPage() {
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
  },
  mounted() {
    this.loadPage();
  }
}
</script>