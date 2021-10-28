<script lang="ts">
	import TextSkeleton from '@/components/skeleton/TextSkeleton.vue';
	import InputSkeleton from '@/components/skeleton/InputSkeleton.vue';



	export default {
		components: {
			TextSkeleton,
			InputSkeleton
		}
	}
</script>

<template>
	<div>
		<div class="mb-8">
			<div class="flex items-center">
				<div class="flex w-full items-center justify-between space-x-4">
					<div class="relative">
						<div class="w-48">
							<InputSkeleton></InputSkeleton>
						</div>
					</div>

					<div class="w-32">
							<InputSkeleton></InputSkeleton>
						</div>
				</div>
			</div>
		</div>
		<div class="text-gray-600 font-light">
			<table id="table-product" class="w-full ">
			<tr class=" font-normal ">
					<td>
						<TextSkeleton></TextSkeleton>
					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
			</tr>

			
			<tr v-for="i in 4">

					<td>
						<TextSkeleton></TextSkeleton>
					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
					<td>
						<TextSkeleton></TextSkeleton>

					</td>
			</tr>

		</table>
		</div>
</div>
</template>

<style type="text/css">
	tr {
		height:  32px;
	}
</style>