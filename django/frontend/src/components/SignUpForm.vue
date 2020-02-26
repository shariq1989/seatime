<template>
    <v-app id="inspire">
        <v-content>
            <v-row
                    align="center"
                    justify="center"
            >
                <v-col
                        cols="12"
                        sm="8"
                        md="4"
                >
                    <v-card class="elevation-12">
                        <v-toolbar
                                color="primary"
                                dark
                                flat
                        >
                            <v-toolbar-title>Create an account</v-toolbar-title>
                            <v-spacer/>
                        </v-toolbar>
                        <v-card-text>
                            <v-form>
                                <v-text-field
                                        label="First Name"
                                        name="firstName"
                                        type="text"
                                />
                                <v-text-field
                                        label="Last Name"
                                        name="lastName"
                                        type="text"
                                />
                                <v-text-field
                                        label="Email"
                                        name="emailAddr"
                                        type="email"
                                />
                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        type="password"
                                />
                                <v-text-field
                                        id="passwordConfirm"
                                        label="Confirm Password"
                                        name="passwordConfirm"
                                        type="password"
                                />
                            </v-form>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer/>
                            <v-btn color="primary">Create Account</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-col>
            </v-row>
        </v-content>
    </v-app>
</template>

<script>
    export default {
        props: {
            source: String,
        },
    }
</script>
