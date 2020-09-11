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
                    <v-col>
                      <v-card-title>Misc.</v-card-title>
                    </v-col>
                    <v-col>
                      <v-row>

                      </v-row>
                      <v-row>
                        <v-checkbox v-model="documents.drug_test_compliant"
                                    label="Drug Test Compliance"></v-checkbox>
                      </v-row>
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