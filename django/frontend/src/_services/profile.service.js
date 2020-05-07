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
    callAPI(input[0], input[1], input[2], endpoint);
});

export let updateDocuments = input => new Promise((resolve, reject) => {
    let apiEndpoint = '/mariner-documents/';
    callAPI(input[0], input[1], input[2], endpoint);
});


export let getDocuments = () => new Promise((resolve, reject) => {
    let token = JSON.parse(localStorage.getItem('user'));
    axios({
        url: process.env.VUE_APP_API_URL + '/mariner-documents/',
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

function callAPI(method, object, id, endpoint) {
    let authToken = JSON.parse(localStorage.getItem('user'));
    if (method === 'PUT') {
        endpoint += id + '/';
        // id is only needed for PUT because it doesnt exist yet for POST
        object.id = id;
    }
    axios({
        url: process.env.VUE_APP_API_URL + endpoint,
        data: object,
        method: method,
        headers: {"Authorization": "Token " + authToken}
    })
        .then(response => {
            resolve(response)
        })
        .catch(err => {
            reject(err)
        })
}