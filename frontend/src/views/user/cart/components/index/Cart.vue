<script lang="ts">
	import {reactive, onBeforeMount, inject, toRefs, ref, defineAsyncComponent } from 'vue';
	import CartService from '@/models/cart/cart_service';



	const SpinnerComponent = defineAsyncComponent({
		loader:() => import('@/components/loading/SpinningBar.vue')
	});


	export default {
		components: {
			SpinnerComponent
		},
		props: {
			cart: {
				type: Object,
				default: null
			},
			index: Number
		},
		setup(props) {

			const { cart, index } = toRefs(props)
			const loading = inject('loading')

			const state = reactive({
				quantity: null,
				total: null,
				id: null,
				index: null,
			})

			async function removeCart(id, index){
				
				const schema = {
					id: id,
					index: index
				}


				await CartService.remove_cart(schema)

			}


			async function updateCart(cart){
				state.index = index
				state.id = cart.id

				state.total = state.quantity * cart?.product.product_price

				CartService.update_cart(state)
			}

			onBeforeMount(() => {
				state.quantity = props.cart.quantity
				state.total = props.cart.total
			})

			return {
				cart,
				index,
				state,
				updateCart,
				removeCart,
				loading
			}
		}
	}
</script>


<template>
	<div>
		{{loading}}
		<div id="card" class="grid lg:grid-cols-8 lg:gap-x-12">

					<div  class="lg:col-span-4 break-all lg:flex lg:flex-row">
					
						<img :src="cart?.product.product_image" class="lg:w-36 rounded-xl lg:h-36" alt="">
						<div class="justify-center lg:flex font-semibold break-words capitalize lg:flex-col lg:ml-4">
							<span class="mb-2">
								{{cart?.product.product_name}}
							</span>
							
						</div>
					</div>

					<div class="lg:col-span-1 justify-center flex flex-row items-center">
						<span>
							$
						</span>
						<span class="text-xs font-semibold">
							{{cart?.product.product_price}}
						</span>
					</div>

					<div class="col-span-1 flex flex-col justify-center items-center">

						<input @blur="updateCart(cart, index)" v-model="cart.quantity" type="number" min="0" class="text-gray-600 text-xs py-2 bg-gray-50 lg:w-16 rounded-lg outline-none">
					</div>

					<div class="col-span-1 text-xs justify-center flex items-center">
						<span class="text-xs">
							$
						</span>
						<span class="text-xs font-semibold">
							{{cart.quantity * cart?.product.product_price}}
						</span>
					</div>

					<div class="col-span-1 justify-center flex items-center">
						<button @click="removeCart(cart.id, index)" class="btn btn-danger">
							<div class="flex items-center justify-center">	
								<spinner-component custom-style="h-4 w-4 border-red-600" v-if="loading"></spinner-component>
								<div v-else>
									<span class="iconify" data-icon="ph:trash-thin"></span>
								</div>
							</div>
						</button>
					</div>
		</div>

	</div>
</template>