---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the operation. |
| <CopyableCode code="actionType" /> | `string` |  |
| <CopyableCode code="display" /> | `object` | Display information of the operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation applies to data-plane. |
| <CopyableCode code="origin" /> | `string` |  |
| <CopyableCode code="properties" /> | `` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` |  | Lists all the operations supported by Microsoft.ProviderHub. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the operations supported by the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, subscriptionId, data__contents" /> | Creates or updates the operation supported by the given provider. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, subscriptionId" /> | Deletes an operation. |
| <CopyableCode code="_list" /> | `EXEC` |  | Lists all the operations supported by Microsoft.ProviderHub. |
