---
title: providers_at_tenant_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - providers_at_tenant_scope
  - resources
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
<tr><td><b>Name</b></td><td><code>providers_at_tenant_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.providers_at_tenant_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The provider ID. |
| <CopyableCode code="namespace" /> | `string` | The namespace of the resource provider. |
| <CopyableCode code="providerAuthorizationConsentState" /> | `string` | The provider authorization consent state. |
| <CopyableCode code="registrationPolicy" /> | `string` | The registration policy of the resource provider. |
| <CopyableCode code="registrationState" /> | `string` | The registration state of the resource provider. |
| <CopyableCode code="resourceTypes" /> | `array` | The collection of provider resource types. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceProviderNamespace" /> | Gets the specified resource provider at the tenant level. |
| <CopyableCode code="list" /> | `SELECT` |  | Gets all resource providers for the tenant. |
