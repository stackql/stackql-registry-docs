---
title: server_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - server_groups
  - postgresql_hsc
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
<tr><td><b>Name</b></td><td><code>server_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql_hsc.server_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties used to create a new server group. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerGroups_Get` | `SELECT` | `resourceGroupName, serverGroupName, subscriptionId` | Gets information about a server group. |
| `ServerGroups_List` | `SELECT` | `subscriptionId` | List all the server groups in a given subscription. |
| `ServerGroups_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the server groups in a given resource group. |
| `ServerGroups_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverGroupName, subscriptionId` | Creates a new server group with servers. |
| `ServerGroups_Delete` | `DELETE` | `resourceGroupName, serverGroupName, subscriptionId` | Deletes a server group together with servers in it. |
| `ServerGroups_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Check the availability of name for resource |
| `ServerGroups_Restart` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Restarts the server group. |
| `ServerGroups_Start` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Starts the server group. |
| `ServerGroups_Stop` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Stops the server group. |
| `ServerGroups_Update` | `EXEC` | `resourceGroupName, serverGroupName, subscriptionId` | Updates an existing server group. The request body can contain one to many of the properties present in the normal server group definition. |
