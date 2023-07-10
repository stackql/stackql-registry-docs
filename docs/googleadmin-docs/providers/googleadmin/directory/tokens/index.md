---
title: tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - tokens
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.tokens</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `anonymous` | `boolean` | Whether the application is registered with Google. The value is `true` if the application has an anonymous Client ID. |
| `clientId` | `string` | The Client ID of the application the token is issued to. |
| `displayText` | `string` | The displayable name of the application the token is issued to. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | The type of the API resource. This is always `admin#directory#token`. |
| `nativeApp` | `boolean` | Whether the token is issued to an installed application. The value is `true` if the application is installed to a desktop or mobile device. |
| `scopes` | `array` | A list of authorization scopes the application is granted. |
| `userKey` | `string` | The unique ID of the user that issued the token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clientId, userKey` | Gets information about an access token issued by a user. |
| `list` | `SELECT` | `userKey` | Returns the set of tokens specified user has issued to 3rd party applications. |
| `delete` | `DELETE` | `clientId, userKey` | Deletes all access tokens issued by a user for an application. |
