<script lang="ts">
	import {defineAsyncComponent, onMounted, ref, onBeforeMount, computed} from 'vue'
	import {useRoute, useRouter} from 'vue-router'
	import { width } from '@/mixins/screen'
	import ProductService from '@/models/product/service'
	import User from '@/models/user/user_model'



	const Navigation = defineAsyncComponent({
		loader: () =>import('@/components/navigation/NavigationAdmin.vue')
	})

	const Sidebar = defineAsyncComponent({
		loader: () => import('@/components/sidebar/Sidebar.vue')
	})
	
	const NavigationTop = defineAsyncComponent({
		loader: () =>import('./NavigationTop.vue')
	})


	export default{
		components: {
			Navigation,
			Sidebar,
			NavigationTop
		},

		setup(){
			const route = useRoute();

			const router = useRouter();

			const showSidebar = ref(false);

			const product_count = ref(0)

			onMounted(() =>  {
				ProductService
				.get_count()
				.then((resp) => {
					console.log(resp.data)
					product_count.value = resp.data
				})
			})

			const notifications = ref(false);

			const showMobileNav = ref(false);

			const sidebarSize = computed(() =>{
			
					let size = 350

					if(width.value < 1028) {
					 return	 width
					}
					
					return size
				
			})


			return {
				product_count,
				route,
				showSidebar,
				sidebarSize,
				notifications,
				showMobileNav,
				width,
				router,
				User
			}

		}
	}
</script>

<template>

	<div  :class="[showSidebar ? 'overflow-y-hidden px-4 lg:px-10' : 'overflow-y-']" class="flex relative overflow-x-hidden ">


		<Navigation class="transition-all   duration-300" :custom-style="showMobileNav ? 'w-48 transition-all fixed top-0 left-0 duration-300' :'w-0 overflow-hidden  transition-all duration-300'"></Navigation>

		<button @click="showMobileNav = false" v-show="showMobileNav" class="fixed top-7 z-40 left-16">
			<span class="iconify" data-icon="mdi:window-close"></span>
		</button>


		<div :class="[showSidebar && !route.path.includes('/user/profile/')   ? 'lg:w-7/12' : 'w-full']" class="transition-all duration-300 lg:ml-64   w-full">
			<div id="navigation" class="h-20 ">
				<div class="flex h-full lg:px-6 justify-between items-center">

					<div class="flex items-center">
						<button @click="showMobileNav = true" class="mr-2 block lg:hidden">
							<span class="iconify" data-icon="mdi:menu"></span>
						</button>
						<span class="text-xl text-green-800">
							<span class="iconify" data-icon="mdi:store"></span>
						</span>

					</div>
					<div class="text-gray-400 flex items-center">
						

						<div class="relative">
							<div  v-show="notifications" class="absolute bg-white z-20 shadow-md top-6 rounded-xl p-4 text-sm right-0 h-96  w-72 ">
								Notifications
							</div>

							<button @click="notifications = !notifications" class="mr-2 relative">
								<span class="iconify" data-icon="mdi:bell-outline"></span>
							</button>

						

						</div>

							<button @click="showSidebar = true" v-show="!showSidebar && !route.path.includes('/user/profile/') ">
							<img :src="User?.user.profile.photo" class="w-12 object-cover mr-2 h-12 rounded-full bg-gray-200" />
							</button>

					</div>

					
					
				</div>
			</div>
			<div class="p-2 lg:p-6 lg:mr-4">
		
				<router-view></router-view>
			</div>
		</div>
		<Sidebar v-show="!route.path.includes('/user/profile/')" class=" lg:overflow-y-hidden overflow-y-auto top-0 right-0 fixed h-screen bg-gray-50 text-gray-600 lg:border-l transition-all mr-0 duration-300 lg:border-gray-100 " :class="[showSidebar ? 'w-screen h-screen lg:w-3/12 p-4' : 'w-0 overflow-hidden']">
			<template v-slot:header>
				<div class="flex items-center justify-between">
					<div class="flex items-center">
						<img :src="User?.user.profile.photo" class="w-12 object-cover mr-2 h-12 rounded-full 	bg-gray-200" />
						
						
						<div>
							<div class=" font-semibold text-xs">
								Verrandy Bagus
							</div>
							<div class="text-gray-500 text-xs">
								Admin
							</div>
						</div>
					</div>
					
					<div  class="flex items-center justify-center">
						<button @click="router.push({name: 'admin-profile-settings'})" class="w-8 h-8 mr-4 flex items-center justify-center text-gray-500">
							<span class="iconify" data-icon="mdi:cog-outline"></span>
						</button>


						<!-- button for close sidebar -->

						<button @click="showSidebar = false" class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center ">
							<span class="iconify" data-icon="mdi:window-close"></span>

						</button>
					</div>
				</div>
				

				<div class="mt-6">
			 		<div class="grid grid-cols-2 gap-x-4">
			 			<div class="bg-white rounded-2xl p-2 flex items-center">
			 				<div class="w-10 mr-2 rounded-full h-10 bg-blue-100 flex items-center justify-center">
			 					<span class="iconify text-xl" data-icon="mdi:cube-outline"></span>
			 				</div>
			 				<div class="flex text-xs flex-col">
			 					<span class="font-bold text-sm text-green-600">
			 						{{product_count}}
			 					</span>
			 					<span class="text-xs text-gray-400">
			 						Product
			 					</span>
			 				</div>
			 			</div>

			 			<div class="bg-white rounded-2xl p-2 flex items-center">
			 				<div class="w-10 mr-2 rounded-full h-10 bg-blue-100 flex items-center justify-center">
			 					<span class="iconify text-xl" data-icon="akar-icons:cart"></span>
			 				</div>
			 				<div class="flex text-xs flex-col">
			 					<span class=" text-sm font-bold text-base text-green-600">
			 						2000
			 					</span>
			 					<span class="text-xs text-gray-400">
			 						Order
			 					</span>
			 				</div>
			 			</div>
			 		</div>
			 	</div>


				<div class="p-5 mt-6 bg-white rounded-xl ">
					 <div class="header flex items-center justify-between">
					 	<h1 class="text-green-700 text-sm font-semibold ">
					 		Sales analystic
					 	</h1>

					 	<button class="text-gray-600">
					 		<span class="iconify" data-icon="mdi:filter-variant"></span>
					 	</button>
					 </div>
					 <div class="body mt-4">
					 	
					 	<div class="lg:grid lg:grid-cols-2 flex flex-col-reverse">
					 		<div class="grid grid-cols-3 lg:block">
					 			<div class="text-xs mb-4">
							 		<div class="text-gray-400 mb-1">
							 			Online
							 		</div>
							 		<div class="
							 		font-bold text-green-600">
							 		$2,135	
							 		</div>
							 	</div>
							 	<div class="text-xs mb-4">
							 		<div class="text-gray-400 mb-1">
							 			Offline
							 		</div>
							 		<div class="
							 		font-bold text-green-600">
							 		$2,135	
							 		</div>
							 	</div>
							 	<div class="text-xs ">
							 		<div class="text-gray-400 mb-1">
							 			Marketing
							 		</div>
							 		<div class="
							 		font-bold text-green-600">
							 		$2,135	
							 		</div>
							 	</div>
					 		</div>
					 		<div class="mb-4 flex items-center justify-center">
					 			<div class="bg-gray-600 w-32 h-32 rounded-full">
					 				
					 			</div>
					 		</div>
					 	</div>
					 </div>
				</div>
				<div class="mt-6 text-xs">
					<div class="flex items-center justify-between">
						<span class="capitalize text-sm  font-bold">
							recent orders
						</span>
						<button class="underline capitalize ">
							see all
						</button>
					</div>
					<div class="bg-white rounded-xl p-4">
						<ul>
							<li v-for="i in 3" class="pb-2">
								<div class="flex  justify-between items-center">
									<div class="flex items-center">
										<div class="h-12 mr-4 w-12 rounded-lg bg-gray-200">
											
										</div>
										<div class="flex flex-col">
											<span class="mb-1 font-bold">
												Product
											</span>
											<span class="">
												1 minutes ago
											</span>
										</div>
									</div>
									<span class="text-green-600 font-bold">
										+ 29914
									</span>
								</div>
							</li>
						</ul>
					</div>
				</div>
			</template>
		</Sidebar>
	</div>
</template>