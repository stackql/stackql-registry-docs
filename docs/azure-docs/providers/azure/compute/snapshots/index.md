---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - compute
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="managedBy" /> | `string` | Unused. Always Null. |
| <CopyableCode code="properties" /> | `object` | Snapshot resource properties. |
| <CopyableCode code="sku" /> | `object` | The snapshots sku name. Can be Standard_LRS, Premium_LRS, or Standard_ZRS. This is an optional parameter for incremental snapshot and the default behavior is the SKU will be set to the same sku as the previous snapshot |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Gets information about a snapshot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists snapshots under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists snapshots under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Creates or updates a snapshot. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Deletes a snapshot. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists snapshots under a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists snapshots under a resource group. |
| <CopyableCode code="grant_access" /> | `EXEC` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId, data__access, data__durationInSeconds" /> | Grants access to a snapshot. |
| <CopyableCode code="revoke_access" /> | `EXEC` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Revokes access to a snapshot. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, snapshotName, subscriptionId" /> | Updates (patches) a snapshot. |
