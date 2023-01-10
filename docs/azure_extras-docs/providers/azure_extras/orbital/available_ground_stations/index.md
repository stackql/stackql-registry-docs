---
title: available_ground_stations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_ground_stations
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
<tr><td><b>Name</b></td><td><code>available_ground_stations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.orbital.available_ground_stations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of groundStation. |
| `name` | `string` | Name of the ground station. |
| `properties` | `object` | The properties bag for this resource. |
| `type` | `string` | Resource type. |
| `location` | `string` | Azure region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AvailableGroundStations_Get` | `SELECT` | `groundStationName, subscriptionId` | Gets the specified available ground station. |
| `AvailableGroundStations_ListByCapability` | `SELECT` | `capability, subscriptionId` | Returns list of available ground stations. |
