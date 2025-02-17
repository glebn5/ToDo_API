<template>
    <div>
      <h1>Login</h1>
      <form @submit.prevent="handlerLogin">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
    </div>
</template>

<script>
import axios from 'axios';
import VueCookies from 'vue-cookies';


export default {
    data() {
        return {
            username: '',
            password: '',
        };
    }, 
    methods: {
        async handlerLogin() {
            try {
                const response = await axios.post('http://127.0.0.1:8000/api/token/', {
                    username: this.username,
                    password: this.password,
                }, { withCredentials: true });

                VueCookies.set('access_token', response.data.access, '360m');
                VueCookies.set('refresh_token', response.data.refresh, '1d'); 

                alert('Login Successful!');
                this.$router.push('/');
            } catch (error) {
                console.error (error);  
                alert('Login failed!');
            }
        }
    }
}
</script>