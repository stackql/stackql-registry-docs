---
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
  - container_apps
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
<tr><td><b>Name</b></td><td><code>container_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_apps.container_apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `managedBy` | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| `properties` | `object` | ContainerApp resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `list_by_subscription` | `SELECT` | `subscriptionId` |  |
| `create_or_update` | `INSERT` | `containerAppName, resourceGroupName, subscriptionId` | Create or update a Container App. |
| `delete` | `DELETE` | `containerAppName, resourceGroupName, subscriptionId` | Delete a Container App. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |  |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |  |
| `start` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `stop` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` | Patches a Container App using JSON Merge Patch |
