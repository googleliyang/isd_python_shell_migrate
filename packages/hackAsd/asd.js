import api from '../../api'
import config from './data'


export default {

     awaitWrap: (promise) =>  promise.then(data => [null, data]).catch(err => [err, null]),


    // 加密
    addSign: function(data) {
        return new Promise((resolve, rej) => {
            let token
            if (config.IS_NEED_TOKEN) {
                token = this.getUserInfo().token
                if (!token) {
                    return rej('Token is empty')
                }
            }

            api.post('isdCommonSearch/isdTool/encryptParam', {
                token,
                param: JSON.stringify(data),
            }, {}, false).then(res => {

                if (res.data && res.data.message) {
                    // console.log(res.data.message)
                    resolve(res.data.message)
                } else {
                    rej('获取加密数据失败!')
                }

            }).catch(err => {
                rej(err)
            })
        })
    },


    // 初始化 token 和 用户信息
    fetchTokenAndUserInfo(data) {
         return api.post('isdCommonSearch/token/getToken', data, {}, false)
    },


    setUserInfo(data) {
        data = JSON.stringify(data)
        return localStorage.setItem(config.LOCALSTORAGE_KEY.USERINFO_KEY, data)
    },

    getUserInfo() {
        let res = localStorage.getItem(config.LOCALSTORAGE_KEY.USERINFO_KEY)
        return res ? JSON.parse(res) : null
    }

}
