---
title: restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - restore_points
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
<tr><td><b>Name</b></td><td><code>restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.restore_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The restore point properties. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to get the restore point. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to create the restore point. Updating properties of an existing restore point is not allowed |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, restorePointCollectionName, restorePointName, subscriptionId" /> | The operation to delete the restore point. |
