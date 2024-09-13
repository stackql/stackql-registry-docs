---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - migrationcenter
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

Creates, updates, deletes or gets an <code>asset</code> resource or lists <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The full name of the asset. |
| <CopyableCode code="assignedGroups" /> | `array` | Output only. The list of groups that the asset is assigned to. |
| <CopyableCode code="attributes" /> | `object` | Generic asset attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the asset was created. |
| <CopyableCode code="insightList" /> | `object` | Message containing insights list. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="machineDetails" /> | `object` | Details of a machine. |
| <CopyableCode code="performanceData" /> | `object` | Performance data for an asset. |
| <CopyableCode code="sources" /> | `array` | Output only. The list of sources contributing to the asset. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the asset was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Gets the details of an asset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the assets in a given project and location. |
| <CopyableCode code="batch_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId" /> | Deletes list of Assets. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Deletes an asset. |
| <CopyableCode code="batch_update" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Updates the parameters of a list of assets. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="assetsId, locationsId, projectsId" /> | Updates the parameters of an asset. |
| <CopyableCode code="aggregate_values" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Aggregates the requested fields based on provided function. |
| <CopyableCode code="report_asset_frames" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Reports a set of frames. |

## `SELECT` examples

Lists all the assets in a given project and location.

```sql
SELECT
name,
assignedGroups,
attributes,
createTime,
insightList,
labels,
machineDetails,
performanceData,
sources,
updateTime
FROM google.migrationcenter.assets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a asset only if the necessary resources are available.

```sql
UPDATE google.migrationcenter.assets
SET 
requests = '{{ requests }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified asset resource.

```sql
DELETE FROM google.migrationcenter.assets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
