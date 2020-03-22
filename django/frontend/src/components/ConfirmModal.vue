<template v-slot:append>
    <template>
        <div class="text-left">
            <v-dialog v-model="confirmDialog" width="500">
                <v-card>
                    <v-card-title class="headline grey lighten-2" primary-title>
                        Confirm Action
                    </v-card-title>
                    <v-card-text>
                        Are you sure you want to proceed?
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="primary" text @click="confirmDialog = false">
                            Cancel
                        </v-btn>
                        <v-btn color="red darken-1" text @click="confirmDialog = false">
                            Confirm
                        </v-btn>
                    </v-card-actions>
                </v-card>

                <template v-slot:activator="{ on }">
                    <div class="pa-2" v-on="on">
                        <v-list-item-icon>
                            <v-icon>mdi-logout</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                            <v-list-item-title>Logout</v-list-item-title>
                        </v-list-item-content>
                    </div>
                </template>
            </v-dialog>
        </div>
    </template>
</template>
