import axios from 'axios';

export let getSeatimeEntries = () => new Promise((resolve, reject) => {
    let token = JSON.parse(localStorage.getItem('user'));
    axios({
        url: process.env.VUE_APP_API_URL + '/voyages/',
        method: 'GET',
        headers: {"Authorization": "Token " + token}
    }).then(response => {
        console.log(response);
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    })
});

export let updateSeatimeEntries = input => new Promise((resolve, reject) => {
    let apiEndpoint = '/voyages/';
    callAPI(input[0], input[1], input[2], apiEndpoint).then(response => {
        resolve(response)
    }).catch(err => {
        reject(err)
    });
});

function callAPI(method, object, id, endpoint) {
    let authToken = JSON.parse(localStorage.getItem('user'));
    if (method === 'PUT') {
        endpoint += id + '/';
        // id is only needed for PUT because it doesnt exist yet for POST
        object.id = id;
    }
    return axios({
        url: process.env.VUE_APP_API_URL + endpoint,
        data: object,
        method: method,
        headers: {"Authorization": "Token " + authToken}
    });
}