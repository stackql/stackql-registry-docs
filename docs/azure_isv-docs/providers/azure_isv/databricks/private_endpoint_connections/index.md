---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - databricks
  - azure_isv    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.databricks.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The properties of a private endpoint connection |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Get a private endpoint connection properties for a workspace |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List private endpoint connections of the workspace |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Update the status of a private endpoint connection with the specified name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Remove private endpoint connection with the specified name |
