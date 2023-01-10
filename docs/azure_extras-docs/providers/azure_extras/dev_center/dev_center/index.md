---
title: dev_center
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_center
  - dev_center
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>dev_center</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.dev_center</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the devcenter. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DevCenters_Get` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Gets a devcenter. |
| `DevCenters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all devcenters in a resource group. |
| `DevCenters_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all devcenters in a subscription. |
| `DevCenters_CreateOrUpdate` | `INSERT` | `devCenterName, resourceGroupName, subscriptionId` | Creates or updates a devcenter resource |
| `DevCenters_Delete` | `DELETE` | `devCenterName, resourceGroupName, subscriptionId` | Deletes a devcenter |
| `DevCenters_Update` | `EXEC` | `devCenterName, resourceGroupName, subscriptionId` | Partially updates a devcenter. |
