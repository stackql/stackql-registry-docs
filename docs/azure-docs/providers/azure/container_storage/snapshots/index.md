---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - container_storage
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
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_storage.snapshots" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Get a Snapshot |
| <CopyableCode code="list_by_pool" /> | `SELECT` | <CopyableCode code="poolName, resourceGroupName, subscriptionId" /> | List Snapshot resources by Pool |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Create a Snapshot |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="poolName, resourceGroupName, snapshotName, subscriptionId" /> | Delete a Snapshot |
