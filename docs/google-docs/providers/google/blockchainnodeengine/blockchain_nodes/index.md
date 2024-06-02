---
title: blockchain_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - blockchain_nodes
  - blockchainnodeengine
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>blockchain_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="blockchainnodeengine.blockchain_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The fully qualified name of the blockchain node. e.g. `projects/my-project/locations/us-central1/blockchainNodes/my-node`. |
| <CopyableCode code="blockchainType" /> | `string` | Immutable. The blockchain type of the node. |
| <CopyableCode code="connectionInfo" /> | `object` | The connection information through which to interact with a blockchain node. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp at which the blockchain node was first created. |
| <CopyableCode code="ethereumDetails" /> | `object` | Ethereum-specific blockchain node details. |
| <CopyableCode code="labels" /> | `object` | User-provided key-value pairs. |
| <CopyableCode code="privateServiceConnectEnabled" /> | `boolean` | Optional. When true, the node is only accessible via Private Service Connect; no public endpoints are exposed. Otherwise, the node is only accessible via public endpoints. Warning: Private Service Connect enabled nodes may require a manual migration effort to remain compatible with future versions of the product. If this feature is enabled, you will be notified of these changes along with any required action to avoid disruption. See https://cloud.google.com/vpc/docs/private-service-connect. |
| <CopyableCode code="state" /> | `string` | Output only. A status representing the state of the node. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp at which the blockchain node was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blockchainNodesId, locationsId, projectsId" /> | Gets details of a single blockchain node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists blockchain nodes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new blockchain node in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blockchainNodesId, locationsId, projectsId" /> | Deletes a single blockchain node. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists blockchain nodes in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="blockchainNodesId, locationsId, projectsId" /> | Updates the parameters of a single blockchain node. |
