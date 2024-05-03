---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
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
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.providers" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | Gets the specified resource provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all resource providers for a subscription. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets all resource providers for a subscription. |
| <CopyableCode code="_provider_permissions" /> | `EXEC` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | Get the provider permissions. |
| <CopyableCode code="provider_permissions" /> | `EXEC` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | Get the provider permissions. |
| <CopyableCode code="register" /> | `EXEC` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | Registers a subscription with a resource provider. |
| <CopyableCode code="register_at_management_group_scope" /> | `EXEC` | <CopyableCode code="groupId, resourceProviderNamespace" /> | Registers a management group with a resource provider. Use this operation to register a resource provider with resource types that can be deployed at the management group scope. It does not recursively register subscriptions within the management group. Instead, you must register subscriptions individually. |
| <CopyableCode code="unregister" /> | `EXEC` | <CopyableCode code="resourceProviderNamespace, subscriptionId" /> | Unregisters a subscription from a resource provider. |
