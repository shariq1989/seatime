import axios from 'axios';

export function getProfile() {
    let userToken = localStorage.getItem('user');
    let headers = {"Token: ": userToken};
    axios({url: process.env.VUE_APP_API_URL + '/mariner-profiles/', method: 'GET', header: headers})
        .then(response => {
            console.log(response);
        })
        .catch(err => {
            console.log(err);
        })
}
