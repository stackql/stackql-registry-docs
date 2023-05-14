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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.object_storage.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique ID for this cluster. |
| `domain` | `string` | The base URL for this cluster, used for connecting with third-party clients. |
| `region` | `string` | The region where this cluster is located. |
| `static_site_domain` | `string` | The base URL for this cluster used when hosting static sites. |
| `status` | `string` | This cluster's status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getObjectStorageCluster` | `SELECT` | `clusterId` | Returns a single Object Storage Cluster.<br /> |
| `getObjectStorageClusters` | `SELECT` |  | Returns a paginated list of Object Storage Clusters that are available for<br />use.  Users can connect to the clusters with third party clients to create buckets<br />and upload objects.<br /> |
| `_getObjectStorageCluster` | `EXEC` | `clusterId` | Returns a single Object Storage Cluster.<br /> |
| `_getObjectStorageClusters` | `EXEC` |  | Returns a paginated list of Object Storage Clusters that are available for<br />use.  Users can connect to the clusters with third party clients to create buckets<br />and upload objects.<br /> |
