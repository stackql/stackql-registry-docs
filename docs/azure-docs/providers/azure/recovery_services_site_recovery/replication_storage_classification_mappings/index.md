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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_storage_classification_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_storage_classification_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Storage mapping properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | Gets the details of the specified storage classification mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the storage classification mappings in the vault. |
| <CopyableCode code="list_by_replication_storage_classifications" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId" /> | Lists the storage classification mappings for the fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | The operation to create a storage classification mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, storageClassificationMappingName, storageClassificationName, subscriptionId" /> | The operation to delete a storage classification mapping. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the storage classification mappings in the vault. |
| <CopyableCode code="_list_by_replication_storage_classifications" /> | `EXEC` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, storageClassificationName, subscriptionId" /> | Lists the storage classification mappings for the fabric. |
