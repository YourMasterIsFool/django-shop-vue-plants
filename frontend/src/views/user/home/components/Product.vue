<script lang="ts">
	import { toRefs, reactive } from 'vue'
	import {useRouter} from 'vue-router'
	import CartService from '@/models/cart/cart_service'

	export default {
		props: {
			product: {
				type: Object,

			}
		},

		setup(props){
			const {product} = toRefs(props)
			const router = useRouter()
			const state = reactive({
				quantity: 1,
				product:null,
				total: 0
			})

			function addCart(prod:Object){

				state.product = prod.id
				state.total = state.quantity * prod.product_price

				console.log(state)
				CartService.add_cart(state)

			}


			return {
				product,
				router,
				addCart
			}
		}
	}
</script>

<template>
	<div class="product p-4 lg:p-6 relative border border-gray-200 rounded-3xl">


		<div   class="cursor-pointer absolute top-6 right-6 w-6 h-6 lg:w-8 lg:h-8 flex items-center justify-center border border-pink-100 rounded-lg bg-pink-100">
			<span class="text-xs lg:text-sm material-icons text-pink-400">
				favorite
			</span>
		</div>


		<div class="flex justify-center">
			<img :src="product?.product_image" class="h-28 w-28 lg:h-56 lg:w-56  w-full rounded-lg object-fill" alt="">


		</div>


		<div class="text-gray-600 mt-2 font-semibold text-xs lg:text-base">
			<h4 class="capitalize">
				{{product?.product_name}}
			</h4>
		</div>

		<div class="mt-1">
			<div class="flex items-center space-x-1">
				<span v-for="i in 5" class="material-icons text-yellow-500 text-sm lg:text-base">
					star
				</span>
			</div>
		</div>


		<div class="mt-4">
			
			<div class="flex flex-col lg:flex-row lg:items-center lg:justify-between">
				<div>
					<span class="text-xs">
						$
					</span>
					<span class="text-sm font-bold">
						{{product?.product_price}}
					</span>
				</div>

				<button @click="addCart(product)" class="hover:bg-green-600 mt-4 lg:mt-0 hover:text-white 

				hover:border-none transition-all duration-300 px-3 text-xs rounded-xl flex items-center py-2 border border-gray-200">
					<span class="material-icons text-sm lg:text-base lg:mr-2">
						shopping_bag
					</span>

					<span class="
					font-semibold capitalize">
						add to cart	
					</span>


				</button>

			</div>

		</div>


	</div>
</template>