new Vue({
    el: '#app',
    data: {
        score: 10,
        award: false,
        raffle: false,
        integral: 0
    },
    methods: {}
    ,
    created() {
// 发送 ajax 请求
        axios.get('/score_api/').then(response => {
            // console.log(response.data) // 得到返回结果数据
            this.score = response.data.score
            this.award = response.data.award
            this.raffle = response.data.raffle
            this.integral = response.data.integral
        }).catch(error => {
            console.log(error.message)
        })
    },
})