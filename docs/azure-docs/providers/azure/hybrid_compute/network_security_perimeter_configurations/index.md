---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.network_security_perimeter_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `properties` | `object` | Properties that define a Network Security Perimeter resource. |
| `type` | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_private_link_scope` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` | Lists the network security perimeter configurations for a private link scope. |
| `_list_by_private_link_scope` | `EXEC` | `resourceGroupName, scopeName, subscriptionId` | Lists the network security perimeter configurations for a private link scope. |
| `get_by_private_link_scope` | `EXEC` | `perimeterName, resourceGroupName, scopeName, subscriptionId` | Gets the network security perimeter configuration for a private link scope. |
| `reconcile_for_private_link_scope` | `EXEC` | `perimeterName, resourceGroupName, scopeName, subscriptionId` | Forces the network security perimeter configuration to refresh for a private link scope. |
