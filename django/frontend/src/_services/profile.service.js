import axios from 'axios';

export let getProfile = new Promise((resolve, reject) => {
    let userToken = localStorage.getItem('user');
    let headers = {"Token: ": userToken};
    axios({url: process.env.VUE_APP_API_URL + '/mariner-profiles/', method: 'GET', header: headers})
        .then(response => {
            console.log(response);
            resolve(response)
        })
        .catch(err => {
            console.log(reject);
            reject(err)
        })
});