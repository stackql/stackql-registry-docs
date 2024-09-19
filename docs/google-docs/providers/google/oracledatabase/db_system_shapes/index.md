---
title: db_system_shapes
hide_title: false
hide_table_of_contents: false
keywords:
  - db_system_shapes
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

Creates, updates, deletes, gets or lists a <code>db_system_shapes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_system_shapes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.db_system_shapes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the Database System Shape resource with the format: projects/{project}/locations/{region}/dbSystemShapes/{db_system_shape} |
| <CopyableCode code="availableCoreCountPerNode" /> | `integer` | Optional. Number of cores per node. |
| <CopyableCode code="availableDataStorageTb" /> | `integer` | Optional. Storage per storage server in terabytes. |
| <CopyableCode code="availableMemoryPerNodeGb" /> | `integer` | Optional. Memory per database server node in gigabytes. |
| <CopyableCode code="maxNodeCount" /> | `integer` | Optional. Maximum number of database servers. |
| <CopyableCode code="maxStorageCount" /> | `integer` | Optional. Maximum number of storage servers. |
| <CopyableCode code="minCoreCountPerNode" /> | `integer` | Optional. Minimum core count per node. |
| <CopyableCode code="minDbNodeStoragePerNodeGb" /> | `integer` | Optional. Minimum node storage per database server in gigabytes. |
| <CopyableCode code="minMemoryPerNodeGb" /> | `integer` | Optional. Minimum memory per node in gigabytes. |
| <CopyableCode code="minNodeCount" /> | `integer` | Optional. Minimum number of database servers. |
| <CopyableCode code="minStorageCount" /> | `integer` | Optional. Minimum number of storage servers. |
| <CopyableCode code="shape" /> | `string` | Optional. shape |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists the database system shapes available for the project and location. |

## `SELECT` examples

Lists the database system shapes available for the project and location.

```sql
SELECT
name,
availableCoreCountPerNode,
availableDataStorageTb,
availableMemoryPerNodeGb,
maxNodeCount,
maxStorageCount,
minCoreCountPerNode,
minDbNodeStoragePerNodeGb,
minMemoryPerNodeGb,
minNodeCount,
minStorageCount,
shape
FROM google.oracledatabase.db_system_shapes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
