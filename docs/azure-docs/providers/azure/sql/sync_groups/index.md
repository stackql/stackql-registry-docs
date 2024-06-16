---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
  - sql
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
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.sync_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a sync group. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Gets a sync group. |
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId" /> | Lists sync groups under a hub database. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Creates or updates a sync group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Deletes a sync group. |
| <CopyableCode code="cancel_sync" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Cancels a sync group synchronization. |
| <CopyableCode code="refresh_hub_schema" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Refreshes a hub database schema. |
| <CopyableCode code="trigger_sync" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Triggers a sync group synchronization. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName" /> | Updates a sync group. |
