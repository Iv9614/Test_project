import React from  "react";
import GoogleLogin from "react-google-login";


export const SocialLogin = () => {
    const responseGoogle = (response) => {
      console.log(response)
      // send request to backend
    };
    return (
      <>
        <GoogleLogin
          clientId="<CLIENT_ID>.apps.googleusercontent.com"
          buttonText="使用 Google 登入"
          onSuccess={responseGoogle}
          onFailure={responseGoogle}
          cookiePolicy={"single_host_origin"}
        />
      </>
    );
  };