---
title: cache_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - cache_rules
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
<tr><td><b>Name</b></td><td><code>cache_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.cache_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified cache rule resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all cache rule resources for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Creates a cache rule for a container registry with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Deletes a cache rule resource from a container registry. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all cache rule resources for the specified container registry. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cacheRuleName, registryName, resourceGroupName, subscriptionId" /> | Updates a cache rule for a container registry with the specified parameters. |
