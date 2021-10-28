<script lang="ts">
	import User from '@/models/user/user_model'

	export default {
		setup() {

			return {
				User
			}
		}
	}
</script>
<template>
	<div
	class="text-sm text-gray-600"
	>
	
		<div class="flex flex-col">
				<div class="flex flex-col items-center">
					<!-- <div class="rounded-full h-24 w-24 bg-gray-600">
			
					</div> -->
					<img :src="User.user?.profile.photo" class="h-24 w-24 rounded-full" alt="">
					<div class="capitalize mt-4 text-gray-700">
						{{User.user?.profile.firstname}} {{User.user?.profile.lastname}}
					</div>
					<div class="lg:mt-1 text-xs text-gray-500">
						{{User.user?.email}}
					</div>
				</div>
				
				<ul class="mt-6 p-6">
					<li class="py-4 w-full hover:border-green-600 cursor-pointer transition-all duration-300 hover:text-green-600 flex items-center capitalize border-b-2 border-gray-100">
						<span class="iconify mr-2" data-icon="mdi:account-circle-outline"></span>
						<span>
							Change Email
						</span>
					</li>
					<li class="py-3 hover:border-green-600 cursor-pointer transition-all duration-300 hover:text-green-600 flex items-center capitalize border-b-2 border-gray-100">
						<span class="iconify mr-2" data-icon="mdi:lock-outline"></span>
						<span>
							Change Password
						</span>
					</li>
				</ul>
		</div>


	</div>
</template>