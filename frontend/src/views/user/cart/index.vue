<script lang="ts">
	import {onMounted} from 'vue'
	import CartService from '@/models/cart/cart_service'
	import Carts from './components/index/Carts.vue'

	export default {
		components:{
			Carts
		},
		setup() {
			onMounted(async () => {
				await CartService.get_cart()
				.then((resp) => {
					console.log(resp)
				})
			})
		}
	}
</script>

<template>
	<div class="lg:p-12">
		<div class="text-gray-700 grid grid-cols-4 gap-4">
			<div class="lg:col-span-3">
				
				<div class="flex items-center justify-between">
							<h1 class="lg:text-2xl capitalize text-gray-700 font-semibold">
					Shopping Cart
					</h1>
					<h1 class="lg:text-lg capitalize text-gray-700 font-semibold">
					3 Items
					</h1>



				</div>

				

				<div class="bg-white lg:p-8 rounded-xl mt-4 border border-gray-100">
					<div class="flex text-xs capitalize items-center">
						<input class="mr-10 " type="checkbox">
						<h1 class="text-normal">
							checkout all 
						</h1>
						
					</div>

					<Carts></Carts>
				</div>	

			</div>
			<div class="lg:col-span-1">
				
			</div>
		</div>
	</div>
</template>

<style lang="scss">
	table{
		td {
			padding-bottom: 1.5rem;
		}
	}
</style>