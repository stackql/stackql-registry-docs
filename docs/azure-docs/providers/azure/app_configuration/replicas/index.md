---
title: replicas
hide_title: false
hide_table_of_contents: false
keywords:
  - replicas
  - app_configuration
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
<tr><td><b>Name</b></td><td><code>replicas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.replicas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the replica. |
| <CopyableCode code="location" /> | `string` | The location of the replica. |
| <CopyableCode code="properties" /> | `object` | All replica properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified replica. |
| <CopyableCode code="list_by_configuration_store" /> | `SELECT` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Lists the replicas for a given configuration store. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Creates a replica with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, replicaName, resourceGroupName, subscriptionId" /> | Deletes a replica. |
| <CopyableCode code="_list_by_configuration_store" /> | `EXEC` | <CopyableCode code="configStoreName, resourceGroupName, subscriptionId" /> | Lists the replicas for a given configuration store. |
