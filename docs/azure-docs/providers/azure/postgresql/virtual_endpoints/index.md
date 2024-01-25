---
title: virtual_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_endpoints
  - postgresql
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
<tr><td><b>Name</b></td><td><code>virtual_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.virtual_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of a virtual endpoint. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, virtualEndpointName` | Gets information about a virtual endpoint. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the servers in a given resource group. |
| `create` | `INSERT` | `resourceGroupName, serverName, subscriptionId, virtualEndpointName` | Creates a new virtual endpoint for PostgreSQL flexible server. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId, virtualEndpointName` | Deletes a virtual endpoint. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the servers in a given resource group. |
| `update` | `EXEC` | `resourceGroupName, serverName, subscriptionId, virtualEndpointName` | Updates an existing virtual endpoint. The request body can contain one to many of the properties present in the normal virtual endpoint definition. |
