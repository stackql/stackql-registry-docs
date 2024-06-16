---
title: cloud_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_endpoints
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
<tr><td><b>Name</b></td><td><code>cloud_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_sync.cloud_endpoints" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a given CloudEndpoint. |
| <CopyableCode code="list_by_sync_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get a CloudEndpoint List. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Create a new CloudEndpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Delete a given CloudEndpoint. |
| <CopyableCode code="afs_share_metadata_certificate_public_keys" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Get the AFS file share metadata signing certificate public keys. |
| <CopyableCode code="post_backup" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Post Backup a given CloudEndpoint. |
| <CopyableCode code="post_restore" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Post Restore a given CloudEndpoint. |
| <CopyableCode code="pre_backup" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Pre Backup a given CloudEndpoint. |
| <CopyableCode code="pre_restore" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Pre Restore a given CloudEndpoint. |
| <CopyableCode code="restoreheartbeat" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Restore Heartbeat a given CloudEndpoint. |
| <CopyableCode code="trigger_change_detection" /> | `EXEC` | <CopyableCode code="cloudEndpointName, resourceGroupName, storageSyncServiceName, subscriptionId, syncGroupName" /> | Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint. |
