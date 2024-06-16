---
title: private_link_services_private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_private_endpoint_connection
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
<tr><td><b>Name</b></td><td><code>private_link_services_private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_link_services_private_endpoint_connection" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the PrivateEndpointConnectProperties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Get the specific private end point connection by specific private link service in the resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Delete private end point connection for a private link service in a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="peConnectionName, resourceGroupName, serviceName, subscriptionId" /> | Approve or reject private end point connection for a private link service in a subscription. |
