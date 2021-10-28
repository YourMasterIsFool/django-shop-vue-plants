<script lang="ts">
	import {defineAsyncComponent} from 'vue';
	import IndexSkeleton from './skeleton/IndexSkeleton.vue'
	import ProductService from '@/models/product/service'

	const IndexComponent = defineAsyncComponent({
		loader: () => import('./components/IndexComponent.vue')
		,
		loadingComponent: IndexSkeleton
	})



	export default {

		components: {
			IndexComponent,
			IndexSkeleton
		}
	}
</script>

<template>
	<div>
		<IndexComponent></IndexComponent>
	</div>
</template>

 