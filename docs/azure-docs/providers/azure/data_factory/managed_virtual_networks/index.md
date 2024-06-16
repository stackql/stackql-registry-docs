---
title: managed_virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_virtual_networks
  - data_factory
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
<tr><td><b>Name</b></td><td><code>managed_virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.managed_virtual_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | A managed Virtual Network associated with the Azure Data Factory |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId" /> | Gets a managed Virtual Network. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists managed Virtual Networks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, factoryName, managedVirtualNetworkName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a managed Virtual Network. |
