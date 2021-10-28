<script lang="ts">
	
	import Cart from '@/models/cart/cart_model'

	export default {
		setup() {


			return {
				Cart
			}
		}
	}

</script>


<template>
	<div>
		<table id="cart" class="w-full mt-6 hidden lg:block">
			<tr v-for='cart in Cart.carts'>
				<td width="50">
					<input type="checkbox">
				</td>
				<td width="400">

					<div class="flex lg:pr-10">
						<img :src="cart?.product.product_image" class="rounded-xl h-24 w-24" alt=""/>

						<div class="flex flex-col ml-2">
							<span class="capitalize font-semibold">
								{{cart?.product.product_name}}
							</span>
							<span class="mt-1 text-gray-500 text-xs">
								{{cart?.product.product_detail?.description}}
								
							</span>

						</div>
					</div>	

				</td>
				<td width="100">
					<span class="font-bold text-xl">
						$6000
					</span>
				</td>
				<td width="100">
					<div class="flex items-center text-xs">
						<span class="mr-2">
							Quantity:
						</span>
						<input type="number" class="lg:w-24 rounded-lg bg-gray-100 text-xs pl-3 outline-none py-2">
						
					</div>
				</td>
				
			</tr>
		</table>	
	</div>
</template>
