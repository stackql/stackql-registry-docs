---
title: managed_clusters_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_outbound_network_dependencies_endpoints
  - aks
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
<tr><td><b>Name</b></td><td><code>managed_clusters_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.aks.managed_clusters_outbound_network_dependencies_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `category` | `string` | The category of endpoints accessed by the AKS agent node, e.g. azure-resource-management, apiserver, etc. |
| `endpoints` | `array` | The endpoints that AKS agent nodes connect to |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
