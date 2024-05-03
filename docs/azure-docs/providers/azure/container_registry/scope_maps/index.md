---
title: scope_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_maps
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
<tr><td><b>Name</b></td><td><code>scope_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.scope_maps" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Gets the properties of the specified scope map. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the scope maps for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Creates a scope map for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Deletes a scope map from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the scope maps for the specified container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, scopeMapName, subscriptionId" /> | Updates a scope map with the specified parameters. |
