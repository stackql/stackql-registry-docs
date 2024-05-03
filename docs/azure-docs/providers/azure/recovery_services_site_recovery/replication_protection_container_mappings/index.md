---
title: replication_protection_container_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_container_mappings
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
<tr><td><b>Name</b></td><td><code>replication_protection_container_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_container_mappings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection container mapping properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a protection container mapping. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings in the vault. |
| <CopyableCode code="list_by_replication_protection_containers" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings for a protection container. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to create a protection container mapping. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to delete or remove a protection container mapping. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings in the vault. |
| <CopyableCode code="_list_by_replication_protection_containers" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection container mappings for a protection container. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to purge(force delete) a protection container mapping. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, fabricName, mappingName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update protection container mapping. |
