<script lang="ts">
	import axios from 'axios';
	import {reactive, inject, ref} from 'vue';
	import {useRouter} from 'vue-router';
	import SpinningBar from '@/components/loading/SpinningBar.vue';

	export default {
		components: {
			SpinningBar
		},
		setup(){

			const router = useRouter();
			const loading = inject('loading');

			const state = reactive<Object>({
				email: null,
				password: null,
			})

			const error = ref<Array>([])

			async function login() {
				await axios.post('auth/jwt/create//', state)
				.then((resp) => {
					localStorage.setItem('access', resp.data.access)
					localStorage.setItem('refresh', resp.data.refresh)
					router.push({name: 'user-home'})
				})
				.catch((err) => {
					if(err.response ) {
						error.value = err.response.data
					}

				})
			}

			return {
				error,
				login,
				state,
				router,
				loading
			}
		}
	}
</script>

<template>
	<div class="">
		<div class="text-gray-600 fixed h-screen w-screen top-0 left-0 flex items-center p-6 lg:p-0 justify-center">
			<div class="lg:w-1/4 p-6 bg-white rounded-xl shadow-md border border-gray-200">
				{{loading}}
				<h1 class="text-xl font-semibold">
					Login
				</h1>
				<p class="mt-2 text-xs text-gray-500">
					Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
					tempor incididunt ut 
				</p>

				<div v-show="error?.detail" class="box-error">
					<span>
						{{error?.detail}}
					</span>
				</div>
				<div class="grid mt-4 gap-4">

					<div class="form-group">
						
						<label for="">
						email
						</label>
						<div class="relative w-full">
							<span class="iconify icon absolute top-3 left-2" data-icon="akar-icons:person"></span>
							<input v-model="state.email" type="text" placeholder="Enter your  email" :class="error?.email ? 'form-error' : 'form-control'" class=" pl-8 focus:border focus:border-green-700">
							<ul v-show="error?.email">
								<li v-for="message in error?.email" class="text-error">
									{{message}}
								</li>
							</ul>
						</div>
			    	</div>

		    		<div class="form-group">
						<label for="">
							password
						</label>

						<div class="relative w-full">
							<span class="iconify absolute top-3 left-2" data-icon="akar-icons:lock-on"></span>
							<input v-model="state.password" type="text" placeholder="Enter your password" :class="error?.password ? 'form-error' : 'form-control'" class="pl-8 focus:border focus:border-green-700">
							<ul v-show="error?.password">
								<li v-for="message in error?.password" class="text-error">
									{{message}}
								</li>
							</ul>
						</div>
					</div>		
				</div>

				<div class=" mt-4 items-center">
					<p class=" flex items-center">
						<span class="capitalize mr-1">
							doesnt have account ?
						</span>
						<button @click="router.push('/register')"  class="font-semibold capitalize">
							<span>
								Register
							</span>
						</button>
					</p>
				</div>
				<div class="mt-4 flex justify-end">
					<button @click="login" class="w-32 flex items-center justify-center btn btn-primary">
						<SpinningBar v-if="loading" custom-style="w-4 h-4">
							
						</SpinningBar>

						<div v-else>
							<span class="iconify icon" data-icon="ant-design:login-outlined"></span>
							<span>
								Login
							</span>
						</div>
					</button>
				</div>
			</div>
		</div>
	</div>			
</template>


<style lang="postcss" scoped>
	p{
		@apply text-gray-600 text-xs
	}
</style>