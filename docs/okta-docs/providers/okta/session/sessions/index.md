---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - okta
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.session.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `expiresAt` | `string` |
| `login` | `string` |
| `userId` | `string` |
| `createdAt` | `string` |
| `status` | `string` |
| `amr` | `array` |
| `_links` | `object` |
| `lastPasswordVerification` | `string` |
| `idp` | `object` |
| `lastFactorVerification` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `sessionId` | Get details about a session. |
| `insert` | `INSERT` |  | Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL. |
| `delete` | `DELETE` | `sessionId` |  |
| `refresh` | `EXEC` | `sessionId` |  |
