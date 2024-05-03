---
title: remote_rendering_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - remote_rendering_accounts
  - mixed_reality
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
<tr><td><b>Name</b></td><td><code>remote_rendering_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mixed_reality.remote_rendering_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `object` | Identity for the resource. |
| <CopyableCode code="properties" /> | `object` | Common Properties shared by Mixed Reality Accounts |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieve a Remote Rendering Account. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Resources by Resource Group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List Remote Rendering Accounts by Subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Creating or Updating a Remote Rendering Account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Delete a Remote Rendering Account. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List Resources by Resource Group |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List Remote Rendering Accounts by Subscription |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Regenerate specified Key of a Remote Rendering Account |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updating a Remote Rendering Account |
