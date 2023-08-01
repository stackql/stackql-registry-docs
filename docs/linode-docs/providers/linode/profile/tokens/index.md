---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - profile
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.profile.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This token's unique ID, which can be used to revoke it.<br /> |
| `label` | `string` | This token's label.  This is for display purposes only, but can be used to more easily track what you're using each token for.<br /> |
| `scopes` | `string` | The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the &lt;a target="_top" href="https://github.com/linode/linode-cli"&gt;Linode CLI&lt;/a&gt;, require tokens with access to `*`. Tokens with more restrictive scopes are generally more secure.<br /> |
| `token` | `string` | The token used to access the API.  When the token is created, the full token is returned here.  Otherwise, only the first 16 characters are returned.<br /> |
| `created` | `string` | The date and time this token was created.<br /> |
| `expiry` | `string` | When this token will expire.  Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated.  Tokens may be created with "null" as their expiry and will never expire unless revoked.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getPersonalAccessToken` | `SELECT` | `tokenId` | Returns a single Personal Access Token.<br /> |
| `getPersonalAccessTokens` | `SELECT` |  | Returns a paginated list of Personal Access Tokens currently active for your User.<br /> |
| `createPersonalAccessToken` | `INSERT` |  | Creates a Personal Access Token for your User. The raw token will be returned in the response, but will never be returned again afterward so be sure to take note of it. You may create a token with _at most_ the scopes of your current token. The created token will be able to access your Account until the given expiry, or until it is revoked.<br /> |
| `deletePersonalAccessToken` | `DELETE` | `tokenId` | Revokes a Personal Access Token. The token will be invalidated immediately, and requests using that token will fail with a 401. It is possible to revoke access to the token making the request to revoke a token, but keep in mind that doing so could lose you access to the api and require you to create a new token through some other means.<br /> |
| `_getPersonalAccessToken` | `EXEC` | `tokenId` | Returns a single Personal Access Token.<br /> |
| `_getPersonalAccessTokens` | `EXEC` |  | Returns a paginated list of Personal Access Tokens currently active for your User.<br /> |
| `updatePersonalAccessToken` | `EXEC` | `tokenId` | Updates a Personal Access Token.<br /> |
