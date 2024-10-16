import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig ({
    router: {
        options: {
            strict: true,
        },
        // extendRoutes(routes, resolve) {
        //     routes.push({
        //         name: 'board-list',
        //         path: '/board/list',
        //         component: resolve(__dirname, 'pages/list.vue')
        //     })
        // }
    }
})