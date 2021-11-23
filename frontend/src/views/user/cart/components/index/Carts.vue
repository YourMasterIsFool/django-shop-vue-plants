<script lang="ts">
	import {reactive, onBeforeMount} from 'vue'
	import Cart from '@/models/cart/cart_model'
	import CartVue from './Cart.vue'

	export default {
		components: {
			CartVue
		},
		setup() {
			

			return {
				Cart,
			
			}
		}
	}

</script>


<template>
	<div>
		<ul v-if="Cart.carts.length > 0">
			<li  class="lg:pb-8" v-for="cart in Cart.carts" >
				<CartVue :cart="cart"></CartVue>
			</li>
		</ul>
		<div  class="h-72 w-full flex justify-center items-center">
			<div class="w-72">
				<span class="text-xl text-green-600 font-semibold">
				Tidak memiliki item di keranjang	
			</span>	
			</div>		
		</div>
	</div>
</template>
