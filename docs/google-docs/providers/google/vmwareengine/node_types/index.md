---
title: node_types
hide_title: false
hide_table_of_contents: false
keywords:
  - node_types
  - vmwareengine
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
<tr><td><b>Name</b></td><td><code>node_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vmwareengine.node_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this node type. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-proj/locations/us-central1-a/nodeTypes/standard-72` |
| <CopyableCode code="availableCustomCoreCounts" /> | `array` | Output only. List of possible values of custom core count. |
| <CopyableCode code="capabilities" /> | `array` | Output only. Capabilities of this node type. |
| <CopyableCode code="diskSizeGb" /> | `integer` | Output only. The amount of storage available, defined in GB. |
| <CopyableCode code="displayName" /> | `string` | Output only. The friendly name for this node type. For example: ve1-standard-72 |
| <CopyableCode code="families" /> | `array` | Output only. Families of the node type. For node types to be in the same cluster they must share at least one element in the `families`. |
| <CopyableCode code="kind" /> | `string` | Output only. The type of the resource. |
| <CopyableCode code="memoryGb" /> | `integer` | Output only. The amount of physical memory available, defined in GB. |
| <CopyableCode code="nodeTypeId" /> | `string` | Output only. The canonical identifier of the node type (corresponds to the `NodeType`). For example: standard-72. |
| <CopyableCode code="totalCoreCount" /> | `integer` | Output only. The total number of CPU cores in a single node. |
| <CopyableCode code="virtualCpuCount" /> | `integer` | Output only. The total number of virtual CPUs in a single node. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, nodeTypesId, projectsId" /> | Gets details of a single `NodeType`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists node types |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists node types |
