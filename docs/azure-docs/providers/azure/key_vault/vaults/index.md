---
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
  - key_vault
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
<tr><td><b>Name</b></td><td><code>vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.vaults" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the key vault resource. |
| <CopyableCode code="name" /> | `string` | Name of the key vault resource. |
| <CopyableCode code="location" /> | `string` | Azure location of the key vault resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the vault |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Tags assigned to the key vault resource. |
| <CopyableCode code="type" /> | `string` | Resource type of the key vault resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the specified Azure key vault. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__location, data__properties" /> | Create or update a key vault in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Deletes the specified Azure key vault. |
| <CopyableCode code="_exec_list" /> | `EXEC` | <CopyableCode code="$filter, api-version, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription and within the specified resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the vault name is valid and is not already in use. |
| <CopyableCode code="exec_list" /> | `EXEC` | <CopyableCode code="$filter, api-version, subscriptionId" /> | The List operation gets information about the vaults associated with the subscription. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="location, subscriptionId, vaultName" /> | Permanently deletes the specified vault. aka Purges the deleted Azure key vault. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Update a key vault in the specified subscription. |
