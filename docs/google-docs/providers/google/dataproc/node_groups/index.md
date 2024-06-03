---
title: node_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - node_groups
  - dataproc
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
<tr><td><b>Name</b></td><td><code>node_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.node_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The Node group resource name (https://aip.dev/122). |
| <CopyableCode code="labels" /> | `object` | Optional. Node group labels. Label keys must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty. If specified, they must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). The node group must have no more than 32 labelsn. |
| <CopyableCode code="nodeGroupConfig" /> | `object` | The config settings for Compute Engine resources in an instance group, such as a master or worker group. |
| <CopyableCode code="roles" /> | `array` | Required. Node group roles. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_regions_clusters_node_groups_get" /> | `SELECT` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Gets the resource representation for a node group in a cluster. |
| <CopyableCode code="projects_regions_clusters_node_groups_create" /> | `INSERT` | <CopyableCode code="clustersId, projectsId, regionsId" /> | Creates a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata). |
| <CopyableCode code="projects_regions_clusters_node_groups_repair" /> | `EXEC` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Repair nodes in a node group. |
| <CopyableCode code="projects_regions_clusters_node_groups_resize" /> | `EXEC` | <CopyableCode code="clustersId, nodeGroupsId, projectsId, regionsId" /> | Resizes a node group in a cluster. The returned Operation.metadata is NodeGroupOperationMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#nodegroupoperationmetadata). |
