---
title: diagnostics_packages
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostics_packages
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>diagnostics_packages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.diagnostics_packages</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified diagnostics package. |
| `list_by_packet_core_control_plane` | `SELECT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Lists all the diagnostics packages under a packet core control plane. |
| `create_or_update` | `INSERT` | `diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Creates or updates a diagnostics package. |
| `delete` | `DELETE` | `diagnosticsPackageName, packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Deletes the specified diagnostics package. |
| `_list_by_packet_core_control_plane` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Lists all the diagnostics packages under a packet core control plane. |
