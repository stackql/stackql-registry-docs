---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - dev_test_labs
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a lab user profile. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Get user profile. |
| `list` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId` | List user profiles in a given lab. |
| `create_or_update` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId` | Create or replace an existing user profile. This operation can take a while to complete. |
| `delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId` | Delete user profile. This operation can take a while to complete. |
| `_list` | `EXEC` | `api-version, labName, resourceGroupName, subscriptionId` | List user profiles in a given lab. |
| `update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId` | Allows modifying tags of user profiles. All other properties will be ignored. |
