---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - usertype
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
| `created` | `string` |
| `displayName` | `string` |
| `createdBy` | `string` |
| `default` | `boolean` |
| `lastUpdatedBy` | `string` |
| `_links` | `object` |
| `lastUpdated` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `typeId, subdomain` | Fetches a User Type by ID. The special identifier `default` may be used to fetch the default User Type. |
| `list` | `SELECT` | `subdomain` | Fetches all User Types in your org |
| `insert` | `INSERT` | `subdomain` | Creates a new User Type. A default User Type is automatically created along with your org, and you may add another 9 User Types for a maximum of 10. |
| `delete` | `DELETE` | `typeId, subdomain` | Deletes a User Type permanently. This operation is not permitted for the default type, nor for any User Type that has existing users |
| `partialUpdate` | `EXEC` | `typeId, subdomain` | Updates an existing User Type |
| `update` | `EXEC` | `typeId, subdomain` | Replace an existing User Type |
