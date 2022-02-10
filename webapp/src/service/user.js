import request from '../utils/axios'

// export function getHome(params) {
//   return axios.get('/index-infos');
// }

export function login(data) {
  return request({
      url: "/webapp/login",
      method: "post",
      data,
  });
}

export function register(data) {
  return request({
      url: "/webapp/register",
      method: "post",
      data,
  });
}

export function checkUsername(data) {
  return request({
      url: "/webapp/checkUsername",
      method: "get",
      params: data,
  });
}

export function checkEmail(data) {
  return request({
      url: "/webapp/checkEmail",
      method: "get",
      params: data,
  });
}

export function checkPhone(data) {
  return request({
      url: "/webapp/checkPhone",
      method: "get",
      params: data,
  });
}
export function getUserInfo(data) {
  return request({
      url: "/webapp/userInfo",
      method: "post",
      data,
  });
}

export function EditUserInfo(data) {
  return request({
      url: "/webapp/userInfo",
      method: "put",
      data,
  });
}

export function AddBalanceInfo(data) {
  return request({
      url: "/webapp/balanceInfo",
      method: "post",
      headers: { "Content-Type": "multipart/form-data" },
      data,
      type: "form"
  });
}

export function GetBalanceInfo(data) {
  return request({
      url: "/webapp/balanceInfo",
      method: "get",
      params: data,
  });
}

export function AddPointInfo(data) {
  return request({
      url: "/webapp/pointInfo",
      method: "post",
      data,
  });
}

export function GetPointInfo(data) {
  return request({
      url: "/webapp/pointInfo",
      method: "get",
      params: data,
  });
}

export function validFB(data) {
  return request({
      url: "/webapp/validFB",
      method: "post",
      data,
  });
}

export function validLogin() {
  return request({
      url: "/webapp/validLogin",
      method: "get",
  });
}

export function forgetPassword(data) {
  return request({
      url: "/webapp/forgetPassword",
      method: "post",
      data,
  });
}

export function inviteList(data) {
  return request({
      url: "/webapp/inviteList",
      method: "post",
      data,
  });
}

export function logout() {
  return request({
      url: "/webapp/logout",
      method: "post",
  });
}

// export function getUserInfo() {
//   return axios.get('/user/info');
// }

// export function EditUserInfo(params) {
//   return axios.put('/user/info', params);
// }

// export function login(params) {
//   return axios.post('/user/login', params);
// }

// export function logout() {
//   return axios.post('/user/logout')
// }

// export function register(params) {
//   return axios.post('/user/register', params);
// }

