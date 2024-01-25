---
title: dpp_resource_guard_proxy
hide_title: false
hide_table_of_contents: false
keywords:
  - dpp_resource_guard_proxy
  - data_protection
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
<tr><td><b>Name</b></td><td><code>dpp_resource_guard_proxy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.dpp_resource_guard_proxy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | ResourceGuardProxyBase object, used in ResourceGuardProxyBaseResource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` |
| `delete` | `DELETE` | `resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` |
| `unlock_delete` | `EXEC` | `resourceGroupName, resourceGuardProxyName, subscriptionId, vaultName` |
