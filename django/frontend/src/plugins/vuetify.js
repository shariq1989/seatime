import Vue from 'vue'
import Vuetify from 'vuetify/lib'

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify)

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: colors.indigo.darken1, // #3f51b5
                secondary: colors.grey.darken1, // #757575
                accent: colors.amber.darken2, // #ffc107
            },
        },
    },
})