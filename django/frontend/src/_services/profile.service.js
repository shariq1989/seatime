import axios from 'axios';

export function getProfile() {
    let promise = new Promise((resolve, reject) => {
        axios({url: process.env.VUE_APP_API_URL + '/mariner-profiles/', data: {}, method: 'POST'})
            .then(response => {
                console.log(response);
                resolve(response)
            })
            .catch(err => {
                console.log(reject);
                reject(err)
            })
    });
}