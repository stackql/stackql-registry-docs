---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a secret. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Get secret. |
| `list` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId, userName` | List secrets in a given user profile. |
| `create_or_update` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName, data__properties` | Create or replace an existing secret. This operation can take a while to complete. |
| `delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Delete secret. |
| `_list` | `EXEC` | `api-version, labName, resourceGroupName, subscriptionId, userName` | List secrets in a given user profile. |
| `update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Allows modifying tags of secrets. All other properties will be ignored. |
