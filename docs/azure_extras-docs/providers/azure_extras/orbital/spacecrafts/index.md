---
title: spacecrafts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts
  - orbital
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
<tr><td><b>Name</b></td><td><code>spacecrafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.orbital.spacecrafts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | List of Spacecraft Resource Properties. |
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Spacecrafts_Get` | `SELECT` | `resourceGroupName, spacecraftName, subscriptionId` | Gets the specified spacecraft in a specified resource group. |
| `Spacecrafts_List` | `SELECT` | `resourceGroupName, subscriptionId` | Returns list of spacecrafts by resource group. |
| `Spacecrafts_ListBySubscription` | `SELECT` | `subscriptionId` | Returns list of spacecrafts by subscription. |
| `Spacecrafts_CreateOrUpdate` | `INSERT` | `resourceGroupName, spacecraftName, subscriptionId` | Creates or updates a spacecraft resource. |
| `Spacecrafts_Delete` | `DELETE` | `resourceGroupName, spacecraftName, subscriptionId` | Deletes a specified spacecraft resource. |
| `Spacecrafts_ListAvailableContacts` | `EXEC` | `resourceGroupName, spacecraftName, subscriptionId, data__contactProfile, data__endTime, data__groundStationName, data__startTime` | Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile. |
| `Spacecrafts_UpdateTags` | `EXEC` | `resourceGroupName, spacecraftName, subscriptionId` | Updates the specified spacecraft tags. |
