---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
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

Creates, updates, deletes, gets or lists a <code>examples</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>examples</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalabeling.examples" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the example, in format of: projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/ {annotated_dataset_id}/examples/{example_id} |
| <CopyableCode code="annotations" /> | `array` | Output only. Annotations for the piece of data in Example. One piece of data can have multiple annotations. |
| <CopyableCode code="imagePayload" /> | `object` | Container of information about an image. |
| <CopyableCode code="textPayload" /> | `object` | Container of information about a piece of text. |
| <CopyableCode code="videoPayload" /> | `object` | Container of information of a video. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_datasets_annotated_datasets_examples_get" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, examplesId, projectsId" /> | Gets an example by resource name, including both data and annotation. |
| <CopyableCode code="projects_datasets_annotated_datasets_examples_list" /> | `SELECT` | <CopyableCode code="annotatedDatasetsId, datasetsId, projectsId" /> | Lists examples in an annotated dataset. Pagination is supported. |

## `SELECT` examples

Lists examples in an annotated dataset. Pagination is supported.

```sql
SELECT
name,
annotations,
imagePayload,
textPayload,
videoPayload
FROM google.datalabeling.examples
WHERE annotatedDatasetsId = '{{ annotatedDatasetsId }}'
AND datasetsId = '{{ datasetsId }}'
AND projectsId = '{{ projectsId }}';
```
