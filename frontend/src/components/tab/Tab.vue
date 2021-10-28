<script>
	import { inject  } from 'vue';

	export default {
		setup() {
			const selectedTab = inject('selectedTab');
		}
	}
</script>

<template>
	<div id="tabs">
		<slot>
			
		</slot>
	</div>
</template>