---
title: virtual_appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_appliances
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_appliances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Network Virtual Appliance definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Gets the specified Network Virtual Appliance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Network Virtual Appliances in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Network Virtual Appliances in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Network Virtual Appliance. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Deletes the specified Network Virtual Appliance. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="networkVirtualApplianceName, resourceGroupName, subscriptionId" /> | Restarts one or more VMs belonging to the specified Network Virtual Appliance. |
