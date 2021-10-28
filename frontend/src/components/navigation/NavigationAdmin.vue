<script lang="ts">
	import {ref, onBeforeMount} from 'vue';
	import { useRouter, useRoute } from 'vue-router';
	export default {
		props: {
			customStyle: String
		},
		setup(props) {

			const router = useRouter()

			const route = useRoute()

			const menus = ref([
				{
					menu: 'Shop'
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


			const menus_admin = ref([
				{
					menu: 'Dashboard',
					icon: 'ion:rocket-outline',
					name: "admin-home"
				},
				{
					menu: 'Product',
					icon: 'ion:cube-outline',
					name: "admin-product",
				},
				{
					menu: 'Order',
					icon: 'ion:cart-outline',
					name: "admin-product"
				},
				{
					menu: 'Statistic',
					icon: 'ion:pie-chart',
					name: "admin-product"
				},
				{
					menu: 'Stock',
					icon:"ion:bag-handle-outline",
					name: "admin-product",
					dropdowns: [
						{
							menu_dropdown: "Stock"
						},
						{
							menu_dropdown: "Stock In"
						},
						{
							menu_dropdown: "Stock Out"
						},
					]
				},

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

			return {
				menus,
				selectedRoute,
				changeRoute,
				menus_admin,
				router,
				route,
				props
			}
		}
	}
</script>

<template>
	<div>
		<div id="admin-navigation" :class="props.customStyle" class="fixed lg:border-r-2 transition-all duration-300 lg:border-gray-100 h-screen bg-white  z-10 lg:p-0 lg:w-64">
		<div class="">
			<div class="flex items-center justify-center block p-2 lg:p-6 text-white font-semibold h-20 lg:text-xl text-green-700 flex items-center capitalize text-xs ">
				<span class="hidden lg:block">
					my plants
				</span>
			</div>
			<div class="mt-6">
				<ul class="">
					<li @click="changeRoute(index, item)" v-for="(item, index) in menus_admin" :class="[selectedRoute == index ? 'text-green-600 bg-green-100 bg-opacity-50 border-green-600 ' : 'text-gray-600 ']" class="py-2 mb-8 hover:bg-gray-100 hover:text-green-600 cursor-pointer px-3 ml-4 rounded-tl-full border-r-2   border-white rounded-bl-full transition-all duration-300 hover:bg-white ">
						<div class="flex  text-base items-center">
							<span class="iconify mr-4 text-xl" :data-icon="item.icon"></span>
							<span class=" ">
								{{item.menu}}
							</span>
						</div>
					</li>
				</ul>
			</div>
		</div>
	</div>
	</div>
</template>