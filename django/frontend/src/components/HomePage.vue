<!--suppress JSUnusedGlobalSymbols -->
<template>
  <v-app id="inspire" style="background-color: #bbdefb;">
    <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
    <v-content>
      <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                             @input="updateModalStatus"/>
      <v-container fluid class="#bbdefb lighten-4 fill-height">
        <v-row class="mb-6">
          <v-col>
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Profile
              </h1>
              <div v-if="profileLoading">
                <v-progress-circular
                    indeterminate
                    color="primary"
                />
                <v-card-text>
                  User Profile Loading
                </v-card-text>
              </div>
              <div v-if="!profileLoading && !userProfile">
                <v-card-text>
                  You need to complete this section
                </v-card-text>
              </div>
              <div v-if="!profileLoading && userProfile">
                <v-card-text>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Name
                  </p>
                  <p class="text-left">{{ userProfile["first_name"] }}
                    {{ userProfile["middle_name"] }}
                    {{ userProfile["last_name"] }}</p>

                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Birth Date
                  </p>
                  <p class="text-left">{{ userProfile["birth_date"] }}</p>

                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Citizenship
                  </p>
                  <p class="text-left">{{ userProfile["citizenship_cntry"] }}</p>

                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Residence
                  </p>
                  <p class="text-left">{{ userProfile["residence_state"] }}</p>
                </v-card-text>
              </div>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Documents
              </h1>
              <div v-if="documentsLoading">
                <v-progress-circular
                    indeterminate
                    color="primary"
                />
                <v-card-text>
                  Documents Loading
                </v-card-text>
              </div>
              <div v-if="!documentsLoading && !documents">
                <v-card-text>
                  You need to complete this section
                </v-card-text>
              </div>
              <div v-if="!documentsLoading && documents">
                <v-card-text>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Mariner Ref
                  </p>
                  <p class="text-left">{{ documents["mariner_ref_num"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    MMC Document Number
                  </p>
                  <p class="text-left">{{ documents["mmc_doc_num"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    MMC Issue
                  </p>
                  <p class="text-left">{{ documents["mmc_issue_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    MMC Expiration
                  </p>
                  <p class="text-left">{{ documents["mmc_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Medical National Expiration
                  </p>
                  <p class="text-left">{{ documents["med_ntl_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Medical STCW Expiration
                  </p>
                  <p class="text-left">{{ documents["med_stcw_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Medical Pilot Expiration
                  </p>
                  <p class="text-left">{{ documents["med_pilot_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    TWIC Expiration
                  </p>
                  <p class="text-left">{{ documents["twic_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Basic Training Expiration
                  </p>
                  <p class="text-left">{{ documents["basic_training_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Advanced Firefighting Expiration
                  </p>
                  <p class="text-left">{{ documents["advanced_fire_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    First Aid & CPR Expiration
                  </p>
                  <p class="text-left">{{ documents["first_aid_cpr_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Passport Expiration
                  </p>
                  <p class="text-left">{{ documents["passport_expr_date"] }}</p>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    Drug Test Expiration
                  </p>
                  <p class="text-left">{{ documents["drug_test_compliant"] }}</p>
                </v-card-text>
              </div>
            </v-card>
          </v-col>
          <v-col>
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Trips
              </h1>
              <div v-if="tripsLoading">
                <v-progress-circular
                    indeterminate
                    color="primary"
                />
                <v-card-text>
                  Loading Trips
                </v-card-text>
              </div>
              <div v-if="!tripsLoading && !trips">
                <v-card-text>
                  You need to complete this section
                </v-card-text>
              </div>
              <div v-if="!tripsLoading && trips">
                <v-card-text>
                  <p class="text-left subtitle-2 tag-title" style="margin: 0;">
                    You have logged {{ trips.length }} trips
                  </p>
                </v-card-text>
              </div>
            </v-card>
          </v-col>
        </v-row>
        <v-row class="mb-6">
          <v-col>
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Progress
              </h1>
              <div>
                <v-card-text>
                  <div>
                    <v-progress-linear
                        v-model="power"
                        color="amber"
                        height="25"
                    >
                      <template v-slot="{ value }">
                        <strong>{{ Math.ceil(value) }}%</strong>
                      </template>
                    </v-progress-linear>

                    <br>

                    <v-progress-linear
                        v-model="skill"
                        color="blue-grey"
                        height="25"
                    >
                      <template v-slot="{ value }">
                        <strong>{{ Math.ceil(value) }}%</strong>
                      </template>
                    </v-progress-linear>

                    <br>

                    <v-progress-linear
                        v-model="knowledge"
                        height="25"
                    >
                      <strong>{{ Math.ceil(knowledge) }}%</strong>
                    </v-progress-linear>
                  </div>
                  <div>
                    <apexchart width="500" type="bar" :options="options" :series="series"></apexchart>
                  </div>
                </v-card-text>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import {getDocuments, getProfile} from "../_services/profile.service";
import {funcLogout} from "../_services/user.service";
import ConfirmModalComponent from "./ConfirmModalComponent"
import NavDrawerComponent from "./NavDrawerComponent";
import {getSeatimeEntries} from "../_services/seatime_entry.service";

export default {
  components: {NavDrawerComponent, ConfirmModalComponent},
  data() {
    return {
      options: {
        chart: {
          id: 'vuechart-example'
        },
        xaxis: {
          categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
        }
      },
      series: [{
        name: 'series-1',
        data: [30, 40, 45, 50, 49, 60, 70, 91]
      }],
      drawer: 'true',
      color: 'primary',
      profileLoading: true,
      documentsLoading: true,
      tripsLoading: true,
      userProfile: {},
      documents: {},
      trips: [],
      skill: 20,
      knowledge: 33,
      power: 78,
      logoutDialog: {
        displayStatus: false,
        dialogHeader: 'Confirm Logout',
        dialogMessage: 'Are you sure you would like to proceed?'
      }
    }
  },
  methods: {
    loadData: function () {
      getProfile().then((resp) => {
        console.log(resp.data);
        this.profileLoading = false;
        this.userProfile = resp.data[0];
      }).catch((error) => {
        console.log(error)
        this.profileLoading = false;
        this.userProfile = {error: 'Error loading profile'};
      });
      getDocuments().then((resp) => {
        console.log(resp.data);
        this.documentsLoading = false;
        this.documents = resp.data[0];
      }).catch((error) => {
        console.log(error)
        this.documentsLoading = false;
        this.documents = {error: 'Error loading documents'};
      });
      getSeatimeEntries().then((resp) => {
        console.log(resp.data);
        this.tripsLoading = false;
        this.trips = resp.data;
      }).catch((error) => {
        console.log(error)
        this.tripsLoading = false;
        this.trips = {error: 'Error loading trips'};
      });
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
    }
  },
  mounted() {
    this.loadData();
  }
}
</script>

<style>
.tag-title {
  color: gray;
}

</style>