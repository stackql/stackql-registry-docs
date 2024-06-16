---
title: replication_migration_items
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_migration_items
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_migration_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_migration_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Migration item properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> |  |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the list of ASR migration items in the protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create an ASR migration item (enable migration). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete an ASR migration item. |
| <CopyableCode code="migrate" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate migration of the item. |
| <CopyableCode code="pause_replication" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate pause replication of the item. |
| <CopyableCode code="resume_replication" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate resume replication of the item. |
| <CopyableCode code="resync" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to resynchronize replication of an ASR migration item. |
| <CopyableCode code="test_migrate" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate test migration of the item. |
| <CopyableCode code="test_migrate_cleanup" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to initiate test migrate cleanup. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update the recovery settings of an ASR migration item. |
