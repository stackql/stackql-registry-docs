---
title: replication_protection_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_protection_containers
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
<tr><td><b>Name</b></td><td><code>replication_protection_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_protection_containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Protection profile custom data details. |
| <CopyableCode code="type" /> | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of a protection container. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection containers in a vault. |
| <CopyableCode code="list_by_replication_fabrics" /> | `SELECT` | <CopyableCode code="api-version, fabricName, resourceGroupName, resourceName, subscriptionId" /> | Lists the protection containers in the specified fabric. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to create a protection container. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to remove a protection container. |
| <CopyableCode code="discover_protectable_item" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | The operation to a add a protectable item to a protection container(Add physical server). |
| <CopyableCode code="switch_cluster_protection" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to switch protection from one container to another. |
| <CopyableCode code="switch_protection" /> | `EXEC` | <CopyableCode code="api-version, fabricName, protectionContainerName, resourceGroupName, resourceName, subscriptionId" /> | Operation to switch protection from one container to another or one replication provider to another. |
