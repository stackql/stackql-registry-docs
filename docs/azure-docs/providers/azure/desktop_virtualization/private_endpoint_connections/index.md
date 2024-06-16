---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - desktop_virtualization
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_host_pool" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | List private endpoint connections associated with hostpool. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List private endpoint connections. |
| <CopyableCode code="delete_by_host_pool" /> | `DELETE` | <CopyableCode code="hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Remove a connection. |
| <CopyableCode code="delete_by_workspace" /> | `DELETE` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Remove a connection. |
| <CopyableCode code="get_by_host_pool" /> | `EXEC` | <CopyableCode code="hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Get a private endpoint connection. |
| <CopyableCode code="get_by_workspace" /> | `EXEC` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Get a private endpoint connection. |
| <CopyableCode code="update_by_host_pool" /> | `EXEC` | <CopyableCode code="hostPoolName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approve or reject a private endpoint connection. |
| <CopyableCode code="update_by_workspace" /> | `EXEC` | <CopyableCode code="privateEndpointConnectionName, resourceGroupName, subscriptionId, workspaceName" /> | Approve or reject a private endpoint connection. |
