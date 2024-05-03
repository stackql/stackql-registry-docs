---
title: hybrid_identity_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_identity_metadata
  - hybrid_compute
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.hybrid_identity_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, metadataName, resourceGroupName, subscriptionId" /> | Implements HybridIdentityMetadata GET method. |
| <CopyableCode code="list_by_machines" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Returns the list of HybridIdentityMetadata of the given machine. |
| <CopyableCode code="_list_by_machines" /> | `EXEC` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Returns the list of HybridIdentityMetadata of the given machine. |
