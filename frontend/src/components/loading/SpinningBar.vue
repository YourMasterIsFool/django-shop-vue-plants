<script lang="ts">

	export default {
		props:{
			customStyle:{
				type:String,
				default: "h-4 w-4 border-gray-600"
			},

		},
		setup(props){
			return {
				props
			}
		}
	}
</script>

<template>
	<div>
	    <div style="border-top-color:transparent"
	    	:class="props.customStyle"
	        class=" border-2 rounded-full animate-spin">
	        	
	        </div>
	</div>
</template>