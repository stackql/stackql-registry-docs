---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>analyses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis} |
| <CopyableCode code="analysisResult" /> | `object` | The result of an analysis. |
| <CopyableCode code="annotatorSelector" /> | `object` | Selector of all available annotators and phrase matchers to run. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the analysis was created, which occurs when the long-running operation completes. |
| <CopyableCode code="requestTime" /> | `string` | Output only. The time at which the analysis was requested. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Gets an analysis. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Lists analyses. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Creates an analysis. The long running operation is done when the analysis has completed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="analysesId, conversationsId, locationsId, projectsId" /> | Deletes an analysis. |

## `SELECT` examples

Lists analyses.

```sql
SELECT
name,
analysisResult,
annotatorSelector,
createTime,
requestTime
FROM google.contactcenterinsights.analyses
WHERE conversationsId = '{{ conversationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>analyses</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.contactcenterinsights.analyses (
conversationsId,
locationsId,
projectsId,
requestTime,
name,
analysisResult,
createTime,
annotatorSelector
)
SELECT 
'{{ conversationsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ requestTime }}',
'{{ name }}',
'{{ analysisResult }}',
'{{ createTime }}',
'{{ annotatorSelector }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: requestTime
        value: '{{ requestTime }}'
      - name: name
        value: '{{ name }}'
      - name: analysisResult
        value: '{{ analysisResult }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: annotatorSelector
        value: '{{ annotatorSelector }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>analyses</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.analyses
WHERE analysesId = '{{ analysesId }}'
AND conversationsId = '{{ conversationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
