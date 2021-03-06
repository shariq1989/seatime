import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    }, {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login.vue')
    }, {
        path: '/signup',
        name: 'SignUp',
        component: () => import('../views/SignUp')
    }, {
        path: '/profile',
        name: 'Profile',
        component: () => import('../views/Profile')
    }, {
        path: '/document',
        name: 'Document',
        component: () => import('../views/Document')
    }, {
        path: '/seatime_entry',
        name: 'SeatimeEntry',
        component: () => import('../views/SeatimeEntry')
    }, {
        path: '/checklist',
        name: 'Checklist',
        component: () => import('../views/Checklist')
    }
];

const router = new VueRouter({
    routes
});

router.beforeEach((to, from, next) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const publicPages = ['/login', '/signup'];
    const authRequired = !publicPages.includes(to.path);
    const loggedIn = localStorage.getItem('user');

    if (authRequired && !loggedIn) {
        return next('/login');
    }

    next();
});

export default router
