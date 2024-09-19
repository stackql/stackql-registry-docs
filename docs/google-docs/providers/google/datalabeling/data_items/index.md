---
title: data_items
hide_title: false
hide_table_of_contents: false
keywords:
  - data_items
  - datalabeling
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

Creates, updates, deletes, gets or lists a <code>data_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.data_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the data item, in format of: projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id} |
| <CopyableCode code="imagePayload" /> | `object` | Container of information about an image. |
| <CopyableCode code="textPayload" /> | `object` | Container of information about a piece of text. |
| <CopyableCode code="videoPayload" /> | `object` | Container of information of a video. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_data_items_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, dataItemsId, datasetsId, projectsId" /> | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| <CopyableCode code="projects_datasets_annotated_datasets_data_items_list" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |
| <CopyableCode code="projects_datasets_data_items_get" /> | `SELECT` | <CopyableCode code="dataItemsId, datasetsId, projectsId" /> | Gets a data item in a dataset by resource name. This API can be called after data are imported into dataset. |
| <CopyableCode code="projects_datasets_data_items_list" /> | `SELECT` | <CopyableCode code="datasetsId, projectsId" /> | Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported. |

## `SELECT` examples

Lists data items in a dataset. This API can be called after data are imported into dataset. Pagination is supported.

```sql
SELECT
name,
imagePayload,
textPayload,
videoPayload
FROM google.datalabeling.data_items
WHERE datasetsId = '{{ datasetsId }}'
AND projectsId = '{{ projectsId }}';
```
