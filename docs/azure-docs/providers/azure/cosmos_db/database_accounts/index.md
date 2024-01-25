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
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | Indicates the type of database account. This can only be set at database account creation. |
| `location` | `string` | The location of the resource group to which the resource belongs. |
| `properties` | `object` | Properties for the database account. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| `type` | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Retrieves the properties of an existing Azure Cosmos DB database account. |
| `list` | `SELECT` | `subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account. |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes an existing Azure Cosmos DB database account. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| `check_name_exists` | `EXEC` | `accountName` | Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters. |
| `failover_priority_change` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__failoverPolicies` | Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |
| `offline_region` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Offline the specified region for the specified Azure Cosmos DB database account. |
| `online_region` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__region` | Online the specified region for the specified Azure Cosmos DB database account. |
| `regenerate_key` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyKind` | Regenerates an access key for the specified Azure Cosmos DB database account. |
| `update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Updates the properties of an existing Azure Cosmos DB database account. |
