---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
  - container_service
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
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_service.fleets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a Fleet. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Resource Etag. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Fleets_Get` | `SELECT` | `fleetName, resourceGroupName, subscriptionId` |
| `Fleets_List` | `SELECT` | `subscriptionId` |
| `Fleets_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Fleets_CreateOrUpdate` | `INSERT` | `fleetName, resourceGroupName, subscriptionId` |
| `Fleets_Delete` | `DELETE` | `fleetName, resourceGroupName, subscriptionId` |
| `Fleets_ListCredentials` | `EXEC` | `fleetName, resourceGroupName, subscriptionId` |
| `Fleets_Update` | `EXEC` | `fleetName, resourceGroupName, subscriptionId` |
