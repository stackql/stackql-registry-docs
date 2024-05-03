---
title: recovery_points
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points
  - data_replication
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
<tr><td><b>Name</b></td><td><code>recovery_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.recovery_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Recovery point model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="protectedItemName, recoveryPointName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the recovery point of a protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Gets the list of recovery points of the given protected item. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Gets the list of recovery points of the given protected item. |
