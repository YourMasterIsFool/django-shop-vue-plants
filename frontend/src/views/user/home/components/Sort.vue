<script lang="ts">
	

	import {ref} from 'vue';

	export default {
		setup() {
			const showSort = ref(false);

			return {
				showSort
			}
		}		
	}
</script>

<template>
	<div class="flex text-sm items-center">
		<button @click="showSort = true" class="border-b rounded-lg px-3 py-1 lg:hover-none hover:bg-gray-100 duration-300 transition-all
		hover:shadow-md lg:border-none lg:text-base text-xs flex lg:block items-center">
			<span class="lg:mr-12">
				Sort
			</span>
			<span class=" text-sm ml-4 lg:hidden block material-icons">
				filter
			</span>
		</button>

		<div v-show="showSort" class="fixed h-screen top-0 w-screen bg-black bg-opacity-20 z-0">
				
			</div>
		<div :class="[showSort ? 'fixed bottom-0 left-0 rounded-tl-xl rounded-tr-xl z-50 bg-white items-start p-4 w-screen flex-col h-3/4' : 'block h-0 lg:h-auto ']" class=" w-0 overflow-hidden flex lg:items-center lg:w-screen lg:w-auto">
				
			<h1 class="hidden lg_block">
				Sort
			</h1>
			<div class="grid grid-cols-3 lg:space-x-4 lg:flex  gap-2 z-10 lg:z-0">
					<button class="rounded-xl bg-green-600 text-white lg:px-4 py-2 ">
				Revelance	
				</button>


				<button class="rounded-xl border-2 border-gray-200 capitalize px-4 py-2 ">
					Popular	
				</button>
				<button class="rounded-xl border-2 border-gray-200 capitalize px-4 py-2 ">
					Most new	
				</button>
				<button class="rounded-xl border-2 border-gray-200 capitalize px-4 py-2 ">
					price	
				</button>
				</div>

		</div>
	</div>
</template>