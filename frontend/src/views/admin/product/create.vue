<script lang="ts">
	import {defineAsyncComponent} from 'vue'
	import CreateSkeleton from './skeleton/CreateSkeleton.vue'

	const CreateComponent = defineAsyncComponent({
		loader: () => import('./components/CreateComponent.vue'),
		loadingComponent: CreateSkeleton
	})


	export default {
		components: {
			CreateComponent,
			CreateSkeleton
		},
		setup() {

		}
	}
</script>


<template>
	<div>
		<CreateComponent></CreateComponent>
	</div>
</template>
