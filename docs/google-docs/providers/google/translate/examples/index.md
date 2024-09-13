
---
title: examples
hide_title: false
hide_table_of_contents: false
keywords:
  - examples
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

Creates, updates, deletes or gets an <code>example</code> resource or lists <code>examples</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>examples</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.examples" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the example, in form of `projects/{project-number-or-id}/locations/{location_id}/datasets/{dataset_id}/examples/{example_id}` |
| <CopyableCode code="sourceText" /> | `string` | Sentence in source language. |
| <CopyableCode code="targetText" /> | `string` | Sentence in target language. |
| <CopyableCode code="usage" /> | `string` | Output only. Usage of the sentence pair. Options are TRAIN|VALIDATION|TEST. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_datasets_examples_list" /> | `SELECT` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Lists sentence pairs in the dataset. |

## `SELECT` examples

Lists sentence pairs in the dataset.

```sql
SELECT
name,
sourceText,
targetText,
usage
FROM google.translate.examples
WHERE datasetsId = '{{ datasetsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
