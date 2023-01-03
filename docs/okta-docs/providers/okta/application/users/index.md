---
title: users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `_links` | `object` |
| `scope` | `string` |
| `status` | `string` |
| `lastSync` | `string` |
| `credentials` | `object` |
| `lastUpdated` | `string` |
| `statusChanged` | `string` |
| `profile` | `object` |
| `syncState` | `string` |
| `externalId` | `string` |
| `created` | `string` |
| `_embedded` | `object` |
| `passwordChanged` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, userId` | Fetches a specific user assignment for application by `id`. |
| `list` | `SELECT` | `appId` | Enumerates all assigned [application users](#application-user-model) for an application. |
| `insert` | `INSERT` | `appId` | Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request. |
| `delete` | `DELETE` | `appId, userId` | Removes an assignment for a user from an application. |
| `update` | `EXEC` | `appId, userId` | Updates a user's profile for an application |
