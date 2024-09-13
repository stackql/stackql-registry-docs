---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
  - transcoder
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

Creates, updates, deletes, gets or lists a <code>job_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.transcoder.job_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the job template. Format: `projects/{project_number}/locations/{location}/jobTemplates/{job_template}` |
| <CopyableCode code="config" /> | `object` | Job configuration |
| <CopyableCode code="labels" /> | `object` | The labels associated with this job template. You can use these to organize and group your job templates. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Returns the job template data. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists job templates in the specified region. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a job template in the specified region. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobTemplatesId, locationsId, projectsId" /> | Deletes a job template. |

## `SELECT` examples

Lists job templates in the specified region.

```sql
SELECT
name,
config,
labels
FROM google.transcoder.job_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>job_templates</code> resource.

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
INSERT INTO google.transcoder.job_templates (
locationsId,
projectsId,
name,
config,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ config }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: config
        value: '{{ config }}'
      - name: labels
        value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>job_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.transcoder.job_templates
WHERE jobTemplatesId = '{{ jobTemplatesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
