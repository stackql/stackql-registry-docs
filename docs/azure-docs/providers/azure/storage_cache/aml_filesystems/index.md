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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aml_filesystems</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.aml_filesystems" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed Identity properties. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the AML file system. |
| <CopyableCode code="sku" /> | `object` | SKU for the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | Availability zones for resources. This field should only contain a single element in the array. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Returns an AML file system. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all AML file systems the user has access to under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all AML file systems the user has access to under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Create or update an AML file system. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Schedules an AML file system for deletion. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Returns all AML file systems the user has access to under a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all AML file systems the user has access to under a resource group. |
| <CopyableCode code="aml_filesystems" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get the number of available IP addresses needed for the AML file system information provided. |
| <CopyableCode code="archive" /> | `EXEC` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Archive data from the AML file system. |
| <CopyableCode code="cancel_archive" /> | `EXEC` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Cancel archiving data from the AML file system. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="amlFilesystemName, resourceGroupName, subscriptionId" /> | Update an AML file system instance. |
