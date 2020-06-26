<template>
    <v-app id="inspire" style="background-color: #bbdefb;">
        <v-content>
            <v-container fill-height fluid>
                <v-row align="center">
                    <v-row>
                        <v-col
                                cols="12"
                                sm="2"
                        >
                        </v-col>
                        <v-col
                                cols="12"
                                sm="5"
                        >
                            <h1>Welcome to SeaTime.</h1>
                            <p>A toolkit that allows mariners to manage various aspects of work life</p>
                            <ul>
                                <li>Mariner Profile</li>
                                <li>Documents</li>
                                <li>Voyages</li>
                                <li>...etc...</li>
                            </ul>
                            <v-img src="../assets/stock/tomas-williams-p-_RJY6hN3E-unsplash.jpg" aspect-ratio="1.7"
                                   contain></v-img>
                        </v-col>
                        <v-col
                                cols="12"
                                sm="3"
                        >
                            <v-card class="elevation-12">
                                <v-form @submit.prevent="handleSubmit">
                                    <div class="pa-2">
                                        <v-alert type="error" v-if="displayErrorMessage">
                                            <span class="text-left" v-html="errorMessage"></span>
                                        </v-alert>
                                    </div>
                                    <v-card-title>
                                        Lets Set Sail
                                    </v-card-title>
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
                                        <v-btn to="/signup">Create an account</v-btn>
                                        <v-spacer/>
                                        <v-btn type="submit">Login</v-btn>
                                    </v-card-actions>
                                </v-form>
                            </v-card>
                        </v-col>
                        <v-col
                                cols="12"
                                sm="2"
                        >
                        </v-col>
                    </v-row>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import router from "../router";
    import {funcLogin, funcLogout} from "../_services/user.service";

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
            funcLogout();
        },
        methods: {
            handleSubmit() {
                this.submitted = true;
                const {username, password} = this;
                if (username && password) {
                    funcLogin({username, password}).then(() => {
                        router.push('/');
                    }).catch((err) => {
                        console.log(err);
                        this.displayErrorMessage = true;
                        this.errorMessage = 'Invalid username or password. Please try again.';
                    })
                }
            },
        }
    };
</script>
<style>
    body {
        background-image: url('../assets/stock/ariel.jpg');
    }
</style>