---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.backups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Get the specified Backup under Backup Vault. |
| <CopyableCode code="list_by_vault" /> | `SELECT` | <CopyableCode code="accountName, backupVaultName, resourceGroupName, subscriptionId" /> | List all backups Under a Backup Vault |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId, data__properties" /> | Create a backup under the Backup Vault |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Delete a Backup under the Backup Vault |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, backupName, backupVaultName, resourceGroupName, subscriptionId" /> | Patch a Backup under the Backup Vault |
