---
title: protection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_policies
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
<tr><td><b>Name</b></td><td><code>protection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.protection_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Resource name associated with the resource. |
| <CopyableCode code="eTag" /> | `string` | Optional ETag. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Base class for backup policy. Workload-specific backup policies are derived from this class. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, policyName, resourceGroupName, subscriptionId, vaultName" /> | Provides the details of the backup policies associated to Recovery Services Vault. This is an asynchronous<br />operation. Status of the operation can be fetched using GetPolicyOperationResult API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, policyName, resourceGroupName, subscriptionId, vaultName" /> | Creates or modifies a backup policy. This is an asynchronous operation. Status of the operation can be fetched<br />using GetPolicyOperationResult API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, policyName, resourceGroupName, subscriptionId, vaultName" /> | Deletes specified backup policy from your Recovery Services Vault. This is an asynchronous operation. Status of the<br />operation can be fetched using GetProtectionPolicyOperationResult API. |
