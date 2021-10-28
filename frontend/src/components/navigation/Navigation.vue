<script lang="ts">
	import {ref, onBeforeMount} from 'vue';
	import { useRouter, useRoute } from 'vue-router';
	export default {

		setup() {

			const router = useRouter()

			const route = useRoute()

			const menus = ref([
				{
					menu: 'Shop',
					name: 'user-home'
				},
				{
					menu: 'plant care'
				},
				{
					menu: 'workshops'
				},
				{
					menu: 'blogs'
				}
			])



			const selectedRoute = ref(localStorage.getItem('selectedRoute'))
				

			onBeforeMount(() => {
				selectedRoute.value = localStorage.getItem('selectedRoute')	
				console.log(selectedRoute.value)
			})
			function changeRoute(index, item) {
				localStorage.setItem('selectedRoute', index),
				selectedRoute.value = index

				router.push({name: item.name})
			}

			function logout(){
				localStorage.removeItem('access')
				router.push('/login')
			}

			return {
				menus,
				logout,
				selectedRoute,
				changeRoute,
				router,
				route
			}
		}
	}
</script>

<template>
	<div  id="user"  class="desktop h-full">
		<div class="w-full pt-2 px-12 h-full flex justify-between items-center">
			<div @click="router.push({name: 'user-home'})" style="width: 250px;" class=" cursor-pointer pb-3 text-2xl capitalize font-semibold text-green-700">
				my plants
			</div>
			<ul class="w-4/5 items-center flex">
				<li @click="changeRoute(index)"  
				v-for="(item, index) in menus" class="transition-all duration-300 pb-3  cursor-pointer capitalize text-lg  flex justify-center px-6">
					<span>
						{{item.menu}}
					</span>
				</li>



			</ul>
			<ul class="pb-3 flex  items-center text-gray-500">
				<li @click="router.push({name: 'user-cart'})" class="pr-6  cursor-pointer">
					<span class="material-icons ">
						shopping_bag
					</span>
				</li>
				<li class="pr-6 cursor-pointer">
					<span class="material-icons">
						favorite_border
					</span>
				</li>
				<li class="pr-6 pb-1 cursor-pointer">
					<div class="w-8 h-8 pb  rounded-full bg-gray-500">
						
					</div>
				</li>

				<li @click="logout" class="pr-6 pb-1 cursor-pointer">
					logout				
				</li>
			</ul>
		</div>
		<div class="border-b border-gray-100">
			
		</div>
	</div>

	
</template>
