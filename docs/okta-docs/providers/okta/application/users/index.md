---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - application
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.application.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `credentials` | `object` |
| `status` | `string` |
| `statusChanged` | `string` |
| `passwordChanged` | `string` |
| `externalId` | `string` |
| `lastUpdated` | `string` |
| `scope` | `string` |
| `lastSync` | `string` |
| `profile` | `object` |
| `created` | `string` |
| `syncState` | `string` |
| `_links` | `object` |
| `_embedded` | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appId, userId, subdomain` | Fetches a specific user assignment for application by `id`. |
| `list` | `SELECT` | `appId, subdomain` | Enumerates all assigned [application users](#application-user-model) for an application. |
| `insert` | `INSERT` | `appId, subdomain` | Assigns an user to an application with [credentials](#application-user-credentials-object) and an app-specific [profile](#application-user-profile-object). Profile mappings defined for the application are first applied before applying any profile properties specified in the request. |
| `delete` | `DELETE` | `appId, userId, subdomain` | Removes an assignment for a user from an application. |
| `update` | `EXEC` | `appId, userId, subdomain` | Updates a user's profile for an application |
