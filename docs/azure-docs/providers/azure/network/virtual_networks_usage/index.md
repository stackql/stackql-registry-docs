---
title: virtual_networks_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_usage
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
<tr><td><b>Name</b></td><td><code>virtual_networks_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_networks_usage</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Subnet identifier. |
| `name` | `object` | Usage strings container. |
| `currentValue` | `number` | Indicates number of IPs used from the Subnet. |
| `limit` | `number` | Indicates the size of the subnet. |
| `unit` | `string` | Usage units. Returns 'Count'. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` |
