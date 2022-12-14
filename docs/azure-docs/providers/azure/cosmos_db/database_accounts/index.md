---
title: database_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.database_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique resource identifier of the ARM resource. |
| `name` | `string` | The name of the ARM resource. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of Azure resource. |
| `properties` | `object` | Properties for the database account. |
| `kind` | `string` | Indicates the type of database account. This can only be set at database account creation. |
| `tags` | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| `identity` | `object` | Identity for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseAccounts_Get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB database account. |
| `DatabaseAccounts_List` | `SELECT` | `subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| `DatabaseAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| `DatabaseAccounts_CreateOrUpdate` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account. |
| `DatabaseAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB database account. |
| `DatabaseAccounts_CheckNameExists` | `EXEC` | `accountName` | Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters. |
| `DatabaseAccounts_FailoverPriorityChange` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__failoverPolicies` | Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |
| `DatabaseAccounts_GetReadOnlyKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the read-only access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListConnectionStrings` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the connection strings for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListMetricDefinitions` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves metric definitions for the given database account. |
| `DatabaseAccounts_ListMetrics` | `EXEC` | `$filter, accountName, resourceGroupName, subscriptionId` | Retrieves the metrics determined by the given filter for the given database account. |
| `DatabaseAccounts_ListReadOnlyKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the read-only access keys for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_ListUsages` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Retrieves the usages (most recent data) for the given database account. |
| `DatabaseAccounts_OfflineRegion` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Offline the specified region for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_OnlineRegion` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Online the specified region for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyKind` | Regenerates an access key for the specified Azure Cosmos DB database account. |
| `DatabaseAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Azure Cosmos DB database account. |
