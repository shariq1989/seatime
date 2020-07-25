<!--suppress JSUnusedGlobalSymbols, JSUnfilteredForInLoop -->
<template>
    <v-content>
        <v-row class="mb-6">
            <v-col cols="12" sm="2"></v-col>
            <v-col cols="12" sm="8">
                <v-card class="pa-2">
                    <v-data-table
                            :headers="table_headers"
                            :items="voyage_list"
                            :items-per-page="10"
                            class="elevation-1"
                    ></v-data-table>
                </v-card>
            </v-col>
            <v-col cols="12" sm="2"></v-col>
        </v-row>
    </v-content>
</template>

<script>
    import {getVoyages} from "../_services/seatime_entry.service";

    export default {
        data() {
            return {
                APIMethod: 'POST',
                voyage_list: null,
                table_headers: [
                    {text: 'Vessel', value: 'vessel'},
                    {text: 'Departure', value: 'depart_date'},
                    {text: 'Arrival', value: 'arrival_date'},
                    {text: 'Voyage', value: 'voyage_type'},
                    {text: 'Workday', value: 'workday_type'},
                    {text: 'Position', value: 'rank'},
                    {text: 'Rating', value: 'designation'}
                ]
            }
        },
        methods: {
            loadPage: function () {
                getVoyages().then((resp) => {
                    console.log(resp);
                    this.voyage_list = resp.data;
                })
            },
        },
        mounted() {
            this.loadPage();
        }
    }
</script>