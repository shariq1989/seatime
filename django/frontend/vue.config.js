module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    mode: 'development',
    externals: {
        // global app config object
        config: JSON.stringify({
            apiUrl: 'http://localhost:8000'
        })
    }
};