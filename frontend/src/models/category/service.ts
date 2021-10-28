import axios from 'axios';

class CategoryService {

	async get_all(): Promise<any> {
		return new Promise((resolve, reject) => {
			axios.get('categories/')
			.then((resp) => {
				resolve(resp)
			})
			.catch((err) => {
				console.log(err)
			})
		})
	}
}


export default new CategoryService