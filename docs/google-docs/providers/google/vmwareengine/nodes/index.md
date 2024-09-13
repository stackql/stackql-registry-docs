---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>node</code> resource or lists <code>nodes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this node. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: projects/my-project/locations/us-central1-a/privateClouds/my-cloud/clusters/my-cluster/nodes/my-node |
| <CopyableCode code="customCoreCount" /> | `string` | Output only. Customized number of cores |
| <CopyableCode code="fqdn" /> | `string` | Output only. Fully qualified domain name of the node. |
| <CopyableCode code="internalIp" /> | `string` | Output only. Internal IP address of the node. |
| <CopyableCode code="nodeTypeId" /> | `string` | Output only. The canonical identifier of the node type (corresponds to the `NodeType`). For example: standard-72. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the appliance. |
| <CopyableCode code="version" /> | `string` | Output only. The version number of the VMware ESXi management component in this cluster. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, nodesId, privateCloudsId, projectsId" /> | Gets details of a single node. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clustersId, locationsId, privateCloudsId, projectsId" /> | Lists nodes in a given cluster. |

## `SELECT` examples

Lists nodes in a given cluster.

```sql
SELECT
name,
customCoreCount,
fqdn,
internalIp,
nodeTypeId,
state,
version
FROM google.vmwareengine.nodes
WHERE clustersId = '{{ clustersId }}'
AND locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}'; 
```
