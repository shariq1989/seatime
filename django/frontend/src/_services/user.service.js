import axios from 'axios';
import router from "../router";

export let funcLogin = user => new Promise((resolve, reject) => {
    axios({url: process.env.VUE_APP_API_URL + '/rest-auth/login/', data: user, method: 'POST'})
        .then(response => {
            if (response.data.key) {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                localStorage.setItem('user', JSON.stringify(response.data.key));
                axios({url: process.env.VUE_APP_API_URL + '/current-mariner/', method: 'POST'}).then(response => {
                    console.log(response);
                    localStorage.setItem('userId', JSON.stringify(response.data));
                }).catch(error => {
                    console.log(error);
                });
            }
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
});

export let funcRegister = registrationFields => new Promise((resolve, reject) => {
    axios({url: process.env.VUE_APP_API_URL + '/rest-auth/registration/', data: registrationFields, method: 'POST'})
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

export function funcLogout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
    router.push('/login');
}
