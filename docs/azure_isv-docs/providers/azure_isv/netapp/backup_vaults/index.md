---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
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
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backup_vaults" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Backup Vault properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Get the Backup Vault |
| <CopyableCode code="list_by_netapp_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List and describe all Backup Vaults in the NetApp account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId, data__location" /> | Create or update the specified Backup Vault in the NetApp account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Delete the specified Backup Vault |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | Patch the specified NetApp Backup Vault |
