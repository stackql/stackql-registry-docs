---
title: replication_storage_classification_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_storage_classification_mappings
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_storage_classification_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_storage_classification_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Storage mapping properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | Gets the details of the specified storage classification mapping. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the storage classification mappings in the vault. |
| `list_by_replication_storage_classifications` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId` | Lists the storage classification mappings for the fabric. |
| `create` | `INSERT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | The operation to create a storage classification mapping. |
| `delete` | `DELETE` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | The operation to delete a storage classification mapping. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the storage classification mappings in the vault. |
| `_list_by_replication_storage_classifications` | `EXEC` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId` | Lists the storage classification mappings for the fabric. |
