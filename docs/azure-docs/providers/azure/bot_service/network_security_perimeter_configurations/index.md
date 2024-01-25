---
title: network_security_perimeter_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configurations
  - bot_service
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
<tr><td><b>Id</b></td><td><code>azure.bot_service.network_security_perimeter_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the resource |
| `name` | `string` | Name of the resource |
| `properties` | `object` | Properties of Network Security Perimeter configuration |
| `type` | `string` | Type of the resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId` | Gets the specified Network Security Perimeter configuration associated with the Bot. |
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List Network Security Perimeter configurations associated with the Bot. |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List Network Security Perimeter configurations associated with the Bot. |
| `reconcile` | `EXEC` | `networkSecurityPerimeterConfigurationName, resourceGroupName, resourceName, subscriptionId` | Reconcile the specified Network Security Perimeter configuration associated with the Bot. |
