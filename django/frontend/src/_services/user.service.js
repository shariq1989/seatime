export const userService = {
    func_login,
    func_logout,
    func_register
};
import axios from 'axios';
import router from '../router/index.js'

function func_login(username, password) {
    axios.post(process.env.VUE_APP_API_URL + '/rest-auth/login/', {
        username: username,
        password: password
    }).then(function (response) {
        if (response.data.key) {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(response.data.key));
            router.push('/');
        }
    }).catch(function (error) {
        console.log(error);
        if (error.response.status === 400) {
            return 'Incorrect username or password. Please try again';
        } else {
            return 'Unexpected error occured';
        }

    });
}

function func_register(emailAddr, username, password, passwordConfirm) {
    axios.post(process.env.VUE_APP_API_URL + '/rest-auth/registration/', {
        username: username,
        password1: password,
        password2: passwordConfirm,
        email: emailAddr
    }).then(function (response) {
        console.log(response);
    }).catch(function (error) {
        console.log(error);
    });
}

function func_logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}
