---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - data_protection
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
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_vaults" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity details |
| <CopyableCode code="properties" /> | `object` | Backup Vault |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Returns a resource belonging to a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates or updates a BackupVault resource belonging to a resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Deletes a BackupVault resource from the resource group. |
| <CopyableCode code="_get_in_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns resource collection belonging to a resource group. |
| <CopyableCode code="_get_in_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Returns resource collection belonging to a subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="get_in_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns resource collection belonging to a resource group. |
| <CopyableCode code="get_in_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Returns resource collection belonging to a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource. |
