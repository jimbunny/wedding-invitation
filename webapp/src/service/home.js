import request from '../utils/axios'

// export function getHome(params) {
//   return axios.get('/index-infos');
// }

export function getTemplateList(data) {
  return request({
      url: "/webapp/templates/getList",
      method: "get",
      params: data,
  });
}

export function getSwipeList(data) {
  return request({
      url: "/webapp/swipes/getList",
      method: "get",
      params: data,
  });
}