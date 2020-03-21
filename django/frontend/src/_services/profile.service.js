import axios from 'axios';

export function getProfile() {
    let token = localStorage.getItem('user');
    axios({
        url: process.env.VUE_APP_API_URL + '/mariner-profiles/',
        method: 'GET',
        header: {'authorization': `Token ${token}`}
    })
        .then(response => {
            console.log(response);
        })
        .catch(err => {
            console.log(err);
        })
}
