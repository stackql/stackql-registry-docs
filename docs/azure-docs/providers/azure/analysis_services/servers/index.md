---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - analysis_services
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
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.analysis_services.servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the Analysis Services resource. |
| `name` | `string` | The name of the Analysis Services resource. |
| `location` | `string` | Location of the Analysis Services resource. |
| `properties` | `object` | Properties of Analysis Services resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the Analysis Services resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `subscriptionId` | Lists all the Analysis Services servers for the given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Analysis Services servers for the given resource group. |
| `create` | `INSERT` | `resourceGroupName, serverName, subscriptionId` | Provisions the specified Analysis Services server based on the configuration specified in the request. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId` | Deletes the specified Analysis Services server. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the Analysis Services servers for the given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the Analysis Services servers for the given resource group. |
| `check_name_availability` | `EXEC` | `location, subscriptionId` | Check the name availability in the target location. |
| `dissociate_gateway` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Dissociates a Unified Gateway associated with the server. |
| `resume` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Resumes operation of the specified Analysis Services server instance. |
| `suspend` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Suspends operation of the specified Analysis Services server instance. |
| `update` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Updates the current state of the specified Analysis Services server. |
