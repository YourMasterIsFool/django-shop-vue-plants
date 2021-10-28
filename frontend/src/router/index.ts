import {createRouter, createWebHistory} from 'vue-router'

const routes = [

	{
		path: '/login',
		name: 'login',
		component:() => import('@/views/Login.vue')
	},
	{
		path: '/register',
		name: 'register',
		component:() => import('@/views/Register.vue')
	},
	{
		path: '/',
		name: 'user',
		component: () =>  import('@/views/user/base.vue'),
		
		children: [

			{
				path: "",
				name: 'user-home',
				component: () => import('@/views/user/home/index.vue')
			},

			{
				path: "cart",
				name: 'user-cart',
				meta: {
					requiresAuth: true
				},
				component: () => import('@/views/user/cart/index.vue')
			},
		]
	},
	{
		path: '/admin',
		name: 'admin',
		meta: {
			requiresAuth: true
		},
		component: () =>  import('@/views/admin/base.vue'),
		children: [

			{
				path: "",
				name: 'admin-home',
				component: () => import('@/views/admin/home/index.vue')
			},

			{
				path: "/product",
				name: 'admin-product',
				component: () => import('@/views/admin/product/index.vue')
			},

			{
				path: "/product/create",
				name: 'admin-product-create',
				component: () => import('@/views/admin/product/create.vue')
			},

			{
				path: '/user/profile/',
				name: 'admin-profile',
				component: () => import('@/views/admin/profile/index.vue'),
				children: [

					{
						path: '',
						name: 'admin-profile-settings',
						component: () => import('@/views/admin/profile/components/AccountSetting.vue')
					},

					{
						path: 'address',
						name: 'admin-profile-address',
						component: () => import('@/views/admin/profile/components/AddressSetting.vue')
					}
				]
			}
		]
	}

]

const router = createRouter({
	history: createWebHistory(),
	routes
})


router.beforeEach((to, from, next) =>{
	if(to.matched.some(record => record.meta.requiresAuth)) {
		if(!localStorage.getItem('access')){
			return next({path: '/login'})
		}
		else {
			next()
		}
	}
	else {
		next()
	}
})


export default router