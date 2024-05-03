---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - object_storage
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.object_storage.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID for this cluster. |
| <CopyableCode code="domain" /> | `string` | The base URL for this cluster, used for connecting with third-party clients. |
| <CopyableCode code="region" /> | `string` | The region where this cluster is located. |
| <CopyableCode code="static_site_domain" /> | `string` | The base URL for this cluster used when hosting static sites. |
| <CopyableCode code="status" /> | `string` | This cluster's status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getObjectStorageCluster" /> | `SELECT` | <CopyableCode code="clusterId" /> | Returns a single Object Storage Cluster.<br /> |
| <CopyableCode code="getObjectStorageClusters" /> | `SELECT` |  | Returns a paginated list of Object Storage Clusters that are available for<br />use.  Users can connect to the clusters with third party clients to create buckets<br />and upload objects.<br /> |
| <CopyableCode code="_getObjectStorageCluster" /> | `EXEC` | <CopyableCode code="clusterId" /> | Returns a single Object Storage Cluster.<br /> |
| <CopyableCode code="_getObjectStorageClusters" /> | `EXEC` |  | Returns a paginated list of Object Storage Clusters that are available for<br />use.  Users can connect to the clusters with third party clients to create buckets<br />and upload objects.<br /> |
