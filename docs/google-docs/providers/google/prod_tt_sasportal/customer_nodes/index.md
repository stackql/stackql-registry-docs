---
title: customer_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_nodes
  - prod_tt_sasportal
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
<tr><td><b>Name</b></td><td><code>customer_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="prod_tt_sasportal.customer_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. |
| <CopyableCode code="displayName" /> | `string` | The node's display name. |
| <CopyableCode code="sasUserIds" /> | `array` | User ids used by the devices belonging to this node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_nodes_list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists nodes. |
| <CopyableCode code="customers_nodes_nodes_list" /> | `SELECT` | <CopyableCode code="customersId, nodesId" /> | Lists nodes. |
| <CopyableCode code="customers_nodes_create" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a new node. |
| <CopyableCode code="customers_nodes_nodes_create" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a new node. |
| <CopyableCode code="customers_nodes_delete" /> | `DELETE` | <CopyableCode code="customersId, nodesId" /> | Deletes a node. |
| <CopyableCode code="_customers_nodes_list" /> | `EXEC` | <CopyableCode code="customersId" /> | Lists nodes. |
| <CopyableCode code="_customers_nodes_nodes_list" /> | `EXEC` | <CopyableCode code="customersId, nodesId" /> | Lists nodes. |
