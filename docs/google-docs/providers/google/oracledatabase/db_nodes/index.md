---
title: db_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_nodes
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>db_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.db_nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the database node resource in the following format: projects/{project}/locations/{location}/cloudVmClusters/{cloud_vm_cluster}/dbNodes/{db_node} |
| <CopyableCode code="properties" /> | `object` | Various properties and settings associated with Db node. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudVmClustersId, locationsId, projectsId" /> | Lists the database nodes of a VM Cluster. |

## `SELECT` examples

Lists the database nodes of a VM Cluster.

```sql
SELECT
name,
properties
FROM google.oracledatabase.db_nodes
WHERE cloudVmClustersId = '{{ cloudVmClustersId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
