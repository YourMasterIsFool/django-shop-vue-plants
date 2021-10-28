<script lang="ts">
	import {reactive, onBeforeUpdate, onUpdated, inject, ref} from 'vue'
	import {useRouter} from 'vue-router'
	import ProductModel from '@/models/product/model'
	import ProductService from '@/models/product/service';
	import CategoryService from '@/models/category/service'
	import CategoryStore from '@/models/category/store';
	import SpinningBar from '@/components/loading/SpinningBar.vue';

	export default {
		components:{
			SpinningBar
		},
		setup(){

			const loading = ref(false)
			const router = useRouter()

			const categories = ref(null);

			const addMoreImage = ref(2);

			const state = reactive<ProductModel>({
				product_name: null,
				product_price: 0,
				category: null,
				date: null,
				status: 'published',
				description: null,
				product_image: null
			
			})

			const imageUrl = ref(null)


			const status = ref(
				[
					'published',
					'private'
				]
			)




			// onBeforeUpdate(() => {
			// 	images = []
			// })

			// onUpdated(() => {
			// 	console.log(images)
			// })

			async function addProduct() {
				loading.value = true

				let form_data = new FormData()

				for(var key in state) {
					form_data.append(`${key}`, state[key])
				}


				console.log(form_data)

				await ProductService.addProduct(form_data)
				.then((resp) => {
					console.log(resp)
					loading.value = false

					router.push({name: 'admin-product'})
				})
			}

				function imageChange(event){

					state.product_image = event.target.files[0]

					const url = window.URL.createObjectURL(event.target.files[0])

					imageUrl.value = url 
				}

			

			// get data category
			CategoryService.get_all()
			.then((resp) => {
				categories.value = resp.data
			})

			return {
				imageUrl,
				imageChange,
				state,
				addProduct,
				loading,
				router,
				loading,
			
				categories,
				status,
				addMoreImage,
			
			}
		}
	}
</script>

<template>
	<div>
		<div class="">
	
			<div class="lg:mb-2 text-green-800 font-semibold text-xl capitalize">
				add product 

			</div>

			<div class="text-gray-600 leading-5 tracking-wide w-2/3 text-xs">
				Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
				tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
				
			</div>

			<div class=" mt-6 lg:mt-12">
				<div class="grid lg:grid-cols-2 lg:gap-x-12">
					<div>
						<div class="form-group">
							<label class="">
								Product name
							</label>
							<input v-model="state.product_name" type="text" class="py-3 form-control bg-gray-100 outline-none rounded-lg text-gray-600 focus:border focus:border-gray-700 px-4 text-xs">
							<span class="text-gray-500 text-xs mt-2">
								Do not exceed 20 characters when entering the product name
							</span>
					
					
						</div>

						<div class="">
							<div class="">
								<div class="form-group">
									<label class="">
										Category
									</label>
									<select v-model="state.category"  class="py-3 form-control bg-gray-100 outline-none lg:text-base text-green-800 capitalize rounded-lg text-gray-600 focus:border focus:border-gray-700 px-4 text-xs">
										<option :value="category.id" class="bg-gray-50 my-24" v-for="category in categories">
											{{category.category}}
										</option>
									</select>
								</div>	
							</div>
					
						</div>

						<div class="form-group">
							<label class="">
								description
							</label>
							<textarea v-model="state.description" rows="5" type="text" class="py-3 bg-gray-100 outline-none rounded-lg form-control text-gray-600 focus:border focus:border-gray-700 px-4 text-xs">

							</textarea>
					
						</div>

					


					</div> <div> <div class="form-group"> <label class="">
					Images </label> <div class="grid lg:grid-cols-2
					gap-2"> <div 
					:class="[imageUrl ? 'h-64 w-64' : 'lg:hover:text-white']"
					class="relative  border hover:bg-green-600
					 transition-all duration-300
					text-green-600 border-green-600 rounded-lg border-dotted text-xs w-32 h-32">
										
									

									<img class=" h-64 w-full lg:w-64 " v-if="imageUrl" :src="imageUrl"  alt="">
									<input @change="imageChange" multiple="multiple"  name="" type="file" class="absolute w-full w-64 h-64 z-20 top-0 left-0 cursor-pointer opacity-0 h-full">
									<div class="flex z-10 hover:bg-black hover:bg-opacity-40 cursor-pointer  absolute top-0 left-0 h-full w-full items-center capitalize justify-center">
										 <span class="material-icons">
										 	image 
										 </span>
										 <span class="">
										 	upload image
										 </span>
									</div>
								</div>

								<!-- <button @click="[addMoreImage <= 8 ? addMoreImage += 1 : '']" :class="[addMoreImage <= 8 ? ' border-green-600 border-green-600 border-green-600 text-green-600 hover:text-white hover:bg-green-600' : ' text-red-600 border-red-600' ]" class="relative  cursor-pointer  transition-all duration-300 border  rounded-lg border-dotted  text-xs h-32">
									<div class="flex  h-full w-full items-center capitalize justify-center">
										 <div v-if="addMoreImage <= 8" class="flex justify-center items-center"> 
										 	<span class="material-icons">
										 	add
											 </span>
											 <span class="">
											 	add more image
											 </span>
										 </div>
										 <div class="flex justify-center items-center" v-else>
										 	<span class="material-icons">
										 		block
											 </span>
											 <span class="">
											 maksimum images
											 </span>
										 </div>
									</div>
								</button> -->
							
							</div>
							<span class="text-gray-500 text-xs mt-2">
								Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
								tempor incididunt ut labore et dolore magna aliqua. 
							</span>
						</div>

							<div class="grid lg:grid-cols-2 lg:gap-x-6">
									<div class="form-group relative">
										<label class="">
											Price
										</label>
										<div class="relative ">
											<span class="absolute top-2 left-4 text-green-600">
												$
											</span>
											<input v-model="state.product_price" type="number" class="py-3 bg-gray-100 form-control outline-none
											w-full rounded-lg text-gray-600  pl-8 text-green-700 focus:border focus:border-gray-700 px-4 text-xs" />
										
										</div>	
							 </div>	

							 <div class="form-group relative">
									<label class="">
										Date
									</label>
									<div class="relative ">
										<input v-model="state.date" type="date" class="py-3 bg-gray-100 outline-none form-control rounded-lg text-gray-600 pl-4 text-green-700 focus:border focus:border-gray-700 px-4 text-xs" />
									
									</div>
								
									
							 </div>	
						</div>

						<div class="form-group ">
							<label class="mb-4">
								Status
							</label>
							<div class="flex items-center space-x-4">
								<div v-for="stat in status" :class="[state.status == stat ? 'bg-green-600 text-white' :'']" class=" relative px-4 py-2 rounded-full border border-gray-200 text-xs capitalize">
								<span class="">
									{{stat}}
								</span>
								<input type="radio" :value="stat" v-model="state.status" class="top-0 z-10 left-0 cursor-pointer absolute w-full h-full opacity-0">
							</div>
							</div>
						</div>


						

						<div class=" grid mt-12 grid-cols-2 gap-4">
							<button @click="addProduct" class="border-green-600  lg:py-3 py-3 lg:px-6 px-4 rounded-lg lg:text-sm text-xs border bg-green-600 text-white justify-center flex items-center  capitalize">
								
							<SpinningBar v-if="loading" custom-style="h-6 w-6 border-white"></SpinningBar>
							<span v-else>
								add product
							</span>

							</button>
							<button class=" lg:py-3 py-3 lg:px-6 px-4 rounded-lg lg:text-sm text-xs border  text-green-600  capitalize">
								close
							</button>
						</div>

					</div>
				</div>
			</div>
		</div>
	</div>
</template>


<style lang="postcss">
	.form-group {
		@apply mb-4 flex flex-col;
	}

	.form-group label {
		@apply text-green-800 mb-2 capitalize;
	}
	.form-group input {
		@appy py-4 text-gray-600 text-sm px-2
	}
</style>