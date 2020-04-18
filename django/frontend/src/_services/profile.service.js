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

export let updateProfile = input => new Promise((resolve, reject) => {
    let token = JSON.parse(localStorage.getItem('user'));
    let apiEndpoint = '/mariner-profiles/';
    if (input[0] === 'PUT') {
        apiEndpoint += input[2] + '/'
    }
    console.log(apiEndpoint);
    axios({
        url: process.env.VUE_APP_API_URL + apiEndpoint,
        data: input[1],
        method: input[0],
        headers: {"Authorization": "Token " + token}
    })
        .then(response => {
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
});

