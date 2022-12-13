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
| `tags` | `object` | Resource tags. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Class representing the Kusto pool properties. |
| `sku` | `object` | Azure SKU definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `KustoPools_Get` | `SELECT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Gets a Kusto pool. |
| `KustoPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all Kusto pools |
| `KustoPools_CreateOrUpdate` | `INSERT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__sku` | Create or update a Kusto pool. |
| `KustoPools_Delete` | `DELETE` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Deletes a Kusto pool. |
| `KustoPools_AddLanguageExtensions` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Add a list of language extensions that can run within KQL queries. |
| `KustoPools_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the kusto pool name is valid and is not already in use. |
| `KustoPools_DetachFollowerDatabases` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__attachedDatabaseConfigurationName, data__clusterResourceId` | Detaches all followers of a database owned by this Kusto Pool. |
| `KustoPools_ListFollowerDatabases` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool. |
| `KustoPools_ListLanguageExtensions` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns a list of language extensions that can run within KQL queries. |
| `KustoPools_ListSkus` | `EXEC` | `subscriptionId` | Lists eligible SKUs for Kusto Pool resource. |
| `KustoPools_ListSkusByResource` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the SKUs available for the provided resource. |
| `KustoPools_RemoveLanguageExtensions` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Remove a list of language extensions that can run within KQL queries. |
| `KustoPools_Start` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Starts a Kusto pool. |
| `KustoPools_Stop` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Stops a Kusto pool. |
| `KustoPools_Update` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Update a Kusto Kusto Pool. |
