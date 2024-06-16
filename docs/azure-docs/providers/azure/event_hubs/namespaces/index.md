---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_hubs
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Properties to configure Identity for Bring your Own Keys |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `` | Namespace properties supplied for create namespace operation. |
| <CopyableCode code="sku" /> | `object` | SKU parameters supplied to the create namespace operation |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets the description of the specified namespace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available Namespaces within a subscription, irrespective of the resource groups. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the available Namespaces within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check the give Namespace name availability. |
| <CopyableCode code="failover" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | GeoDR Failover |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the primary or secondary connection strings for the specified Namespace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
