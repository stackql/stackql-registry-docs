---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - peering
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.peering.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | The properties that define connectivity to the Peering Service. |
| <CopyableCode code="sku" /> | `object` | The SKU that defines the type of the peering service. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Gets an existing peering service with the specified name under the given subscription and resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the peering services under the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the peerings under the given subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId, data__location" /> | Creates a new peering service or updates an existing peering with the specified name under the given subscription and resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Deletes an existing peering service with the specified name under the given subscription and resource group. |
| <CopyableCode code="initialize_connection_monitor" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Initialize Peering Service for Connection Monitor functionality |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="peeringServiceName, resourceGroupName, subscriptionId" /> | Updates tags for a peering service with the specified name under the given subscription and resource group. |
