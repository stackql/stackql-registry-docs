---
title: private_endpoint_connections_private_link_hub
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_private_link_hub
  - synapse
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_private_link_hub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.private_endpoint_connections_private_link_hub" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties of a private endpoint connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | Get all PrivateEndpointConnection in the PrivateLinkHub by name |
| <CopyableCode code="list" /> | `SELECT` |  | Get all PrivateEndpointConnections in the PrivateLinkHub |
| <CopyableCode code="_list" /> | `EXEC` |  | Get all PrivateEndpointConnections in the PrivateLinkHub |
