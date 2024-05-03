---
title: snapshot_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshot_policies
  - netapp
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
<tr><td><b>Name</b></td><td><code>snapshot_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.snapshot_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Snapshot policy properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Get a snapshot Policy |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List snapshot policy |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId, data__location, data__properties" /> | Create a snapshot policy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Delete snapshot policy |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List snapshot policy |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, snapshotPolicyName, subscriptionId" /> | Patch a snapshot policy |
