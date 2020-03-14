export const userService = {
    func_login,
    func_logout,
};

function func_login(username, password) {
    axios.post(process.env.VUE_APP_API_URL + '/rest-auth/login/', {
        username: username,
        password: password
    }).then(function (response) {
        if (response.data.key) {
            // store user details and jwt token in local storage to keep user logged in between page refreshes
            localStorage.setItem('user', JSON.stringify(user));
        }
    }).catch(function (error) {
        console.log(error);
    });
}

function func_logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}

function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        if (!response.ok) {
            if (response.status === 401) {
                // auto logout if 401 response returned from api
                func_logout();
                location.reload();
            }

            const error = (data && data.message) || response.statusText;
            return Promise.reject(error);
        }

        return data;
    });
}