---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - event_grid
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified identifier of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the private endpoint connection resource. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get a specific private endpoint connection under a topic, domain, or partner namespace or namespace. |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="parentName, parentType, resourceGroupName, subscriptionId" /> | Get all private endpoint connections under a topic, domain, or partner namespace or namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Delete a specific private endpoint connection under a topic, domain, or partner namespace or namespace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="parentName, parentType, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Update a specific private endpoint connection under a topic, domain or partner namespace. |
