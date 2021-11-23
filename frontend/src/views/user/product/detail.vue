<script lang="ts">
	import {onMounted, reactive, ref} from 'vue'
	import {useRoute, useRouter} from 'vue-router';
	import ProductService from '@/models/product/service';

	export default {

		setup(){
			
			const product = ref(null);

			const state = reactive({
				quantity: null,
			})

			const route = useRoute()

			onMounted(async () => {
				await ProductService.get_detail(route.params.id)
				.then((resp) => {
					product.value = resp.data
					console.log(resp)
				})

			})

			return {
				product,
				state
			}
		}
	}


</script>

<template>
	<div class="lg:p-12 p-6">
		<div class="flex w-full justify-center">
			<div class="w-full lg:w-7/8 lg:mr-72">
				<div class="lg:w-3/3">
						
				
					<div class="mt-4">
						<div class="lg:grid lg:gap-x-6 lg:grid-cols-2">
							<img :src="product?.product_image" class="rounded-lg h-98 shadow-md" alt="">
							<div class="flex flex-col ">
								<div class="flex text-gray-700 justify-between">
										<h1 class="lg:text-2xl font-semibold capitalize">
											{{product?.product_name}}
										</h1>
									</div>
								<div class="mt-1 lg:mb-6 flex  items-center">

									<ul class="flex mr-1">
										<li v-for="i in product?.ratings_avg">
											<span class="iconify text-xs text-yellow-400" data-icon="ant-design:star-filled"></span>
										</li>
									</ul>
									<span class="text-gray-500 text-xs">
										({{product?.reviews_count}})
									</span>
								</div>
								<h1 class="text-green-600 lg:text-3xl font-bold">
									<span>
										Rp.
									</span>
									<span>
										{{product?.product_price}}
									</span>
								</h1>
								<div  class=" lg:mt-6 text-sm capitalize text-gray-500">
										<table>
											<tr>
												<td>Product from</td>
												<td>:</td>
												<td>
													<span class="font-bold">
														{{product?.product_detail?.product_from.product_from}}
													</span>	
												</td>

											</tr>
											<tr>
												<td>Product weight</td>
												<td>:</td>
												<td>
													<span class="font-bold">
														{{product?.product_detail?.weight}}
													</span>	
													<span>
														gram
													</span>
												</td>

											</tr>
										</table>
										<div class="lg:mt-6 lg:h-64 mt-2">
										{{product?.product_detail?.description}}
										</div>
										<div class="mt-2">
											
										</div>
								</div>
							
							</div>
								<div class="fixed text-gray-600 text-xl rounded-lg bg-white mr-4 shadow-xl right-0 p-4 lg:top-25 lg:mr-12 lg:w-72  ">
									<div class="header text-green-600  font-semibold capitalize">
										cart
									</div>
									<div class="lg:mt-4">
										<div class="mt-2">
											<div class="form-group mb-2">
												<label for="">
													quantity
												</label>
												<input v-model="state.quantity" type="number" class="form-control px-2 py-1">
											</div>
											<div class="flex flex-col w-full space-y-4 lg:mt-6 items-center">
												<button class="py-2 w-full  text-xs capitalize btn text-pink-500  rounded-md border border-pink-200">
													<div class="flex items-center">
														<span class="iconify mr-2" data-icon="carbon:favorite"></span>
														<span>
															add to favorites
														</span>
													</div>
												</button>
												<button class="btn w-full py-3 text-xs btn-primary">
													<div class="flex items-center">
														<span class="iconify icon" data-icon="akar-icons:shopping-bag"></span>
														<span>
															add to cart
														</span>
													</div>
												</button>
											</div>
										</div>
									</div>
								</div>
						</div>
					</div>


				</div>
			
			</div>
		</div>
	</div>
</template>

<style type="text/css">
	table tr td:nth-child(1){
		width: 120px;
	}
	table tr td:nth-child(2){
		width: 20px;
	}
	table tr {
		height: 1.50rem;
	}

	.form-group .form-control {
		padding: .5rem .85rem;
	}

	.form-group label {
		margin-bottom: .75rem;
	}

	button {
		padding: .5rem 1rem;
	}
</style>