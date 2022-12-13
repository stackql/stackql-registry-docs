---
title: protection_intent
hide_title: false
hide_table_of_contents: false
keywords:
  - protection_intent
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
<tr><td><b>Name</b></td><td><code>protection_intent</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protection_intent</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Base class for backup ProtectionIntent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ProtectionIntent_Get` | `SELECT` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,<br />call the GetItemOperationResult API. |
| `ProtectionIntent_CreateOrUpdate` | `INSERT` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Create Intent for Enabling backup of an item. This is a synchronous operation. |
| `ProtectionIntent_Delete` | `DELETE` | `api-version, fabricName, intentObjectName, resourceGroupName, subscriptionId, vaultName` | Used to remove intent from an item |
| `ProtectionIntent_Validate` | `EXEC` | `api-version, azureRegion, subscriptionId` |  |
