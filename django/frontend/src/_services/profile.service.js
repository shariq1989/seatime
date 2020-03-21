import axios from 'axios';

export let getProfile = function () {
    let token = JSON.parse(localStorage.getItem('user'));
    new Promise((resolve, reject) => {
        axios({
            url: process.env.VUE_APP_API_URL + '/mariner-profiles/',
            method: 'GET',
            headers: {"Authorization": "Token " + token}
        })
            .then(response => {
                resolve(response)
            })
            .catch(err => {
                reject(err)
            })
    });
};
