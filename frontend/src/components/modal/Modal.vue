<script lang="ts">
	export default {
		setup() {

		}
	}

</script>

<template>
	<div id="modal">
		<div class="modal-header mb-2">
			<slot name="header">
				
			</slot>
		</div>
		<div class="modal-body mb-2">
			<slot name="body">
				
			</slot>
		</div>
		<div class="modal-footer mb-2">
			<slot name="footer">
				
			</slot>
		</div>
	</div>
</template>

