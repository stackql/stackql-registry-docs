---
title: managed_unsupported_vm_sizes
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_unsupported_vm_sizes
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>managed_unsupported_vm_sizes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_managed_clusters.managed_unsupported_vm_sizes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | VM Size id. |
| <CopyableCode code="name" /> | `string` | VM Size name. |
| <CopyableCode code="properties" /> | `object` | VM Sizes properties. |
| <CopyableCode code="type" /> | `string` | VM Size type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, location, subscriptionId, vmSize" /> | Get unsupported vm size for Service Fabric Managed Clusters. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, location, subscriptionId" /> | Get the lists of unsupported vm sizes for Service Fabric Managed Clusters. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, location, subscriptionId" /> | Get the lists of unsupported vm sizes for Service Fabric Managed Clusters. |
