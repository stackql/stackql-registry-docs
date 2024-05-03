---
title: connected_registries
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_registries
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
<tr><td><b>Name</b></td><td><code>connected_registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.connected_registries" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the connected registry. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all connected registries for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Creates a connected registry for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Deletes a connected registry from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all connected registries for the specified container registry. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Deactivates the connected registry instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="connectedRegistryName, registryName, resourceGroupName, subscriptionId" /> | Updates a connected registry with the specified parameters. |
