---
title: user_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - user_tokens
  - authentication
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.authentication.user_tokens</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_auth_token` | `SELECT` | `tokenId` | Retrieve metadata about an authentication token belonging to the currently authenticated User. |
| `list_auth_tokens` | `SELECT` |  | Retrieve a list of the current User's authentication tokens. |
| `create_auth_token` | `INSERT` | `teamId` | Creates and returns a new authentication token for the currently authenticated User. The `bearerToken` property is only provided once, in the response body, so be sure to save it on the client for use with API requests. |
| `delete_auth_token` | `DELETE` | `tokenId` | Invalidate an authentication token, such that it will no longer be valid for future HTTP requests. |
| `_list_auth_tokens` | `EXEC` |  | Retrieve a list of the current User's authentication tokens. |
| `email_login` | `EXEC` | `data__email` | Request a new login for a user to get a token. This will respond with a verification token and send an email to confirm the request. Once confirmed you can use the verification token to get an authentication token. |
| `verify_token` | `EXEC` | `token` | Verify the user accepted the login request and get a authentication token. The user email address and the token received after requesting the login must be added to the URL as a query string with the names `email` and `token`. |
