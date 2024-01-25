---
title: external_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - external_networks
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
<tr><td><b>Name</b></td><td><code>external_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.external_networks</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | Implements ExternalNetworks GET method. |
| `list_by_l3_isolation_domain` | `SELECT` | `l3IsolationDomainName, resourceGroupName, subscriptionId` | Implements External Networks list by resource group GET method. |
| `create` | `INSERT` | `externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties` | Creates ExternalNetwork PUT method. |
| `delete` | `DELETE` | `externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | Implements ExternalNetworks DELETE method. |
| `_list_by_l3_isolation_domain` | `EXEC` | `l3IsolationDomainName, resourceGroupName, subscriptionId` | Implements External Networks list by resource group GET method. |
| `update` | `EXEC` | `externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId` | API to update certain properties of the ExternalNetworks resource. |
