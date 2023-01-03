---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - users
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.users.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier for the user. |
| `modifiedAt` | `string` | Last modification timestamp in UTC. |
| `isLocked` | `boolean` | This has the value `true` if the user's account has been locked. If a user tries to log into their account several times and fails, his or her account will be locked for security reasons. |
| `modifiedBy` | `string` | Identifier of the user who last modified the resource. |
| `roleIds` | `array` | List of roleIds associated with the user. |
| `createdBy` | `string` | Identifier of the user who created the resource. |
| `firstName` | `string` | First name of the user. |
| `isActive` | `boolean` | True if the user is active. |
| `email` | `string` | Email address of the user. |
| `createdAt` | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `isMfaEnabled` | `boolean` | True if multi factor authentication is enabled for the user. |
| `lastLoginTimestamp` | `string` | Timestamp of the last login for the user in UTC. Will be null if the user has never logged in. |
| `lastName` | `string` | Last name of the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getUser` | `SELECT` | `id` | Get a user with the given identifier from the organization. |
| `listUsers` | `SELECT` |  | Get a list of all users in the organization. The response is paginated with a default limit of 100 users per page. |
| `createUser` | `INSERT` | `data__email, data__firstName, data__lastName, data__roleIds` | Create a new user in the organization. |
| `deleteUser` | `DELETE` | `id` | Delete a user with the given identifier from the organization and transfer their content to the user with the identifier specified in "transferTo". |
| `updateUser` | `EXEC` | `id, data__firstName, data__isActive, data__lastName, data__roleIds` | Update an existing user in the organization. |
