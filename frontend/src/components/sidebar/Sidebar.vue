<script lang="ts">

	import { toRefs } from 'vue'
	
	export default {
		props: {
			customStyle:String,
		},
		setup(props) {

			const customStyle = toRefs(props)


			return {
				customStyle
			}
		}
	}
</script>

<template>
	<div :class="customStyle">
		<div class="header">
			<slot name="header"></slot>
		</div>
		<div class="body">
			<slot name="body">
				
			</slot>
		</div>
		<div class="footer">
			<slot name="footer">
				
			</slot>
		</div>
	</div>
</template>