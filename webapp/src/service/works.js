import request from '../utils/axios'

export function getWork(data) {
  return request({
      url: "/work",
      method: "get",
      data,
  });
}

export function deleteWork(data) {
  return request({
      url: "/work",
      method: "delete",
      data,
  });
}

export function getWorkByID(data) {
  return request({
      url: "/work/ById",
      method: "put",
      data,
  });
}

