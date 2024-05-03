---
title: application_gateway_private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - application_gateway_private_endpoint_connections
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
<tr><td><b>Name</b></td><td><code>application_gateway_private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.application_gateway_private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the private endpoint connection on an application gateway. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of Private Link Resource of an application gateway. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Gets the specified private endpoint connection on application gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Lists all private endpoint connections on an application gateway. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Deletes the specified private endpoint connection on application gateway. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="applicationGatewayName, resourceGroupName, subscriptionId" /> | Lists all private endpoint connections on an application gateway. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="applicationGatewayName, connectionName, resourceGroupName, subscriptionId" /> | Updates the specified private endpoint connection on application gateway. |
