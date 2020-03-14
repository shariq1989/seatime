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
                            <v-toolbar-title>Login</v-toolbar-title>
                            <v-spacer/>
                        </v-toolbar>
                        <v-form @submit.prevent="handleSubmit">
                            <v-card-text>
                                <v-text-field
                                        label="Login"
                                        name="login"
                                        prepend-icon="person"
                                        type="text"
                                        v-model="username"
                                />

                                <v-text-field
                                        id="password"
                                        label="Password"
                                        name="password"
                                        prepend-icon="lock"
                                        type="password"
                                        v-model="password"
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
    import axios from 'axios';

    export default {
        props: {
            source: String,
        },
        data() {
            return {
                username: '',
                password: '',
                submitted: false
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
//                    userService.func_login({username, password})
                    axios.post(process.env.VUE_APP_API_URL + '/rest-auth/login/', {
                        username: username,
                        password: password
                    }).then(function (response) {
                        console.log(response);
                    }).catch(function (error) {
                        console.log(error);
                    });
                }
            }
        }
    };
</script>