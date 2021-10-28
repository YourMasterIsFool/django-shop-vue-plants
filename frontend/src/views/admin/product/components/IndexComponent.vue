<script lang="ts">
	import {useRouter} from 'vue-router'
	import {ref, inject} from 'vue'
	import ProductService from '@/models/product/service'
	import { ProductStore } from '@/models/product/model'
	import IndexSkeleton from '../skeleton/IndexSkeleton.vue'

	export default {
		components: {
			IndexSkeleton
		},
		setup() {
			const router = useRouter()
			const products = ref(null);
			const loading = ref(true);
			const moment = inject('moment');
			const selectedModal = ref(null);

			ProductService.get_all()
			.then((resp) => {
				products.value = resp.data

				console.log(resp.data)

				loading.value = false
			})

			return {
				router,
				ProductStore,
				products,
				loading,
				moment,
				selectedModal
			}
		}
	}

</script>

<template>

	<IndexSkeleton v-if="loading"></IndexSkeleton>
	<div v-else>
		<div class="mb-8 mt-4 lg:mt-0 px-4">
			<div class="flex items-center">
				<div class="lg:flex-row flex-col-reverse flex w-full lg:items-center lg:justify-between lg:space-x-4">
					<div class="relative">
						<span class="text-gray-500 text-base top-3 left-2  absolute material-icons">
							search
						</span>
						<input type="text" placeholder="Search your product .." class="bg-gray-100 w-full outline-none text-gray-600 pl-8 rounded-2xl py-3 px-4 text-sm ">
					</div>

					<div class="flex mb-4 lg:mb-0 justify-end lg:block">
						<button @click="router.push({ name: 'admin-product-create'})" class="hover:bg-green-500 hover:text-white transition-all duration-300 flex items-center py-2 px-3 lg:py-3 lg:px-8 text-xs capitalize rounded-xl text-green-500   border border-green-500">
					
					 <span  class="iconify mr-1 text-lg" data-icon="ion:cube-outline"></span>
					 <span>
					 	add product
					 </span>
					</button>
					</div>
				</div>
			</div>
		</div>
		<div class="text-gray-600 pb-12 lg:pb-0 overflow-x-scroll lg:overflow-x-hidden font-light">
			<table id="table-product" class="w-full ">
			<tr class=" font-normal ">
					<td class="">
						product
					</td>
					<td>
						Price
					</td>
					<td>
						Order
					</td>
					<td>
						Date
					</td>
					<td>
						Status
					</td>

					<td>
					
					</td>
			</tr>

			
			<tr v-for="(product, index) in products" class="rounded-xl  font-normal ">

					<td width="200" class="flex text-xs items-center capitalize">

						<img :src="product.product_image" class="w-24 rounded-lg h-24" alt="">
						<div class="pl-2 word-break font-semibold justify-start">
							<span class="">
								{{product.product_name}}
							</span>
						</div>
					</td>
					<td>
						<span class="text-green-600 font-semibold">
							${{product.product_price}}
						</span>
					</td>
					<td>
						{{product.stock}}
					</td>
					<td>
						{{moment(product.date).format('dddd MMMM yyyy')}}
					</td>
					<td>
						<div>
							<span v-if="product.status == 'published'" class="px-4 py-2 text-xs bg-green-600 rounded-lg capitalize text-white">
								{{product.status}}
							</span>

							<span v-else class="px-4 py-2 text-xs bg-yellow-600 rounded-lg capitalize text-white">
								{{product.status}}
							</span>
						</div>
					</td>

					<td>
						<div class="relative flex items-center flex-col space-y-4">
							<button @click="selectedModal = index" class="px-4 hover:bg-gray-200 transition-all duration-300 py-1 text-xs rounded-full border border-gray-200 text-gray-600">


								<span class="iconify text-2xl" data-icon="mdi:dots-horizontal"></span>
							</button>
							<button @click="selectedModal = index" class="px-4 bg-red-500 text-white transition-all duration-300 py-1 text-xs rounded-full ">


								<span class="iconify text-2xl" data-icon="mdi:trash-can-outline"></span>
							</button>
						</div>
					</td>
			</tr>

		</table>
		</div>
	</div>
</template>

<style lang="postcss" scoped>
	#table-product tr:nth-child(1) > td {
		@apply pb-6 bg-white text-sm lg:text-xl  capitalize;
	}

	#table-product tr:nth-child(1) {
		@apply border-none;
	}

	#table-product tr {
		@apply rounded-full border-b-2 border-gray-400;
		
	}
	#table-product td {
		@apply  text-xs  lg:text-sm pt-4 px-4 pb-4; 
	}
</style>