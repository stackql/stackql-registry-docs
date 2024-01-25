---
title: deleted_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - deleted_workspaces
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>deleted_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.deleted_workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | The etag of the workspace. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Workspace properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Gets recently deleted workspaces in a subscription, available for recovery. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets recently deleted workspaces in a resource group, available for recovery. |
| `_list` | `EXEC` | `subscriptionId` | Gets recently deleted workspaces in a subscription, available for recovery. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets recently deleted workspaces in a resource group, available for recovery. |
