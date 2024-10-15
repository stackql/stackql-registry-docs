---
title: item_level_recovery_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - item_level_recovery_connections
  - recovery_services_backup
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>item_level_recovery_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>item_level_recovery_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.item_level_recovery_connections" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="provision" /> | `EXEC` | <CopyableCode code="containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName" /> | Provisions a script which invokes an iSCSI connection to the backup data. Executing this script opens a file
explorer displaying all the recoverable files and folders. This is an asynchronous operation. To know the status of
provisioning, call GetProtectedItemOperationResult API. |
| <CopyableCode code="revoke" /> | `EXEC` | <CopyableCode code="containerName, fabricName, protectedItemName, recoveryPointId, resourceGroupName, subscriptionId, vaultName" /> | Revokes an iSCSI connection which can be used to download a script. Executing this script opens a file explorer
displaying all recoverable files and folders. This is an asynchronous operation. |
