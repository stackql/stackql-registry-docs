---
title: internal_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_networks
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
<tr><td><b>Name</b></td><td><code>internal_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.internal_networks</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | Gets a InternalNetworks. |
| `list_by_l3_isolation_domain` | `SELECT` | `l3IsolationDomainName, resourceGroupName, subscriptionId` | Displays InternalNetworks list by resource group GET method. |
| `create` | `INSERT` | `internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties` | Creates InternalNetwork PUT method. |
| `delete` | `DELETE` | `internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | Implements InternalNetworks DELETE method. |
| `_list_by_l3_isolation_domain` | `EXEC` | `l3IsolationDomainName, resourceGroupName, subscriptionId` | Displays InternalNetworks list by resource group GET method. |
| `update` | `EXEC` | `internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | Updates a InternalNetworks. |
