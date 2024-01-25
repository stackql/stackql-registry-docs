---
title: configuration_policy_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_policy_groups
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
<tr><td><b>Name</b></td><td><code>configuration_policy_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.configuration_policy_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Parameters for VpnServerConfigurationPolicyGroup. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName` | Retrieves the details of a ConfigurationPolicyGroup. |
| `list_by_vpn_server_configuration` | `SELECT` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Lists all the configurationPolicyGroups in a resource group for a vpnServerConfiguration. |
| `create_or_update` | `INSERT` | `configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName` | Creates a ConfigurationPolicyGroup if it doesn't exist else updates the existing one. |
| `delete` | `DELETE` | `configurationPolicyGroupName, resourceGroupName, subscriptionId, vpnServerConfigurationName` | Deletes a ConfigurationPolicyGroup. |
| `_list_by_vpn_server_configuration` | `EXEC` | `resourceGroupName, subscriptionId, vpnServerConfigurationName` | Lists all the configurationPolicyGroups in a resource group for a vpnServerConfiguration. |
