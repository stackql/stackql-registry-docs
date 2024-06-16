---
title: jit_network_access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - jit_network_access_policies
  - security
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
<tr><td><b>Name</b></td><td><code>jit_network_access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.jit_network_access_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="kind" /> | `string` | Kind of the resource |
| <CopyableCode code="location" /> | `string` | Location where the resource is stored |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control. |
| <CopyableCode code="list_by_region" /> | `SELECT` | <CopyableCode code="api-version, ascLocation, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="list_by_resource_group_and_region" /> | `SELECT` | <CopyableCode code="api-version, ascLocation, resourceGroupName, subscriptionId" /> | Policies for protecting resources using Just-in-Time access control for the subscription, location |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__properties" /> | Create a policy for protecting resources using Just-in-Time access control |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, ascLocation, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId" /> | Delete a Just-in-Time access control policy. |
| <CopyableCode code="initiate" /> | `EXEC` | <CopyableCode code="api-version, ascLocation, jitNetworkAccessPolicyInitiateType, jitNetworkAccessPolicyName, resourceGroupName, subscriptionId, data__virtualMachines" /> | Initiate a JIT access from a specific Just-in-Time policy configuration. |
