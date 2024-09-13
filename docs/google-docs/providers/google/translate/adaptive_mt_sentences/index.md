---
title: adaptive_mt_sentences
hide_title: false
hide_table_of_contents: false
keywords:
  - adaptive_mt_sentences
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

Creates, updates, deletes, gets or lists a <code>adaptive_mt_sentences</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adaptive_mt_sentences</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.adaptive_mt_sentences" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the file, in form of `projects/{project-number-or-id}/locations/{location_id}/adaptiveMtDatasets/{dataset}/adaptiveMtFiles/{file}/adaptiveMtSentences/{sentence}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this sentence was created. |
| <CopyableCode code="sourceSentence" /> | `string` | Required. The source sentence. |
| <CopyableCode code="targetSentence" /> | `string` | Required. The target sentence. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this sentence was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_files_adaptive_mt_sentences_list" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, adaptiveMtFilesId, locationsId, projectsId" /> | Lists all AdaptiveMtSentences under a given file/dataset. |
| <CopyableCode code="projects_locations_adaptive_mt_datasets_adaptive_mt_sentences_list" /> | `SELECT` | <CopyableCode code="adaptiveMtDatasetsId, locationsId, projectsId" /> | Lists all AdaptiveMtSentences under a given file/dataset. |

## `SELECT` examples

Lists all AdaptiveMtSentences under a given file/dataset.

```sql
SELECT
name,
createTime,
sourceSentence,
targetSentence,
updateTime
FROM google.translate.adaptive_mt_sentences
WHERE adaptiveMtDatasetsId = '{{ adaptiveMtDatasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
