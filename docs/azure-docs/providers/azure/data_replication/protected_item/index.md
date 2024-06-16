---
title: protected_item
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_item
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
<tr><td><b>Name</b></td><td><code>protected_item</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.protected_item" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Protected item model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the list of protected items in the given vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates the protected item. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Removes the protected item. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Performs the planned failover on the protected item. |
