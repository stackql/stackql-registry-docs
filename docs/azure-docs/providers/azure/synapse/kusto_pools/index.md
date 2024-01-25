---
title: kusto_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>kusto_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Class representing the Kusto pool properties. |
| `sku` | `object` | Azure SKU definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Gets a Kusto pool. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all Kusto pools |
| `create_or_update` | `INSERT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__sku` | Create or update a Kusto pool. |
| `delete` | `DELETE` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Deletes a Kusto pool. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List all Kusto pools |
| `add_language_extensions` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Add a list of language extensions that can run within KQL queries. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the kusto pool name is valid and is not already in use. |
| `detach_follower_databases` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__attachedDatabaseConfigurationName, data__clusterResourceId` | Detaches all followers of a database owned by this Kusto Pool. |
| `remove_language_extensions` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Remove a list of language extensions that can run within KQL queries. |
| `start` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Starts a Kusto pool. |
| `stop` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Stops a Kusto pool. |
| `update` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Update a Kusto Kusto Pool. |
