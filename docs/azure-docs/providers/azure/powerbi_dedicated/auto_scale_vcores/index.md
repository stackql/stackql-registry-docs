---
title: auto_scale_vcores
hide_title: false
hide_table_of_contents: false
keywords:
  - auto_scale_vcores
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>auto_scale_vcores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.auto_scale_vcores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `string` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="location" /> | `string` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an auto scale v-core resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for auto scale v-core resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the PowerBI Dedicated resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Gets details about the specified auto scale v-core. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the auto scale v-cores for the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the auto scale v-cores for the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName, data__sku" /> | Provisions the specified auto scale v-core based on the configuration specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Deletes the specified auto scale v-core. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vcoreName" /> | Updates the current state of the specified auto scale v-core. |
