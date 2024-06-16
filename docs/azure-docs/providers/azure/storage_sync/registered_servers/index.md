---
title: registered_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - registered_servers
  - storage_sync
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
<tr><td><b>Name</b></td><td><code>registered_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.registered_servers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Get a given registered server. |
| <CopyableCode code="list_by_storage_sync_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId" /> | Get a given registered server list. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Add a new registered server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Delete the given registered server. |
| <CopyableCode code="trigger_rollover" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Triggers Server certificate rollover. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverId, storageSyncServiceName, subscriptionId" /> | Update registered server. |
