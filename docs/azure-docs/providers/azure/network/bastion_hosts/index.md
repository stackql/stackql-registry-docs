---
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
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
<tr><td><b>Name</b></td><td><code>bastion_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.bastion_hosts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the Bastion Host. |
| <CopyableCode code="sku" /> | `object` | The sku of this Bastion Host. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Gets the specified Bastion Host. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Bastion Hosts in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Bastion Hosts in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Creates or updates the specified Bastion Host. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Deletes the specified Bastion Host. |
| <CopyableCode code="bastion_hosts" /> | `EXEC` | <CopyableCode code="bastionHostName, resourceGroupName, subscriptionId" /> | Returns the list of currently active sessions on the Bastion. |
