---
title: sims
hide_title: false
hide_table_of_contents: false
keywords:
  - sims
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>sims</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.sims</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | SIM properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Sims_Get` | `SELECT` | `resourceGroupName, simGroupName, simName, subscriptionId` | Gets information about the specified SIM. |
| `Sims_ListBySimGroup` | `SELECT` | `resourceGroupName, simGroupName, subscriptionId` | Gets all the SIMs in a SIM group. |
| `Sims_CreateOrUpdate` | `INSERT` | `resourceGroupName, simGroupName, simName, subscriptionId, data__properties` | Creates or updates a SIM. |
| `Sims_Delete` | `DELETE` | `resourceGroupName, simGroupName, simName, subscriptionId` | Deletes the specified SIM. |
