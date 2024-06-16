---
title: network_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - network_functions
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>network_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_network.network_functions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network function properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Gets information about the specified network function resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the network function resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the network functions in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Creates or updates a network function resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId" /> | Deletes the specified network function resource. |
| <CopyableCode code="execute_request" /> | `EXEC` | <CopyableCode code="networkFunctionName, resourceGroupName, subscriptionId, data__requestMetadata, data__serviceEndpoint" /> | Execute a request to services on a containerized network function. |
