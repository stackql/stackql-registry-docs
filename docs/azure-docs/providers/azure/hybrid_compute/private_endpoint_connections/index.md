---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - hybrid_compute
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a private endpoint connection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId" /> | Gets a private endpoint connection. |
| <CopyableCode code="list_by_private_link_scope" /> | `SELECT` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Gets all private endpoint connections on a private link scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId" /> | Approve or reject a private endpoint connection with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, scopeName, subscriptionId" /> | Deletes a private endpoint connection with a given name. |
| <CopyableCode code="_list_by_private_link_scope" /> | `EXEC` | <CopyableCode code="resourceGroupName, scopeName, subscriptionId" /> | Gets all private endpoint connections on a private link scope. |
