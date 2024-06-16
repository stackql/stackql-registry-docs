---
title: replications
hide_title: false
hide_table_of_contents: false
keywords:
  - replications
  - container_registry
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
<tr><td><b>Name</b></td><td><code>replications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.replications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of a replication. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, replicationName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified replication. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the replications for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, replicationName, resourceGroupName, subscriptionId" /> | Creates a replication for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, replicationName, resourceGroupName, subscriptionId" /> | Deletes a replication from a container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="registryName, replicationName, resourceGroupName, subscriptionId" /> | Updates a replication for a container registry with the specified parameters. |
