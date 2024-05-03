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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.database_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of database account. This can only be set at database account creation. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | Properties for the database account. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB database account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an Azure Cosmos DB database account. The "Update" method is preferred when performing updates on an account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB database account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Azure Cosmos DB database accounts available under the given resource group. |
| <CopyableCode code="check_name_exists" /> | `EXEC` | <CopyableCode code="accountName" /> | Checks that the Azure Cosmos DB account name already exists. A valid account name may contain only lowercase letters, numbers, and the '-' character, and must be between 3 and 50 characters. |
| <CopyableCode code="failover_priority_change" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__failoverPolicies" /> | Changes the failover priority for the Azure Cosmos DB database account. A failover priority of 0 indicates a write region. The maximum value for a failover priority = (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |
| <CopyableCode code="offline_region" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__region" /> | Offline the specified region for the specified Azure Cosmos DB database account. |
| <CopyableCode code="online_region" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__region" /> | Online the specified region for the specified Azure Cosmos DB database account. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__keyKind" /> | Regenerates an access key for the specified Azure Cosmos DB database account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Azure Cosmos DB database account. |
