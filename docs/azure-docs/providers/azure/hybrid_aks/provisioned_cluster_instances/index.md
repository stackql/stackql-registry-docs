---
title: provisioned_cluster_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>provisioned_cluster_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.provisioned_cluster_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location pointing to the underlying infrastructure |
| <CopyableCode code="properties" /> | `object` | Properties of the provisioned cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Gets the provisioned cluster instance |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedClusterResourceUri" /> | Creates or updates the provisioned cluster instance |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedClusterResourceUri" /> | Deletes the provisioned cluster instance |
