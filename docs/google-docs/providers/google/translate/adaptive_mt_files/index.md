
---
title: adaptive_mt_files
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_mt_files
  - translate
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

Creates, updates, deletes or gets an <code>adaptive_mt_file</code> resource or lists <code>adaptive_mt_files</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adaptive_mt_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.adaptive_mt_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the file, in form of `projects/{project-number-or-id}/locations/{location_id}/adaptiveMtDatasets/{dataset}/adaptiveMtFiles/{file}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this file was created. |
| <CopyableCode code="displayName" /> | `string` | The file's display name. |
| <CopyableCode code="entryCount" /> | `integer` | The number of entries that the file contains. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this file was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_get" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, adaptiveMtFilesId, locationsId, projectsId" /> | Gets and AdaptiveMtFile |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_list" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Lists all AdaptiveMtFiles associated to an AdaptiveMtDataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_delete" /> | `DELETE` | <CopyableCode code="adaptiveMtDatasetsId, adaptiveMtFilesId, locationsId, projectsId" /> | Deletes an AdaptiveMtFile along with its sentences. |

## `SELECT` examples

Lists all AdaptiveMtFiles associated to an AdaptiveMtDataset.

```sql
SELECT
name,
createTime,
displayName,
entryCount,
updateTime
FROM google.translate.adaptive_mt_files
WHERE adaptiveMtDatasetsId = '{{ adaptiveMtDatasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified adaptive_mt_file resource.

```sql
DELETE FROM google.translate.adaptive_mt_files
WHERE adaptiveMtDatasetsId = '{{ adaptiveMtDatasetsId }}'
AND adaptiveMtFilesId = '{{ adaptiveMtFilesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
