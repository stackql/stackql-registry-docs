---
title: workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces
  - iot_firmware_defense
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
<tr><td><b>Name</b></td><td><code>workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_firmware_defense.workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Workspace properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get firmware analysis workspace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the firmware analysis workspaces in the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all of the firmware analysis workspaces in the specified subscription. |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | The operation to create or update a firmware analysis workspace. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | The operation to delete a firmware analysis workspace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all of the firmware analysis workspaces in the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all of the firmware analysis workspaces in the specified subscription. |
| `generate_upload_url` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | The operation to get a url for file upload. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | The operation to update a firmware analysis workspaces. |
