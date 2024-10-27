# wanna-login

## Write-up

- Get page source code and you will find an route to get a hint on `/hint` endpoint.
- Put anything in username that is not equal to "guest" to satisfy the first condition.
- For password use the value `null` which will cause the assertion of `valid_user` to pass as giving a non existing user will eval `users_db.get(user['username'])` clause to return `null` which means they're equal and the condition is satisfied
- You also need to set the value of `flag` to be true so everything passes 
> This is the JSON injection payload for the password field `", "password": null, "flag": true, "x": "x`.


## Flag

`shellmates{4wh_GAwD_jS0N_INJeCt1oN_M44A44N}`
