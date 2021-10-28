import {reactive} from 'vue'


interface ProfileModel {
	photo: String,
	firstname: String,
	lastname:String,
	birth: String,
	gender: String,
	user: Number,
}

interface UserModel {
	email: String,
	id: Number,
	is_staff: Boolean,
}

const User = reactive({
	user: null
})

export default User