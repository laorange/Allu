if (parent.callback) {
    //如果是在子框架内就把首页刷新
    parent.callback();
}
var loginApp = new Vue({
    el: '.login-main',
    data: {
        username: '',
        password: '',
        loading: false
    },
    methods: {
        login: function () {
            this.loading = true;
            if (this.username === "" || this.password === "") {
                this.$message.error("Please enter your username or password!");
                this.loading = false;
                return;
            }
            this.$nextTick(function () {
                axios({
                    method: 'post',
                    url: "/dj-rest-auth/login/",
                    data: {
                        username: this.username,
                        password: this.password
                    }
                }).then(
                    response => {
                        console.log("请求API", response.data);
                        if (response.data.key) {
                            localStorage.setItem("dj-rest-auth-token", response.data.key)
                        } 
                        // else {
                        //     console.warn(response.data);
                        // }
                    },
                    error => {
                        console.warn(error.message);
                    },
                );
                document.getElementById('login-form').submit();
            });
        }
    }
});