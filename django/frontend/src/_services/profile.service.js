import axios from 'axios';

export let getProfile = () => new Promise((resolve, reject) => {
    let token = JSON.parse(localStorage.getItem('user'));
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

