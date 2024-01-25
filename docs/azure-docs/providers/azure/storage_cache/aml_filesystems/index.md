---
title: aml_filesystems
hide_title: false
hide_table_of_contents: false
keywords:
  - aml_filesystems
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>aml_filesystems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.aml_filesystems</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed Identity properties. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the AML file system. |
| `sku` | `object` | SKU for the resource. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | Availability zones for resources. This field should only contain a single element in the array. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `amlFilesystemName, resourceGroupName, subscriptionId` | Returns an AML file system. |
| `list` | `SELECT` | `subscriptionId` | Returns all AML file systems the user has access to under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all AML file systems the user has access to under a resource group. |
| `create_or_update` | `INSERT` | `amlFilesystemName, resourceGroupName, subscriptionId` | Create or update an AML file system. |
| `delete` | `DELETE` | `amlFilesystemName, resourceGroupName, subscriptionId` | Schedules an AML file system for deletion. |
| `_list` | `EXEC` | `subscriptionId` | Returns all AML file systems the user has access to under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns all AML file systems the user has access to under a resource group. |
| `aml_filesystems` | `EXEC` | `subscriptionId` | Get the number of available IP addresses needed for the AML file system information provided. |
| `archive` | `EXEC` | `amlFilesystemName, resourceGroupName, subscriptionId` | Archive data from the AML file system. |
| `cancel_archive` | `EXEC` | `amlFilesystemName, resourceGroupName, subscriptionId` | Cancel archiving data from the AML file system. |
| `update` | `EXEC` | `amlFilesystemName, resourceGroupName, subscriptionId` | Update an AML file system instance. |
