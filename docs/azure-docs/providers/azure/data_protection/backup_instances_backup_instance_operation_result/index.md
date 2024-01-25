---
title: backup_instances_backup_instance_operation_result
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances_backup_instance_operation_result
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_instances_backup_instance_operation_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_instances_backup_instance_operation_result</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Proxy Resource Id represents the complete path to the resource. |
| `name` | `string` | Proxy Resource name associated with the resource. |
| `properties` | `object` | Backup Instance |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Proxy Resource tags. |
| `type` | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `backupInstanceName, operationId, resourceGroupName, subscriptionId, vaultName` |
