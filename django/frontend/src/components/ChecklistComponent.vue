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
              <!-- TODO              <div v-if="!pageLoading"> -->
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
                          <v-list-item v-else :key="item.title">
                            <v-list-item-content>
                              <template v-slot:activator="{ on, attrs }">
                                <v-list-item-title v-html="item.title"
                                                   @click.stop="dialog = true">
                                </v-list-item-title>
                              </template>
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
              <!--        for page loading </div> -->
            </v-card>
          </v-col>
          <v-col cols="12" sm="2"></v-col>
        </v-row>

        <v-dialog
            v-model="dialog"
            max-width="290"
        >
          <v-card>
            <v-card-title class="headline">
              Use Google's location service?
            </v-card-title>

            <v-card-text>
              Let Google help apps determine location. This means sending anonymous location data to Google, even when
              no apps are running.
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                  color="green darken-1"
                  text
                  @click="dialog = false"
              >
                Disagree
              </v-btn>

              <v-btn
                  color="green darken-1"
                  text
                  @click="dialog = false"
              >
                Agree
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
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
        {header: 'Select a position'},
        {
          title: 'Ntl DDE',
        },
        {divider: true, inset: true},
        {
          title: 'QMED',
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