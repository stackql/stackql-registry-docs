---
title: backup_status
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_status
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>backup_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.backup_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acquireStorageAccountLock" /> | `string` | Specifies whether the storage account lock has been acquired or not |
| <CopyableCode code="containerName" /> | `string` | Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;csname;vmname. |
| <CopyableCode code="errorCode" /> | `string` | ErrorCode in case of intent failed |
| <CopyableCode code="errorMessage" /> | `string` | ErrorMessage in case of intent failed. |
| <CopyableCode code="fabricName" /> | `string` | Specifies the fabric name - Azure or AD |
| <CopyableCode code="policyName" /> | `string` | Specifies the policy name which is used for protection |
| <CopyableCode code="protectedItemName" /> | `string` | Specifies the product specific ds name. E.g. vm;iaasvmcontainer;csname;vmname. |
| <CopyableCode code="protectedItemsCount" /> | `integer` | Number of protected items |
| <CopyableCode code="protectionStatus" /> | `string` | Specifies whether the container is registered or not |
| <CopyableCode code="registrationStatus" /> | `string` | Container registration status |
| <CopyableCode code="vaultId" /> | `string` | Specifies the arm resource id of the vault |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, azureRegion, subscriptionId" /> |
