import axios from 'axios';
import router from "../router";

export let funcLogin = user => new Promise((resolve, reject) => {
    axios({url: process.env.VUE_APP_API_URL + '/authenticate/', data: user, method: 'POST'})
        .then(response => {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(response.data['token']));
            localStorage.setItem('id', JSON.stringify(response.data['id']));
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
});

export let funcRegister = registrationFields => new Promise((resolve, reject) => {
    axios({url: process.env.VUE_APP_API_URL + '/rest-auth/registration/', data: registrationFields, method: 'POST'})
        .then(response => {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            console.log(response);
            localStorage.setItem('user', JSON.stringify(response.data['token']));
            localStorage.setItem('id', JSON.stringify(response.data['id']));
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
});

export function funcLogout() {
    // remove user from local storage to log user out
    localStorage.clear();
    router.push('/login');
}
