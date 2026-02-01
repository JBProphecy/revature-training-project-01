
---
# When using cookies...

The cookies (access token and refresh token cookies) will be sent with every request. When the access token expires, I can refresh the tokens without having to send a new request. Additionally, I don't need to send back any tokens in the response body... I only need to set the cookies and it's a done deal.

---
# When using headers...

I need to set the access token in an authorization header with each request that needs it. When the access token expires, I won't have the refresh token on hand, so I would need to send another request to an endpoint like /auth/refresh to refresh the tokens. The response body of that request would include the new tokens, which I would need to store somewhere on the device, like the keystore or whatever it's called on mobile with React Native. So the first request would get denied (401 I think, but I would customize it), the second request would refresh the tokens, and the next request would be the same as the first, except it should work that time as long as the tokens were successfully refreshed in the second request. I would not need to send back tokens in the response body for the requests that aren't the refresh endpoint, as those locations aren't where the refresh is happening.

---
# Choosing between them...

My answer is simple... I want to use cookies for the web and headers for mobile devices.

---
# Using the same backend...

I want to be able to use the same backend whether I'm using web or mobile. I should be able to do that with relatively no issues, but authorization is one of those things that I would need to handle differently. For web, my tokens would be sent in cookies. For mobile, my access token would be sent in a header.

I could have a custom header called "x-auth-method" with a value of "cookies" or "header".

---
# Authorization Middleware

I need to create a middleware handler that can handle both methods of authorization depending on the authorization method defined in my custom header x-auth-method.

The response from this middleware handler should be the same for both methods. The difference in how the response is handled depends on the frontend. For the mobile versions, I can try to refresh the tokens if they are expired and then retry the original route. For the web versions, I should probably just do it the same way even though I don't really have to make a separate request to refresh the cookies.

---

**Account Authorization Response Body**

code: 401
type: "unauthorized-header"
status: "undefined" | "invalid"
message: "Missing Header for Authorization Method"
solution: "Define a header called "x-auth-method" with a value of "cookies" or "header"."

message: "Invalid Header for Authorization Method"
solution: "The value of x-auth-method must be "cookie" or "header"."

code: 401
type: "unauthorized-account"
status: "expired" | "invalid" | "undefined"
message: "Your access token is expired."

---

requestCreateProfileViaCookies({ body })
requestCreateProfileViaStorage({ accessToken, body })

requestRefreshAccountTokensViaStorage({ refreshToken })

---

**Refresh Account Tokens Response Body**

code: 200
type: "success"
message: "Your account tokens have been refreshed."

code : 401
type: "failure"
status: "expired" | "invalid" | "undefined"
message: "Your refresh token is expired."

---
