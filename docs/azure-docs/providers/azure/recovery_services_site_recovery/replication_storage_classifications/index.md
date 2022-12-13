---
title: replication_storage_classifications
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_storage_classifications
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
<tr><td><b>Name</b></td><td><code>replication_storage_classifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_storage_classifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | Storage object properties. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationStorageClassifications_Get` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId` | Gets the details of the specified storage classification. |
| `ReplicationStorageClassifications_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Lists the storage classifications in the vault. |
| `ReplicationStorageClassifications_ListByReplicationFabrics` | `SELECT` | `api-version, fabricName, resourceGroupName, resourceName, subscriptionId` | Lists the storage classifications available in the specified fabric. |
