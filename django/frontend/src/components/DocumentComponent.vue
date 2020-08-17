<!--suppress JSUnusedGlobalSymbols, JSUnfilteredForInLoop -->
<template>
  <v-app id="inspire" style="background-color: #bbdefb;">
    <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
    <v-content>
      <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                             @input="updateModalStatus"/>
      <v-container fluid class="#bbdefb lighten-4 fill-height">
        <v-row class="mb-6">
          <v-col cols="12" sm="2"></v-col>
          <v-col cols="12" sm="8">
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Documents
              </h1>
              <div v-if="pageLoading">
                <v-progress-circular
                    indeterminate
                    color="primary"
                />
                <v-card-text>
                  Loading
                </v-card-text>
              </div>
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
                      <v-card-title>Merchant Mariner Credential</v-card-title>
                    </v-col>
                    <v-col>
                      <v-row>
                        <v-text-field
                            v-model=documents.mariner_ref_num
                            label="Mariner Reference Number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-text-field
                            v-model=documents.mmc_doc_num
                            label="MMC Document Number"
                        ></v-text-field>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_mmc_issue"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.mmc_issue_date"
                                label="MMC Issue Date"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.mmc_issue_date"
                                         @input="dateModal_mmc_issue = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_mmc_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.mmc_expr_date"
                                label="MMC Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.mmc_expr_date"
                                         @input="dateModal_mmc_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card-title>Medical</v-card-title>
                    </v-col>
                    <v-col>
                      <v-row>
                        <v-menu
                            v-model="dateModal_med_ntl_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.med_ntl_expr_date"
                                label="Medical National Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.med_ntl_expr_date"
                                         @input="dateModal_med_ntl_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_med_stcw_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.med_stcw_expr_date"
                                label="Medical STCW Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.med_stcw_expr_date"
                                         @input="dateModal_med_stcw_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_med_pilot_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.med_pilot_expr_date"
                                label="Medical Pilot Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.med_pilot_expr_date"
                                         @input="dateModal_med_pilot_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card-title>Misc.</v-card-title>
                    </v-col>
                    <v-col>
                      <v-row>
                        <v-menu
                            v-model="dateModal_twic_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.twic_expr_date"
                                label="TWIC Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.twic_expr_date"
                                         @input="dateModal_twic_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_passport_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.passport_expr_date"
                                label="Passport Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.passport_expr_date"
                                         @input="dateModal_passport_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-checkbox v-model="documents.drug_test_compliant"
                                    label="Drug Test Compliance"></v-checkbox>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col>
                      <v-card-title>Training</v-card-title>
                    </v-col>
                    <v-col>
                      <v-row>
                        <v-menu
                            v-model="dateModal_basic_trng_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.basic_training_expr_date"
                                label="Basic Training Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.basic_training_expr_date"
                                         @input="dateModal_basic_trng_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_adv_fire_exp"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.advanced_fire_expr_date"
                                label="Advanced Firefighting Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.advanced_fire_expr_date"
                                         @input="dateModal_adv_fire_exp = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                      <v-row>
                        <v-menu
                            v-model="dateModal_first_aid"
                            :close-on-content-click="false"
                            :nudge-right="40"
                            transition="scale-transition"
                            offset-y
                            min-width="290px"
                        >
                          <template v-slot:activator="{ on }">
                            <v-text-field
                                v-model="documents.first_aid_cpr_expr_date"
                                label="First Aid & CPR Expiration"
                                readonly
                                :rules="[v => !!v || 'This is a required field']"
                                required
                                v-on="on"
                            ></v-text-field>
                          </template>
                          <v-date-picker v-model="documents.first_aid_cpr_expr_date"
                                         @input="dateModal_first_aid = false"></v-date-picker>
                        </v-menu>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-card-text>
                <v-card-actions>
                  <v-spacer/>
                  <v-btn color="primary" @click.stop="editDocuments">Save Changes</v-btn>
                </v-card-actions>
              </div>
            </v-card>
          </v-col>
          <v-col cols="12" sm="2"></v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import {funcLogout} from "../_services/user.service";
import ConfirmModalComponent from "./ConfirmModalComponent"
import NavDrawerComponent from "./NavDrawerComponent";
import {getDocuments, updateDocuments} from "../_services/profile.service";

export default {
  components: {NavDrawerComponent, ConfirmModalComponent},
  data() {
    return {
      drawer: 'true',
      color: 'primary',
      pageLoading: true,

      dateModal_mmc_issue: false,
      dateModal_mmc_exp: false,
      dateModal_med_ntl_exp: false,
      dateModal_med_stcw_exp: false,
      dateModal_med_pilot_exp: false,
      dateModal_twic_exp: false,
      dateModal_passport_exp: false,
      dateModal_basic_trng_exp: false,
      dateModal_adv_fire_exp: false,
      dateModal_first_aid: false,

      displayErrorMessage: false,
      errorMessage: '',
      snackbar: false,
      snackbarText: null,
      documents: {
        mariner_ref_num: null,
        mmc_doc_num: null,
        mmc_issue_date: null,
        mmc_expr_date: null,
        med_ntl_expr_date: null,
        med_stcw_expr_date: null,
        med_pilot_expr_date: null,
        twic_expr_date: null,
        basic_training_expr_date: null,
        advanced_fire_expr_date: null,
        first_aid_cpr_expr_date: null,
        passport_expr_date: null,
        drug_test_compliant: false,
        id: null
      },
      logoutDialog: {
        displayStatus: false,
        dialogHeader: 'Confirm Logout',
        dialogMessage: 'Are you sure you would like to proceed?'
      },
      APIMethod: 'POST',
    }
  },
  methods: {
    loadPage: () => {
      getDocuments().then((resp) => {
        if (resp.data[0]) {
          this.APIMethod = 'PUT';
        }
        this.pageLoading = false;
        this.documents.id = resp.data[0]['id'];
        this.documents.mariner_ref_num = resp.data[0]['mariner_ref_num'];
        this.documents.mmc_doc_num = resp.data[0]['mmc_doc_num'];
        this.documents.mmc_issue_date = resp.data[0]['mmc_issue_date'];
        this.documents.mmc_expr_date = resp.data[0]['mmc_expr_date'];
        this.documents.med_ntl_expr_date = resp.data[0]['med_ntl_expr_date'];
        this.documents.med_stcw_expr_date = resp.data[0]['med_stcw_expr_date'];
        this.documents.med_pilot_expr_date = resp.data[0]['med_pilot_expr_date'];
        this.documents.twic_expr_date = resp.data[0]['twic_expr_date'];
        this.documents.basic_training_expr_date = resp.data[0]['basic_training_expr_date'];
        this.documents.advanced_fire_expr_date = resp.data[0]['advanced_fire_expr_date'];
        this.documents.first_aid_cpr_expr_date = resp.data[0]['first_aid_cpr_expr_date'];
        this.documents.passport_expr_date = resp.data[0]['passport_expr_date'];
        this.documents.drug_test_compliant = resp.data[0]['drug_test_compliant'];
      }).catch(() => {
        this.pageLoading = false;
      })
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
    editDocuments() {
      this.displayErrorMessage = false;
      this.pageLoading = true;
      let documentFields = {
        mariner_ref_num: this.documents.mariner_ref_num,
        mmc_doc_num: this.documents.mmc_doc_num,
        mmc_issue_date: this.documents.mmc_issue_date,
        mmc_expr_date: this.documents.mmc_expr_date,
        med_ntl_expr_date: this.documents.med_ntl_expr_date,
        med_stcw_expr_date: this.documents.med_stcw_expr_date,
        med_pilot_expr_date: this.documents.med_pilot_expr_date,
        twic_expr_date: this.documents.twic_expr_date,
        basic_training_expr_date: this.documents.basic_training_expr_date,
        advanced_fire_expr_date: this.documents.advanced_fire_expr_date,
        first_aid_cpr_expr_date: this.documents.first_aid_cpr_expr_date,
        passport_expr_date: this.documents.passport_expr_date,
        drug_test_compliant: this.documents.drug_test_compliant,
        user: localStorage.getItem('id'),
      };
      updateDocuments([this.APIMethod, documentFields, this.documents.id]).then(
          () => {
            this.snackbarText = 'Documents updated successfully';
            this.snackbar = true;
            this.loadPage();
            this.pageLoading = false;
          }
      ).catch(err => {
            this.pageLoading = false;
            console.log(err);
            this.displayErrorMessage = true;
            this.errorMessage = 'Error updating documents';
            if (err.response.data) {
              for (const field in err.response.data) {
                for (const error of err.response.data[field]) {
                  this.errorMessage += '<br/>';
                  this.errorMessage += error;
                }
              }
            }
          }
      )
    }
  },
  mounted() {
    this.loadPage();
  }
}
</script>