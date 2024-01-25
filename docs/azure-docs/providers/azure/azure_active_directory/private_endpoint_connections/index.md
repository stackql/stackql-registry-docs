---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - azure_active_directory
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_active_directory.private_endpoint_connections</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `policyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Gets the specified private endpoint connection associated with the given policy. |
| `list_by_policy_name` | `SELECT` | `policyName, resourceGroupName, subscriptionId` | Lists all Private Endpoint Connections for the given policy. |
| `create` | `INSERT` | `policyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Creates specified private endpoint connection associated with the given policy. |
| `delete` | `DELETE` | `policyName, privateEndpointConnectionName, resourceGroupName, subscriptionId` | Deletes the specified private endpoint connection associated with the given policy. |
| `_list_by_policy_name` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Lists all Private Endpoint Connections for the given policy. |
