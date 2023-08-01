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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | Base class for backup policy. Workload-specific backup policies are derived from this class. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectionPolicies_Get` | `SELECT` | `api-version, policyName, resourceGroupName, subscriptionId, vaultName` | Provides the details of the backup policies associated to Recovery Services Vault. This is an asynchronous<br />operation. Status of the operation can be fetched using GetPolicyOperationResult API. |
| `ProtectionPolicies_CreateOrUpdate` | `INSERT` | `api-version, policyName, resourceGroupName, subscriptionId, vaultName` | Creates or modifies a backup policy. This is an asynchronous operation. Status of the operation can be fetched<br />using GetPolicyOperationResult API. |
| `ProtectionPolicies_Delete` | `DELETE` | `api-version, policyName, resourceGroupName, subscriptionId, vaultName` | Deletes specified backup policy from your Recovery Services Vault. This is an asynchronous operation. Status of the<br />operation can be fetched using GetProtectionPolicyOperationResult API. |
