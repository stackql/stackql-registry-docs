---
title: node_groups_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups_nodes
  - compute
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
<tr><td><b>Name</b></td><td><code>node_groups_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="compute.node_groups_nodes" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_nodes" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Adds specified number of nodes to the node group. |
| <CopyableCode code="delete_nodes" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Deletes specified nodes from the node group. |
| <CopyableCode code="list_nodes" /> | `EXEC` | <CopyableCode code="nodeGroup, project, zone" /> | Lists nodes in the node group. |
