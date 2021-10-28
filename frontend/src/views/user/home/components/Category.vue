<script>
	import {inject, onMounted, ref} from 'vue';
	import CategoryService from '@/models/category/service';

	export default {
		setup() {
			
			const axios = inject('axios');
			
			const categories = ref(null)

			onMounted(() => {
			
				CategoryService.get_all()
				.then((resp) => {
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
	<div>
		{{categories}}
	</div>
</template>