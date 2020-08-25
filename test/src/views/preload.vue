<template>
    <div> </div>
</template>

<script>
    import asd from "../../utils/hackAsd/asd";
    import lightAppJssdkUtil from "../../utils/lightAppJssdk.util";
    import config from '../../utils/hackAsd/data'

    export default {

        mounted() {
            this.init()
        },

        data() {
            return {}
        },
        methods: {
            async init() {
                this.$toast.loading({
                    duration: 0,
                    message: '加载中，请稍后...',
                    className: 'loading',
                })
                try {
                    const [err, res] = await asd.awaitWrap(lightAppJssdkUtil.getTicket())
                    this.ticketInfo = JSON.parse(res);
                    // this.userInfo = res
                    if (err) throw (err)
                    let ticket = JSON.parse(this.ticketInfo.data).ticket
                    if (!ticket) throw ('ticket 获取失败')
                    console.log('获取 ticket 为', ticket)
                    const [uerr, userInfo] = await asd.awaitWrap(asd.fetchTokenAndUserInfo({
                        ticket: ticket
                    },))
                    if (uerr) throw (uerr)
                    // if success , set to localstorage
                    console.log('用户信息为' , userInfo)
                    asd.setUserInfo(userInfo.data)
                    this.$toast.clear()
                    this.toIndex()

                } catch (e) {
                    this.$toast.clear()
                    console.error('错误为', e)
                    this.$toast.fail('获取信息失败, 请退出重新打开')
                    // window.location.reload()
                }

            },
            toIndex() {
                this.$router.replace({path: config.AFTER_LOADING_TO_PATH})
                // setTimeout(()=> {
                // }, 2000)
            }
        }
    }
</script>
<style lang="scss" scoped>
    .href-router {
        display: block;
        font-size: 18px;
        text-align: center;
        color: #0095ff;
        text-decoration-line: underline;
    }
</style>

<style>

    .loading {
        width: auto;
        max-width: 200px;
    }

</style>
