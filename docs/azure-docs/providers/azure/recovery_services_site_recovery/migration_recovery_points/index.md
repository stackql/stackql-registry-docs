---
title: migration_recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_recovery_points
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
<tr><td><b>Name</b></td><td><code>migration_recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.migration_recovery_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Migration item recovery point properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, migrationItemName, migrationRecoveryPointName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> |
| <CopyableCode code="list_by_replication_migration_items" /> | `SELECT` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> |
| <CopyableCode code="_list_by_replication_migration_items" /> | `EXEC` | <CopyableCode code="api-version, fabricName, migrationItemName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> |
