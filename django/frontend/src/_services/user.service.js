export const userService = {
    func_logout,
    func_register
};
import axios from 'axios';

// Exported in a shared file
export let funcLogin = user => new Promise((resolve, reject) => {
    axios({url: 'auth', data: user, method: 'POST'})
        .then(response => {
            if (response.data.key) {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                localStorage.setItem('user', JSON.stringify(response.data.key));
            }
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
});

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
