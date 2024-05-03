---
title: hybrid_identity_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_identity_metadata
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
<tr><td><b>Name</b></td><td><code>hybrid_identity_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.hybrid_identity_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the resource properties for the hybrid identity metadata. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Get the hybrid identity metadata proxy resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedClusterResourceUri" /> | Deletes the hybrid identity metadata proxy resource. |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="connectedClusterResourceUri, data__properties" /> | Creates the hybrid identity metadata proxy resource that facilitates the managed identity provisioning. |
