---
title: protected_item_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_item_operation_results
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
<tr><td><b>Name</b></td><td><code>protected_item_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.protected_item_operation_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Base class for backup items. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ProtectedItemOperationResults_Get` | `SELECT` | `api-version, containerName, fabricName, operationId, protectedItemName, resourceGroupName, subscriptionId, vaultName` |
