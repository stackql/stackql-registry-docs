
---
title: evaluations
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluations
  - documentai
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

Creates, updates, deletes or gets an <code>evaluation</code> resource or lists <code>evaluations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>evaluations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.evaluations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the evaluation. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}/evaluations/{evaluation}` |
| <CopyableCode code="allEntitiesMetrics" /> | `object` | Metrics across multiple confidence levels. |
| <CopyableCode code="createTime" /> | `string` | The time that the evaluation was created. |
| <CopyableCode code="documentCounters" /> | `object` | Evaluation counters for the documents that were used. |
| <CopyableCode code="entityMetrics" /> | `object` | Metrics across confidence levels, for different entities. |
| <CopyableCode code="kmsKeyName" /> | `string` | The KMS key name used for encryption. |
| <CopyableCode code="kmsKeyVersionName" /> | `string` | The KMS key version with which data is encrypted. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_processors_processor_versions_evaluations_get" /> | `SELECT` | <CopyableCode code="evaluationsId, locationsId, processorVersionsId, processorsId, projectsId" /> | Retrieves a specific evaluation. |
| <CopyableCode code="projects_locations_processors_processor_versions_evaluations_list" /> | `SELECT` | <CopyableCode code="locationsId, processorVersionsId, processorsId, projectsId" /> | Retrieves a set of evaluations for a given processor version. |

## `SELECT` examples

Retrieves a set of evaluations for a given processor version.

```sql
SELECT
name,
allEntitiesMetrics,
createTime,
documentCounters,
entityMetrics,
kmsKeyName,
kmsKeyVersionName
FROM google.documentai.evaluations
WHERE locationsId = '{{ locationsId }}'
AND processorVersionsId = '{{ processorVersionsId }}'
AND processorsId = '{{ processorsId }}'
AND projectsId = '{{ projectsId }}'; 
```
