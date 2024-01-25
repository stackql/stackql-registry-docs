---
title: network_device_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - network_device_skus
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_device_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_device_skus</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkDeviceSkuName, subscriptionId` | Get a Network Device SKU details. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List Network Device SKUs for the given subscription. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List Network Device SKUs for the given subscription. |
