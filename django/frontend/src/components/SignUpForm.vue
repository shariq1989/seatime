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
                        <v-form @submit.prevent="handleSubmit">
                            <v-toolbar
                                    color="primary"
                                    dark
                                    flat
                            >
                                <v-toolbar-title>Create an account</v-toolbar-title>
                                <v-spacer/>
                            </v-toolbar>
                            <v-card-text>
                                <div class="pa-2">
                                    <v-alert type="error" v-if="displayErrorMessage">
                                        {{errorMessage}}
                                    </v-alert>
                                </div>
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
                                        type="password"
                                        :rules="[v => !!v || 'This is a required field', passwordChecks]"
                                        required
                                />
                                <v-text-field
                                        id="passwordConfirm"
                                        label="Confirm Password"
                                        v-model="passwordConfirm"
                                        type="password"
                                        :rules="[v => !!v || 'This is a required field', passwordConfirmCheck]"
                                        required
                                />
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer/>
                                <v-btn color="primary" type="submit" :disabled="submitDisabled">Create Account</v-btn>
                            </v-card-actions>
                        </v-form>
                    </v-card>
                </v-col>
            </v-row>
        </v-content>
    </v-app>
</template>

<script>
    import router from "../router";
    import {funcRegister} from "../_services/user.service";

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
                submitted: false,
                displayErrorMessage: false,
                errorMessage: '',
                submitDisabled: true
            }
        },
        methods: {
            passwordChecks(value) {
                if (value.length < 8) {
                    this.submitDisabled = true;
                    return "Passwords must be at least 8 characters";
                } else if (this.passwordConfirm.length > 1 && value !== this.passwordConfirm && this.submitDisabled === false) {
                    this.submitDisabled = true;
                    return "Confirm Password and Password fields do not match";
                } else {
                    this.submitDisabled = false;
                    return true;
                }
            },
            passwordConfirmCheck(value) {
                if (value !== this.password) {
                    this.submitDisabled = true;
                    return "Confirm Password and Password fields do not match";
                } else {
                    this.submitDisabled = false;
                    return true;
                }
            },
            handleSubmit() {
                this.submitted = true;
                const {username, password, passwordConfirm, emailAddr} = this;
                if (emailAddr && username && password && passwordConfirm) {
                    funcRegister({
                        username,
                        password1: password,
                        password2: passwordConfirm,
                        email: emailAddr
                    }).then(() => {
                        router.push('/');
                    }).catch((err) => {
                        console.log(err.response.data);
                        this.displayErrorMessage = true;
                        this.errorMessage = 'Error registering user';
                        if (err.response.data) {
                            for (const field in err.response.data) {
                                for (const error of err.response.data[field]) {
                                    this.errorMessage += '<br/>';
                                    this.errorMessage += error;
                                }
                            }
                        }
                    })
                }
            }
        }
    }
</script>
