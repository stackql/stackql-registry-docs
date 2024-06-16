---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.databases" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Gets information about a database in a RedisEnterprise cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets all databases in the specified RedisEnterprise cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Creates a database |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Deletes a single database |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUri" /> | Exports a database file from target database. |
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Flushes all the keys in this database and also from its linked databases. |
| <CopyableCode code="force_link_to_replication_group" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__groupNickname, data__linkedDatabases" /> | Forcibly recreates an existing database on the specified cluster, and rejoins it to an existing replication group. **IMPORTANT NOTE:** All data in this database will be discarded, and the database will temporarily be unavailable while rejoining the replication group. |
| <CopyableCode code="force_unlink" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__ids" /> | Forcibly removes the link to the specified database resource. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUris" /> | Imports database files to target database. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the RedisEnterprise database's access keys. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Updates a database |
| <CopyableCode code="upgrade_db_redis_version" /> | `EXEC` | <CopyableCode code="clusterName, databaseName, resourceGroupName, subscriptionId" /> | Upgrades the database Redis version to the latest available. |
