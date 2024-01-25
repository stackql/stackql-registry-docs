---
title: virtual_networks_ddos_protection_status
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_ddos_protection_status
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_networks_ddos_protection_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_networks_ddos_protection_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | The URL to get the next set of results. |
| `value` | `array` | The Ddos Protection Status Result for each public ip under a virtual network. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` |
