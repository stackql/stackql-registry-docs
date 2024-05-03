---
title: database_migrations_mongo_to_cosmos_dbv_core_mongo
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_mongo_to_cosmos_dbv_core_mongo
  - data_migration
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
<tr><td><b>Name</b></td><td><code>database_migrations_mongo_to_cosmos_dbv_core_mongo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_mongo_to_cosmos_dbv_core_mongo" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Database Migration Resource properties for CosmosDb for Mongo. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Get Database Migration resource. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Create or Update Database Migration resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="migrationName, resourceGroupName, subscriptionId, targetResourceName" /> | Delete Database Migration resource. |
