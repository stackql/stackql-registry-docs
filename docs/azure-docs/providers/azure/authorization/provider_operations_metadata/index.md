---
title: provider_operations_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - provider_operations_metadata
  - authorization
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
<tr><td><b>Name</b></td><td><code>provider_operations_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.provider_operations_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The provider id. |
| <CopyableCode code="name" /> | `string` | The provider name. |
| <CopyableCode code="displayName" /> | `string` | The provider display name. |
| <CopyableCode code="operations" /> | `array` | The provider operations. |
| <CopyableCode code="resourceTypes" /> | `array` | The provider resource types |
| <CopyableCode code="type" /> | `string` | The provider type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceProviderNamespace" /> | Gets provider operations metadata for the specified resource provider. |
| <CopyableCode code="list" /> | `SELECT` |  | Gets provider operations metadata for all resource providers. |
| <CopyableCode code="_list" /> | `EXEC` |  | Gets provider operations metadata for all resource providers. |
