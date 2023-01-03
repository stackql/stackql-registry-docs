---
title: user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>okta.usertype.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `createdBy` | `string` |
| `displayName` | `string` |
| `default` | `boolean` |
| `_links` | `object` |
| `created` | `string` |
| `lastUpdatedBy` | `string` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `typeId` | Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type. |
| `list` | `SELECT` |  | Fetches all User Types in your org |
| `insert` | `INSERT` |  | Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10. |
| `delete` | `DELETE` | `typeId` | Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users |
| `partialUpdate` | `EXEC` | `typeId` | Updates an existing User Type |
| `update` | `EXEC` | `typeId` | Replace an existing User Type |
