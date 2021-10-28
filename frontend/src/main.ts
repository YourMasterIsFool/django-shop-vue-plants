import { createApp, provide, ref } from 'vue'
import App from './App.vue'
import './assets/css/tailwind.css'
import axios, { Axios } from 'axios'
import { useRoute, useRouter } from 'vue-router'
import moment from 'moment'
import router from './router'
import {ref} from 'vue';
import UserService from '@/models/user/user_service'
import User from '@/models/user/user_model'


axios.defaults.baseURL = "http://localhost:8000/api/"


const loading = ref(false)

axios.interceptors.request.use(function(config) {
	
	loading.value = true
	if(localStorage.getItem('access')) {
		const key = localStorage.getItem('access')

		config.headers = {
			'Authorization': `Bearer ${key}`,
			// 'Accept': 'application/json',
		}
	}

	else {
		config.headers = {
			'Authorization': null
		}
	}
	return config
})



if(User.user  == null) {
	UserService.get_profile()
	.then((resp) => {
		console.log(resp)
	})
}


axios.interceptors.response.use((response) => {
	loading.value = false
	return response
},

async function (error) {

	if(error.response.status == 401) {

		router.push('/login')
		loading.value = false
	}

	loading.value = false
	return Promise.reject(error)
}
)

loading.value = false



// createApp(App).mount('#app')
const app = createApp(App)
app.provide('moment', moment)
app.provide('loading', loading.value)
app.use(router)
app.provide('axios', axios)

app.mount("#app")