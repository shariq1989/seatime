export const userService = {
    func_login,
    func_logout,
};
import axios from 'axios';

function func_login(username, password) {
    axios.post(process.env.VUE_APP_API_URL + '/rest-auth/login/', {
        username: username,
        password: password
    }).then(function (response) {
        if (response.data.key) {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(response.data.key));
            this.router.push('/');
        }
    }).catch(function (error) {
        console.log(error);
    });
}

function func_logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}
