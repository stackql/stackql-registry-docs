---
title: database_migrations_mongo_to_cosmos_db_ru_mongo_for_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - database_migrations_mongo_to_cosmos_db_ru_mongo_for_scope
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
<tr><td><b>Name</b></td><td><code>database_migrations_mongo_to_cosmos_db_ru_mongo_for_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.database_migrations_mongo_to_cosmos_db_ru_mongo_for_scope" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, targetResourceName" /> |
| <CopyableCode code="_get" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, targetResourceName" /> |
