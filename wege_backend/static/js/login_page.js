/**This async function carryout JWT authentication process to enable JWT based authorization access
 * @params: None
 * @returns: None*/

async function login_request() {
  const form_ele = document.forms.login_form;
  const login_info = {
    username: form_ele.username.value,
    password: form_ele.password.value,
  };
  const request_jwt_token = await fetch("new_token", {
    method: "POST",
    body: JSON.stringify(login_info),
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  });

  const response = await request_jwt_token.json();
  if (response["access"]) {
    window.alert("Your Successfully loggedin!!!");
    document.cookie = `access_token=${response.access}`;
    document.cookie = `refresh_token=${response.refresh}`;
  
    const get_userinfo = await fetch("get_userinfo_api", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Bearer ${response.access}`, //jwt access token added in header
      },
      body: JSON.stringify({ username: login_info.username }),
    });
    
    const response_get_userinfo = await get_userinfo.json();
    if (response_get_userinfo["detail"]) {
      window.alert(response_get_userinfo["detail"]);
    }
    else {
      alert(JSON.stringify(response_get_userinfo));
      window.location.href = "home";
    }
  }
  else {
    window.alert(response["detail"]);
  }
}
