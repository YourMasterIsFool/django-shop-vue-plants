<script lang="ts">
	import {onMounted, ref, computed, defineAsyncComponent, inject} from 'vue'
	import CartService from '@/models/cart/cart_service'
	import Carts from './components/index/Carts.vue'
	import Cart from '@/models/cart/cart_model'
	
	const SpinnerComponent = defineAsyncComponent({
		loader:() => import('@/components/loading/SpinningBar.vue')
	});

	export default {
		components:{
			Carts,
			SpinnerComponent
		},
		setup() {

			const card_types = ref<Array>([
				{
					type: 'Paypal',
					icon: 'logos:paypal'
				},
				{
					type: "Visa",
					icon: 'logos:visa'
				}
			])

			const loading = inject('loading')


			// selected card for payment
			const selected_card = ref(0);

			// shipping card price
			const shipping = ref(200);


			//calculate sub total with from quantity * product
			const subtotal = computed(() =>{
				const subtotal = Cart.carts.reduce((acc, obj) => {
					let subtotal = parseInt(obj.quantity * obj?.product.product_price)

					return acc + subtotal
				}, 0)

				return subtotal
			})


			// calculate all total subtotal + shipping
			const total = computed(() => {
				return subtotal.value + shipping.value
			})

			onMounted(() => {
				CartService.get_cart()
				.then((resp) => {
					console.log(resp)
				})
			})


			return {
				Cart,
				card_types,
				selected_card,
				subtotal,
				total,
				shipping,
				loading
			}
		}
	}
</script>

<template>
	<div class="lg:p-12">
	
		<div class="text-gray-700 ">
			<div class="lg:w-2/3 lg:mr-24">
				
				<div class="flex items-center justify-between">
							<h1 class="lg:text-2xl capitalize text-gray-700 font-semibold">
					Shopping Cart
					</h1>
					<h1 class="lg:text-lg capitalize text-gray-700 font-semibold">
					{{Cart.carts.length}} Items
					</h1>



				</div>

				

				<div class="bg-white lg:p-8 rounded-xl mt-4 border border-gray-100">
					
					
					<Carts class="">
						
					</Carts>

					
				</div>	

			</div>

			<div class="payment dekstop fixed bottom-0 w-full h-20 lg:h-auto lg:w-auto  lg:bg-gray-50 rounded-xl lg:border border-green-600 bg-white  text-black  lg:border-gray-200 lg:p-6 lg:right-4 lg:top-20 lg:w-1/4">
				<h1 class="uppercase font-bold  lg:block hidden text-lg">
					 Card Details
				</h1>
				<div class="lg:mt-2 body">
					<div class="mb-2">
						<h2 class="capitalize text-xs">
						 card type
						</h2>

						<div class="flex mt-2 space-x-4">
							<div v-for="(card, index) in card_types" :class="[ selected_card == index ? ' border-black' : 'border-gray-300']" @click="selected_card = index" class="radio relative">
								<span class="iconify icon" :data-icon="card.icon"></span>
								<div :class="[selected_card == index ? 'block' : 'hidden']" >
									<span class="iconify absolute right-1 top-1" data-icon="ant-design:check-circle-outlined"></span>
								</div>
								
								<input type="radio" class="" name="">
							</div>
							
						</div>
					
					</div>
					<div class="form-group">
						<label for="">
							Name on card
						</label>
						<input type="text" class="form-control">
					</div>
					<div class="form-group">
						<label for="">
							Card Number
						</label>
						<input type="text" class="form-control">
					</div>
					<div class="grid grid-cols-2 gap-x-2">
						<div class="form-group">
							<label for="">
								Expiration Date
							</label>
							<input type="text" class="form-control">
						</div>
						<div class="form-group">
							<label for="">
								cvv
							</label>
							<input type="text" class="form-control">
						</div>
					</div>
					<div  class="mt-2 flex flex-col space-y-1">
						<div class="flex items-center justify-between">
							<h1 class="font-semibold text-sm mb-1">
								Subtotal
							</h1>
							<span class="text-xs font-semibold">
								${{subtotal}}
							</span>
						</div>

						<div class="flex items-center justify-between">
							<h1 class="font-semibold text-sm mb-1">
								Shipping
							</h1>
							<span class="text-xs font-semibold">
								${{shipping}}
							</span>
						</div>

						<div class="flex items-center justify-between">
							<h1 class="font-semibold text-sm mb-1">
								Total
							</h1>
							<span class="text-xs font-semibold">
								${{total}}
							</span>
						</div>

						<button class="btn btn-primary font-semibold justify-between px-4 mt-2 py-3">
							<span>
								$ {{total}}
							</span>

							<div>
								<span class="mr-2">
									Checkout
								</span>
								<span class="iconify" data-icon="bi:arrow-right"></span>
							</div>
						</button>
					</div>
				</div>
			</div>
			
		</div>
	</div>
</template>

<style lang="postcss" scoped>
	table{
		td {
			padding-bottom: 1.5rem;
		}
	}

	.radio {
		@apply  border rounded-lg px-4 flex items-center justify-center h-16 w-20;
	}
	.radio input {
		@apply absolute cursor-pointer w-full h-full z-0 opacity-0;
	}
	
	.radio .icon {
		@apply absolute text-sm;
	}

	.form-group {
		@apply mb-2
	}
	.form-group label {
		@apply text-black text-xs
	}

	.form-group .form-control {
		@apply pl-4;
	}
</style>