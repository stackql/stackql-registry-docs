---
title: iscsi_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_targets
  - storage_pool
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
<tr><td><b>Name</b></td><td><code>iscsi_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.iscsi_targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="managedByExtended" /> | `array` | List of Azure resource ids that manage this resource. |
| <CopyableCode code="properties" /> | `object` | Response properties for iSCSI Target operations. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId" /> | Get an iSCSI Target. |
| <CopyableCode code="list_by_disk_pool" /> | `SELECT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Get iSCSI Targets in a Disk pool. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties" /> | Create or Update an iSCSI Target. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId" /> | Delete an iSCSI Target. |
| <CopyableCode code="_list_by_disk_pool" /> | `EXEC` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Get iSCSI Targets in a Disk pool. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="diskPoolName, iscsiTargetName, resourceGroupName, subscriptionId, data__properties" /> | Update an iSCSI Target. |
