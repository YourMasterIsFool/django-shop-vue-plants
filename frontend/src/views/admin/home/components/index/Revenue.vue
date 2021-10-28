<script lang="ts">
	import {ref, onMounted} from 'vue';
	import Chart from 'chart.js/auto'


	export default {

		setup() {
			// const chart = ref(null)

			onMounted(() => {
				const chart = document.getElementById("chart").getContext("2d");
				const labels = [
				  'January',
				  'February',
				  'March',
				  'April',
				  'May',
				  'June',
				];
				const data = {
				  labels: labels,
				  datasets: [{
				    label: 'My First dataset',
				    backgroundColor: 'rgb(255, 99, 132)',
				    borderColor: 'rgb(255, 99, 132)',
				    data: [0, 10, 5, 2, 20, 30, 45],
				  }]
				};


				const config = {
					  type: 'line',
					  maintainAspectRatio: false,
					  responsive:true,
					  data: data,
					  options: {}
					};
				const ctx = new Chart(chart, config)
			})


			return {
		
			}
 
		}
	}
</script>

<template>
	<div>
		<div class="mt-6 lg:mt-12">
				<h1 class="text-sm lg:text-lg text-green-800 font-bold capitalize">
					revenue
				</h1>
				<div class="w-full ">
				<canvas ref="chart" id="chart">

				</canvas>
				</div>
			</div>
	</div>
</template>