---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this cluster. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster` |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="management" /> | `boolean` | Output only. True if the cluster is a management cluster; false otherwise. There can only be one management cluster in a private cloud and it has to be the first one. |
| <CopyableCode code="nodeTypeConfigs" /> | `object` | Required. The map of cluster node types in this cluster, where the key is canonical identifier of the node type (corresponds to the `NodeType`). |
| <CopyableCode code="state" /> | `string` | Output only. State of the resource. |
| <CopyableCode code="stretchedClusterConfig" /> | `object` | Configuration of a stretched cluster. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, privateCloudsId, projectsId" /> | Retrieves a `Cluster` resource by its resource name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists `Cluster` resources in a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Creates a new cluster in a given private cloud. Creating a new cluster provides additional nodes for use in the parent private cloud and requires sufficient [node quota](https://cloud.google.com/vmware-engine/quotas). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clustersId, locationsId, privateCloudsId, projectsId" /> | Deletes a `Cluster` resource. To avoid unintended data loss, migrate or gracefully shut down any workloads running on the cluster before deletion. You cannot delete the management cluster of a private cloud using this method. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="clustersId, locationsId, privateCloudsId, projectsId" /> | Modifies a `Cluster` resource. Only fields specified in `updateMask` are applied. During operation processing, the resource is temporarily in the `ACTIVE` state before the operation fully completes. For that period of time, you can't update the resource. Use the operation status to determine when the processing fully completes. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists `Cluster` resources in a given private cloud. |
