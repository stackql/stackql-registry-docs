---
title: custom_classes
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_classes
  - speech
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

Creates, updates, deletes, gets or lists a <code>custom_classes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_classes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.speech.custom_classes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="value" /> | `string` | The class item's value. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Get a custom class. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List custom classes. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a custom class. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Delete a custom class. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="customClassesId, locationsId, projectsId" /> | Update a custom class. |

## `SELECT` examples

List custom classes.

```sql
SELECT
value
FROM google.speech.custom_classes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_classes</code> resource.

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
INSERT INTO google.speech.custom_classes (
locationsId,
projectsId,
customClassId,
customClass
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ customClassId }}',
'{{ customClass }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: customClassId
      value: string
    - name: customClass
      value:
        - name: name
          value: string
        - name: customClassId
          value: string
        - name: items
          value:
            - - name: value
                value: string
        - name: kmsKeyName
          value: string
        - name: kmsKeyVersionName
          value: string
        - name: uid
          value: string
        - name: displayName
          value: string
        - name: state
          value: string
        - name: deleteTime
          value: string
        - name: expireTime
          value: string
        - name: annotations
          value: object
        - name: etag
          value: string
        - name: reconciling
          value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_classes</code> resource.

```sql
/*+ update */
UPDATE google.speech.custom_classes
SET 
name = '{{ name }}',
customClassId = '{{ customClassId }}',
items = '{{ items }}'
WHERE 
customClassesId = '{{ customClassesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>custom_classes</code> resource.

```sql
/*+ delete */
DELETE FROM google.speech.custom_classes
WHERE customClassesId = '{{ customClassesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
