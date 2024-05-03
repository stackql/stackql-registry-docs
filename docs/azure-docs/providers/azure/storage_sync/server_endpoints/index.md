---
title: server_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - server_endpoints
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
<tr><td><b>Name</b></td><td><code>server_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.server_endpoints" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a ServerEndpoint. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a ServerEndpoint list. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Create a new ServerEndpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Delete a given ServerEndpoint. |
| <CopyableCode code="_list_by_sync_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a ServerEndpoint list. |
| <CopyableCode code="recall_action" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Recall a server endpoint. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverEndpointName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Patch a given ServerEndpoint. |
