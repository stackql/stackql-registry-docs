---
title: annotations
hide_title: false
hide_table_of_contents: false
keywords:
  - annotations
  - rapidmigrationassessment
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

Creates, updates, deletes, gets or lists a <code>annotations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.rapidmigrationassessment.annotations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | name of resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time stamp. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of an annotation. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time stamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="annotationsId, locationsId, projectsId" /> | Gets details of a single Annotation. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Annotation |

## `SELECT` examples

Gets details of a single Annotation.

```sql
SELECT
name,
createTime,
labels,
type,
updateTime
FROM google.rapidmigrationassessment.annotations
WHERE annotationsId = '{{ annotationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>annotations</code> resource.

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
INSERT INTO google.rapidmigrationassessment.annotations (
locationsId,
projectsId,
name,
labels,
type
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: labels
      value: '{{ labels }}'
    - name: type
      value: '{{ type }}'

```
</TabItem>
</Tabs>
