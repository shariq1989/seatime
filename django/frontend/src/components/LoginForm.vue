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
                            <v-alert type="error" v-if="displayErrorMessage">
                                {{errorMessage}}
                            </v-alert>
                            <v-toolbar-title>Login</v-toolbar-title>
                            <v-spacer/>
                        </v-toolbar>
                        <v-form @submit.prevent="handleSubmit">
                            <v-card-text>
                                <v-text-field
                                        label="Username"
                                        name="login"
                                        prepend-icon="person"
                                        type="text"
                                        v-model="username"
                                        :rules="[v => !!v || 'Username is required']"
                                        required
                                />

                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
                                        :rules="[v => !!v || 'Password is required']"
                                        required
                                />
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer/>
                                <v-btn color="primary" type="submit">Login</v-btn>
                            </v-card-actions>
                        </v-form>
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
                username: '',
                password: '',
                submitted: false,
                displayErrorMessage: false,
                errorMessage: ''
            }
        },
        created() {
            // reset login status
            userService.func_logout();
        },
        methods: {
            handleSubmit() {
                this.submitted = true;
                const {username, password} = this;
                if (username && password) {
                    var result = userService.func_login(username, password);
                    if (result) {
                        this.displayErrorMessage = true;
                        this.errorMessage = result;
                    }
                }
            }
        }
    };
</script>