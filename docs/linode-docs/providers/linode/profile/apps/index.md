---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.profile.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This authorization's ID, used for revoking access.<br /> |
| `expiry` | `string` | When the app's access to your account expires. If `null`, the app's access must be revoked manually.<br /> |
| `label` | `string` | The name of the application you've authorized.<br /> |
| `scopes` | `string` | The OAuth scopes this app was authorized with.  This defines what parts of your Account the app is allowed to access.<br /> |
| `thumbnail_url` | `string` | The URL at which this app's thumbnail may be accessed.<br /> |
| `website` | `string` | The website where you can get more information about this app.<br /> |
| `created` | `string` | When this app was authorized. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getProfileApp` | `SELECT` | `appId` | Returns information about a single app you've authorized to access your Account.<br /> |
| `getProfileApps` | `SELECT` |  | This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /> |
| `deleteProfileApp` | `DELETE` | `appId` | Expires this app token. This token may no longer be used to access your Account.<br /> |
| `_getProfileApp` | `EXEC` | `appId` | Returns information about a single app you've authorized to access your Account.<br /> |
| `_getProfileApps` | `EXEC` |  | This is a collection of OAuth apps that you've given access to your Account, and includes the level of access granted.<br /> |
