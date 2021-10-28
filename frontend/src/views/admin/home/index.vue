<script lang="ts">
	import {defineAsyncComponent} from 'vue'

	const Sidebar = defineAsyncComponent({
		loader: () => import('@/components/sidebar/Sidebar.vue')
	})

	const Analystics = defineAsyncComponent({
		loader: () => import('./components/index/Analystics.vue')
	})

	const Revenue = defineAsyncComponent({
		loader: () => import('./components/index/Revenue.vue')
	})

	const PopulerProduct = defineAsyncComponent({
		loader: () => import('./components/index/PopulerProduct.vue')
	})


	export default{
		components: {
			Sidebar,
			Analystics,
			Revenue,
			PopulerProduct
		}
	}
	

</script>


<template>
	<div class="px-4">
		<div>
				<Analystics></Analystics>

				<Revenue></Revenue>
				
				<PopulerProduct></PopulerProduct>

		</div>
	</div>
</template>