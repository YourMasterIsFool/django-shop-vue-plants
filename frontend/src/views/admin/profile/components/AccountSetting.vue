<script lang="ts">
	import User from '@/models/user/user_model'
	import UserService from '@/models/user/user_service'
	import {onMounted, ref, onBeforeMount, inject} from 'vue';


	export default {
 		setup(){
			const state = ref<User.user>();
			const moment = inject('moment');

			onBeforeMount(()=> {
				state.value = User.user?.profile
			})


			function updateUserProfile(){
				
			}

			onMounted(async() => {

			})



			return {	
				User,
				state,
				moment

			}
		}
	}
</script>

<template>
	<div>
		<div class="grid lg:grid-cols-2 lg:gap-y-4 lg:gap-x-6">
			<div class="form-group">
				<label for="">
					firstname
				</label>
				<input v-model="state.firstname"  type="text" class="form-control capitalize">
			</div>
			<div class="form-group">
				<label for="">
					lastname
				</label>
				<input v-model="state.lastname" type="text" class="form-control capitalize	">
			</div>

			<div class="form-group">
				<label for="">
					Gender
				</label>
				<div class="flex  items-center">
					<span class=" mr-4 text-sm text-gray-600 font-semibold">
					{{state?.gender}}
					</span>
					<button class="text-green-600 py-3 flex items-center text-xs">
						<span class="iconify text-base mr-1" data-icon="ph:note-pencil-light"></span>
						<span   class="capitalize">
							Update Gender
						</span>
					</button>
				</div>
			</div>

			<div class="form-group">
				<label for="">
					birth
				</label>


				<div class="flex  items-center ">
					<span v-show="state?.birth" class="mr-4 text-sm text-gray-600 font-semibold">
					{{moment(state?.birth).format('DD MMMM YYYY')}}
					</span>

						<button class="text-green-600 py-3 flex items-center text-xs">
							<span class="iconify text-base mr-1" data-icon="ph:note-pencil-light"></span>
							<span   class="capitalize">
								Update Birth
							</span>
						</button>

				</div>
			
			</div>

		</div>
		<div class="lg:flex lg:justify-end mt-4">
			 <button class="btn btn-primary">
			 	<span class="iconify mr-1" data-icon="mdi:content-save-outline"></span>
			 	<span>
			 		save
			 	</span>
			 </button>
		</div>
	</div>
</template>

<style lang="postcss">
	.form-group input {
		@apply px-3
	}
</style>