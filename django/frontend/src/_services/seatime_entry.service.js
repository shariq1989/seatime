import axios from 'axios';

function getRequest(endpoint) {
    let token = JSON.parse(localStorage.getItem('user'));
    return axios({
        url: process.env.VUE_APP_API_URL + endpoint,
        method: 'GET',
        headers: {"Authorization": "Token " + token}
    });
}

export let getSeatimeEntries = () => new Promise((resolve, reject) => {
    getRequest('/voyages/').then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    });
});

export let getVessels = () => new Promise((resolve, reject) => {
    getRequest('/vessels/').then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    });
});

export let getStaffPositions = () => new Promise((resolve, reject) => {
    getRequest('/ranks/').then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    });
});

export let getVoyageTypes = () => new Promise((resolve, reject) => {
    getRequest('/voyage-types/').then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    });
});

export let getWorkdayType = () => new Promise((resolve, reject) => {
    getRequest('/workday-types/').then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
        reject(err)
    });
});

export let updateSeatimeEntries = input => new Promise((resolve, reject) => {
    let apiEndpoint = '/voyages/';
    callAPI(input[0], input[1], input[2], apiEndpoint).then(response => {
        resolve(response)
    }).catch(err => {
        console.log(err);
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