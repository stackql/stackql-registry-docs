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
| `properties` | `object` | Storage mapping properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationStorageClassificationMappings_Get` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | Gets the details of the specified storage classification mapping. |
| `ReplicationStorageClassificationMappings_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the storage classification mappings in the vault. |
| `ReplicationStorageClassificationMappings_ListByReplicationStorageClassifications` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId` | Lists the storage classification mappings for the fabric. |
| `ReplicationStorageClassificationMappings_Create` | `INSERT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | The operation to create a storage classification mapping. |
| `ReplicationStorageClassificationMappings_Delete` | `DELETE` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId` | The operation to delete a storage classification mapping. |
