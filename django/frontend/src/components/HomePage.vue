<!--suppress JSUnusedGlobalSymbols -->
<template>
  <v-app id="inspire" style="background-color: #bbdefb;">
    <NavDrawerComponent v-model="drawer" @input="displayLogoutDialog"/>
    <v-main>
      <ConfirmModalComponent v-model="logoutDialog.displayStatus" v-bind="logoutDialog"
                             @input="updateModalStatus"/>
      <v-container fluid class="#bbdefb lighten-4 fill-height">
        <v-row class="mb-6">
          <v-col>
            <v-card class="pa-2">
              <h1 style="font-family: serif" class="primary--text">
                Seatime Progression
              </h1>
              <div>
                <v-card-text>
                  <div>
                    <apexchart width="1000" type="bar" :options="options" :series="series"></apexchart>
                  </div>
                </v-card-text>
              </div>
            </v-card>
          </v-col>
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
      options: {
        chart: {
          type: 'bar',
          height: 350,
          stacked: true,
          stackType: '100%'
        },
        colors: ['#3f51b5', '#757573'],
        plotOptions: {
          bar: {
            horizontal: true,
          },
        },
        stroke: {
          width: 5,
          colors: ['#fff']
        },
        xaxis: {
          categories: ['2A/E Unlimited', 'DDE Unlimited', 'Chief UFIV', 'Chief OSV'],
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return val + " hours"
            }
          }
        },
        fill: {
          opacity: 1
        },
        legend: {
          position: 'top',
          horizontalAlign: 'left',
          offsetX: 40
        }
      },
      series: [{
        name: 'Seatime Completed',
        data: [100, 200, 20, 50]
      }, {
        name: 'Seatime Remaining',
        data: [180, 360, 180, 180]
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


</style>