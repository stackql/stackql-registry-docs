---
title: node
hide_title: false
hide_table_of_contents: false
keywords:
  - node
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
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.node" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. |
| <CopyableCode code="displayName" /> | `string` | The node's display name. |
| <CopyableCode code="sasUserIds" /> | `array` | User ids used by the devices belonging to this node. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="nodes_get" /> | `SELECT` | <CopyableCode code="nodesId" /> |
| <CopyableCode code="nodes_nodes_get" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> |
