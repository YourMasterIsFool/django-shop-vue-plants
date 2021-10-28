<script lang="ts">
	import {inject, onMounted, ref} from 'vue';
	import CategoryService from '@/models/category/service';
	import categories_store from '@/models/category/store'

	export default {
		setup() {

			console.log(categories_store)
			
			const categories = ref(null)

			onMounted(() => {
			
				CategoryService.get_all()
				.then((resp) => {
					console.log(resp)
					categories.value = resp.data
				})
			
			})


			return {
				categories
			}
		}
	}
</script>

<template>
	
	<div id="filter" class="border-r bg-white border-gray-100 ">
			<h1 class="px-10 py-4 text-md pb-4 border-b border-gray-100 font-semibold capitalize">
				filter 
			</h1>
			<div class=" pt-4 pb-6 px-10">
				<h1 class="text-md font-semibold ">
					Categories
				</h1>
				<ul class="mt-4">
					<li v-for="(category, index) in categories" class=" py-2 flex items-center capitalize">
						<input type="checkbox" class="mr-4 text-green-200">
						<span>
							{{category.category}}
						</span>
					</li>
					<li class="py-2 cursor-pointer pl-7 flex items-center">
						<span>
							others
						</span>

						<span class="ml-2 material-icons">
							expand_more
						</span>
					</li>
				</ul>

			</div>
			<hr class="border border-gray-100">
			<div class=" px-10 py-8">
				<h1 class="font-semibold capitalize">
					Price Range
				</h1>
				<div class="mt-4 flex items-center space-x-4">
					<div class="px-4 flex-1  bg-gray-100 text-gray-300 font-light rounded-lg capitalize py-2">
						min
					</div>
					<div class="relative flex-1">
						<span class="font-semibold  absolute top-2 left-4">
							$
						</span>
						<input type="number" class="border border-gray-300 text-gray-600 w-32 text-base outline-none py-2 pl-8 rounded-lg text-black">
					</div>
				</div>
				<button class="bg-green-600 mt-6 w-full py-2 px-6 rounded-xl text-white font-light capitalize">
					set price
				</button>	
			</div>
			<hr class="border border-gray-100">
			<div class="py-6 px-10">
				<h1 class="text-base font-semibold capitalize">
					rating					
				</h1>
				<div class="flex items-center mt-4">
					<input type="checkbox" class="mr-4">

					<div class="flex items-center mr-2">
						<span v-for="i in 5" class="text-yellow-400 text-base material-icons">
							star
						</span>
					</div>
					<span class="capitalize">
						above
					</span>
				</div>
			</div>

		</div>

</template>