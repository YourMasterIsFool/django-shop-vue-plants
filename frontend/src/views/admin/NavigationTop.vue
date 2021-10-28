<script lang="ts">
	import {ref} from 'vue';


	export default {
		setup() {


			const notifications = ref(false);


			return {
				notifications
			}
		}
	}


</script>

<template>
	<div class="navigation-top h-20 px-2 lg:px-6 justify-between flex items-center ">
		<div class="">
			<div class="text-base lg:text-xl text-gray-700 font-semibold">
				<span class="mr-1">
					Hello,
				</span>
				<span>
					Verrandy
				</span>
			</div>
			<div class="text-xs text-gray-500">
				welcome back
			</div>
		</div>
		<div  @click="notifications = !notifications"  class="relative flex items-center">
			<span class="iconify cursor-pointer text-gray-500 text-xl" data-icon="mdi:bell-outline"></span>
			
		</div>
	</div>
</template>