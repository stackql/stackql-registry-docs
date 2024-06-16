---
title: mongo_role_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_role_definition
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
<tr><td><b>Name</b></td><td><code>mongo_role_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongo_role_definition" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the database account. |
| <CopyableCode code="name" /> | `string` | The name of the database account. |
| <CopyableCode code="properties" /> | `object` | Azure Cosmos DB Mongo Role Definition resource object. |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Retrieves the properties of an existing Azure Cosmos DB Mongo Role Definition with the given Id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves the list of all Azure Cosmos DB Mongo Role Definitions. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Cosmos DB Mongo Role Definition. |
| <CopyableCode code="create_update" /> | `EXEC` | <CopyableCode code="accountName, mongoRoleDefinitionId, resourceGroupName, subscriptionId" /> | Creates or updates an Azure Cosmos DB Mongo Role Definition. |
