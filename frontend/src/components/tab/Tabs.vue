<script lang="ts">
	import { inject, ref, provide, onMounted, provide, watch } from 'vue';

	export default {

		setup(_,{ emit }) {
			const tabs = inject('tabs')
			const selectedTab = ref(tabs.value[0].name);
			
			watch(selectedTab, (newVal) => {
				emit('tabSelect', newVal)
				console.log(newVal)
			})

			return {
				tabs,
				selectedTab,
				
			}

		}


	}

</script>

<template>
	<div id="tabs" class="w-full lg:w-auto overflow-x-hidden">

		<ul class="flex flex-row w-80 scrollbar-hidden lg:w-full overflow-x-scroll items-start lg:overflow-x-auto  space-x-12 items-center">
			<li @click="selectedTab = tab.name" :class="selectedTab == tab.name ? 'border-green-600 border-b-4' : 'border-b-4 border-white'" class="cursor-pointer text-sm lg:text-base transition-all whitespace-nowrap  duration-300  flex justify-center capitalize pb-6" v-for="(tab, index) in tabs">
	
				{{tab.name}} 


			</li>
		</ul>

		
		<div class="py-2">
			<slot>
				
			</slot>
		</div>


	</div>
</template>

<style lang="css">

</style>