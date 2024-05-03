---
title: storage_account_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_account_credentials
  - storsimple_8000_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>storage_account_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.storage_account_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The name of the object. |
| <CopyableCode code="kind" /> | `string` | The Kind of the object. Currently only Series8000 is supported |
| <CopyableCode code="properties" /> | `object` | The storage account credential properties. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId" /> | Gets the properties of the specified storage account credential name. |
| <CopyableCode code="list_by_manager" /> | `SELECT` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Gets all the storage account credentials in a manager. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId, data__properties" /> | Creates or updates the storage account credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managerName, resourceGroupName, storageAccountCredentialName, subscriptionId" /> | Deletes the storage account credential. |
| <CopyableCode code="_list_by_manager" /> | `EXEC` | <CopyableCode code="managerName, resourceGroupName, subscriptionId" /> | Gets all the storage account credentials in a manager. |
