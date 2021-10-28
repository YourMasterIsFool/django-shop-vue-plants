<script lang="ts">
	import {inject, provide, ref, defineAsyncComponent, computed} from 'vue';
	import {useRouter} from 'vue-router'
	import Tabs from '@/components/tab/Tabs.vue';
	import AccountSetting from './components/AccountSetting.vue';


	const User = defineAsyncComponent({
		loader: () => import('./components/User.vue')
	})

	const AccountSetting = defineAsyncComponent({
		loader: () => import('./components/AccountSetting.vue')
	})

	export default {
		components: {
			User,
			Tabs,
			AccountSetting
		},
		setup() {

			const router = useRouter()


			const tabs = ref([
				{
					name: "Account Setting",
					component: AccountSetting,
					path: 'admin-profile-settings'
				},
				{
					name: "Address",
					path: 'admin-profile-address'
				},
				{
					name: "Notifications"
				},
				{
					name: "Documents"
				}
			])

			provide('tabs', tabs)
			const selectedTab = ref('Account Setting');

			function changeTab(value ) {
				
				selectedTab.value = value
				const tab = tabs.value.find(item => item.name === value );

				router.push({name: tab.path})
			}

			const tab = computed(() => {
				return tabs.value.find(item => item.name === selectedTab.value) 
			})

			return {
				selectedTab,
				changeTab,
				tab
			}

		}
	}
</script>


<template>
	<div>
		<div class="grid lg:grid-cols-6 gap-6">
			<div class="lg:col-span-2">
				<div  class="  rounded-xl bg-white shadow-md">
					<User>
						
					</User>
				</div>
			</div>

			<div class="lg:col-span-4">
				<div class="bg-white border p-4 overflow-x-hidden  lg:p-6 rounded-xl shadow-md">
					
					<Tabs @tabSelect="changeTab" >
						
					</Tabs>
					<hr class="border border-gray-100">
						<div class="mt-6">
							<router-view>
							
							</router-view>
						</div>
					
				</div>
				
			</div>
		</div>
	</div>
</template>