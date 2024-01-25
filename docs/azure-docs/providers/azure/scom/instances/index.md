---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - scom
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.scom.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a SCOM instance resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instanceName, resourceGroupName, subscriptionId` | Get SCOM managed instance details |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all SCOM managed instances in a resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all SCOM managed instances in a subscription  |
| `create_or_update` | `INSERT` | `instanceName, resourceGroupName, subscriptionId` | Create or update SCOM managed instance |
| `delete` | `DELETE` | `instanceName, resourceGroupName, subscriptionId` | Delete a SCOM managed instance |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all SCOM managed instances in a resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all SCOM managed instances in a subscription  |
| `link_log_analytics` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Link Log Analytics workspace for SCOM monitoring instance |
| `patch_servers` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Update SCOM servers with latest scom software. |
| `scale` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Scaling SCOM managed instance. |
| `unlink_log_analytics` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Unlink Log Analytics workspace for SCOM monitoring instance |
| `update` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | Patch SCOM managed instance |
