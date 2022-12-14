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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.backup_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `containerName` | `string` | Specifies the product specific container name. E.g. iaasvmcontainer;iaasvmcontainer;csname;vmname. |
| `fabricName` | `string` | Specifies the fabric name - Azure or AD |
| `registrationStatus` | `string` | Container registration status |
| `protectionStatus` | `string` | Specifies whether the container is registered or not |
| `vaultId` | `string` | Specifies the arm resource id of the vault |
| `errorCode` | `string` | ErrorCode in case of intent failed |
| `errorMessage` | `string` | ErrorMessage in case of intent failed. |
| `policyName` | `string` | Specifies the policy name which is used for protection |
| `protectedItemName` | `string` | Specifies the product specific ds name. E.g. vm;iaasvmcontainer;csname;vmname. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BackupStatus_Get` | `SELECT` | `api-version, azureRegion, subscriptionId` |
