---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - session
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
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
| `idp` | `object` |
| `lastPasswordVerification` | `string` |
| `expiresAt` | `string` |
| `status` | `string` |
| `login` | `string` |
| `_links` | `object` |
| `lastFactorVerification` | `string` |
| `amr` | `array` |
| `createdAt` | `string` |
| `userId` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `sessionId, subdomain` | Get details about a session. |
| `insert` | `INSERT` | `subdomain` | Creates a new session for a user with a valid session token. Use this API if, for example, you want to set the session cookie yourself instead of allowing Okta to set it, or want to hold the session ID in order to delete a session via the API instead of visiting the logout URL. |
| `delete` | `DELETE` | `sessionId, subdomain` |  |
| `refresh` | `EXEC` | `sessionId, subdomain` |  |
