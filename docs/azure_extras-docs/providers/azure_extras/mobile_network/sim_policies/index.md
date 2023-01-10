---
title: sim_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sim_policies
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
<tr><td><b>Name</b></td><td><code>sim_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.sim_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | SIM policy properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SimPolicies_Get` | `SELECT` | `mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId` | Gets information about the specified SIM policy. |
| `SimPolicies_ListByMobileNetwork` | `SELECT` | `mobileNetworkName, resourceGroupName, subscriptionId` | Gets all the SIM policies in a mobile network. |
| `SimPolicies_CreateOrUpdate` | `INSERT` | `mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId, data__properties` | Creates or updates a SIM policy. |
| `SimPolicies_Delete` | `DELETE` | `mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId` | Deletes the specified SIM policy. |
| `SimPolicies_UpdateTags` | `EXEC` | `mobileNetworkName, resourceGroupName, simPolicyName, subscriptionId` | Updates SIM policy tags. |
