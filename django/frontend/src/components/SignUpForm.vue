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
                                        label="Email"
                                        v-model="emailAddr"
                                        :rules="[v => !!v || 'This is a required field']"
                                        required
                                />
                                <v-text-field
                                        label="Username"
                                        v-model="username"
                                        :rules="[v => !!v || 'This is a required field']"
                                        required
                                />
                                <v-text-field
                                        id="password"
                                        label="Password"
                                        v-model="password"
                                        :rules="[v => !!v || 'This is a required field']"
                                        required
                                />
                                <v-text-field
                                        id="passwordConfirm"
                                        label="Confirm Password"
                                        v-model="passwordConfirm"
                                        :rules="[v => !!v || 'This is a required field']"
                                        required
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
    import {userService} from "../_services/user.service";

    export default {
        props: {
            source: String,
        },
        data() {
            return {
                emailAddr: '',
                username: '',
                password: '',
                passwordConfirm: '',
                submitted: false
            }
        },
        methods: {
            handleSubmit() {
                this.submitted = true;
                const {emailAddr, username, password, passwordConfirm} = this;
                if (emailAddr && username && password && passwordConfirm) {
                    userService.func_register(emailAddr, username, password, passwordConfirm)
                }
            }
        }
    }
</script>
