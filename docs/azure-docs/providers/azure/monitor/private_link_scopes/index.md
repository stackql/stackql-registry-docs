---
title: private_link_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_scopes
  - monitor
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
<tr><td><b>Name</b></td><td><code>private_link_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.private_link_scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties that define a Azure Monitor PrivateLinkScope resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Returns a Azure Monitor PrivateLinkScope. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all Azure Monitor PrivateLinkScopes within a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Monitor PrivateLinkScopes within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId, data__properties" /> | Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Deletes a Azure Monitor PrivateLinkScope. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a list of all Azure Monitor PrivateLinkScopes within a subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Azure Monitor PrivateLinkScopes within a resource group. |
