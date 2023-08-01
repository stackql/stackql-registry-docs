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
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | ContainerApp resource specific properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ContainerApps_Get` | `SELECT` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `ContainerApps_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `ContainerApps_ListBySubscription` | `SELECT` | `subscriptionId` |  |
| `ContainerApps_CreateOrUpdate` | `INSERT` | `containerAppName, resourceGroupName, subscriptionId` | Create or update a Container App. |
| `ContainerApps_Delete` | `DELETE` | `containerAppName, resourceGroupName, subscriptionId` | Delete a Container App. |
| `ContainerApps_ListCustomHostNameAnalysis` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `ContainerApps_ListSecrets` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` |  |
| `ContainerApps_Update` | `EXEC` | `containerAppName, resourceGroupName, subscriptionId` | Patches a Container App using JSON Merge Patch |
