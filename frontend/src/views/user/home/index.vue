<script lang="ts">
	import {defineAsyncComponent, ref, provide, inject, onMounted, shallowRef} from 'vue'
	import Tabs from '@/components/tab/Tabs.vue';
	import CategorySkeleton from './skeleton/CategorySkeleton.vue';
	import FilterSkeleton from './skeleton/FilterSkeleton.vue';
	import {width} from '@/mixins/screen'
	import ProductService from '@/models/product/service'

	const Sort = defineAsyncComponent({
		loader: () => import('./components/Sort.vue')
	})

	const Search = defineAsyncComponent({
		loader: () => import('./components/Search.vue')
	})

	const Filter = defineAsyncComponent({
		loader: () => import('./components/Filter.vue'),
		loadingComponent: FilterSkeleton,
	})

	const Product = defineAsyncComponent({
		loader:() => import('./components/Product.vue')
	})

	const Sidebar = defineAsyncComponent({
  		loader: () => import('@/components/sidebar/Sidebar.vue')
	})

	const Tab = defineAsyncComponent({
		loader: () => import('@/components/tab/Tab.vue')
	})


	const Reviews = defineAsyncComponent({
		loader: () => import('./components/Reviews.vue')
	})


	const Category = defineAsyncComponent({
		loader:() => import('./components/Category.vue'),
		loadingComponent: CategorySkeleton
	})


	const Details = defineAsyncComponent({
		loader: () => import('./components/Details.vue')
	})

	export default {
		
		components: {
			Sidebar,
			Tab,
			Tabs,
			Details,
			Reviews,
			Category,
			Filter,
			Product,
			Search,
			Sort
		},


		setup() {

			const tabs = ref([
				{
					name: "Details",
					component: shallowRef(Details)
				},
				{
					name: "Reviews",
					component: shallowRef(Reviews)
				},
			])




			provide('tabs', tabs)


			const products = ref(null)

			const selectedProduct = ref(null)
			const selectedProductDetail = ref(null)
			function fetchProductSelect(id:Number) {
				const product = products.value.find(map => map.id == id)
				selectedProduct.value = product
			}



			onMounted(() => {
				ProductService.get_all()
				.then((resp) => {
					products.value = resp.data
				})
			})

			const showFilter = ref(null)
			const selectedTab = ref(0)


			function tabSelect(value) {

				selectedTab.value = value

			}


			return {
				tabs,
				showFilter,
				selectedTab,
				tabSelect,
				products,
				selectedProduct,
				fetchProductSelect,
			}
		}
	}
</script>

<template>
	<div>
		<div class="w-full text-gray-600 flex">
			
		

			<Filter :class="[showFilter ? 'fixed': 'hidden']" class="  lg:block lg:w-1/5 bg-white z-10"></Filter>


			<div class="w-full lg:w-4/5">


				<div class=" border-r border-gray-100">
					<div class="p-4 lg:p-12">
						
						<Search></Search>

						<div class="mpt-2 lg:mt-8">
							<Sort></Sort>
						</div>


						<div class="mt-8">
							<div class="grid grid-cols-2 lg:grid-cols-3 lg:gap-6 gap-4">
								<Product  class="cursor-pointer hover:bg-gray-100 transition-all duration-300" @click="fetchProductSelect(product.id)" :product="product" v-for="product in products">
									
								</Product>
							</div>
						</div>

					</div>
				</div>
		


			</div>



		</div>
	</div>
</template>