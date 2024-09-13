---
title: custom_target_types
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_target_types
  - clouddeploy
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

Creates, updates, deletes, gets or lists a <code>custom_target_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_target_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.clouddeploy.custom_target_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the `CustomTargetType`. Format is `projects/{project}/locations/{location}/customTargetTypes/{customTargetType}`. The `customTargetType` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the `CustomTargetType`. Max length is 255 characters. |
| <CopyableCode code="annotations" /> | `object` | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time at which the `CustomTargetType` was created. |
| <CopyableCode code="customActions" /> | `object` | CustomTargetSkaffoldActions represents the `CustomTargetType` configuration using Skaffold custom actions. |
| <CopyableCode code="customTargetTypeId" /> | `string` | Output only. Resource id of the `CustomTargetType`. |
| <CopyableCode code="etag" /> | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
| <CopyableCode code="uid" /> | `string` | Output only. Unique identifier of the `CustomTargetType`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Most recent time at which the `CustomTargetType` was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Gets details of a single CustomTargetType. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists CustomTargetTypes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new CustomTargetType in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Deletes a single CustomTargetType. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="customTargetTypesId, locationsId, projectsId" /> | Updates a single CustomTargetType. |

## `SELECT` examples

Lists CustomTargetTypes in a given project and location.

```sql
SELECT
name,
description,
annotations,
createTime,
customActions,
customTargetTypeId,
etag,
labels,
uid,
updateTime
FROM google.clouddeploy.custom_target_types
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_target_types</code> resource.

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
INSERT INTO google.clouddeploy.custom_target_types (
locationsId,
projectsId,
name,
customTargetTypeId,
uid,
description,
annotations,
labels,
createTime,
updateTime,
etag,
customActions
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ customTargetTypeId }}',
'{{ uid }}',
'{{ description }}',
'{{ annotations }}',
'{{ labels }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ etag }}',
'{{ customActions }}'
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
      - name: customTargetTypeId
        value: '{{ customTargetTypeId }}'
      - name: uid
        value: '{{ uid }}'
      - name: description
        value: '{{ description }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: customActions
        value: '{{ customActions }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_target_types</code> resource.

```sql
/*+ update */
UPDATE google.clouddeploy.custom_target_types
SET 
name = '{{ name }}',
customTargetTypeId = '{{ customTargetTypeId }}',
uid = '{{ uid }}',
description = '{{ description }}',
annotations = '{{ annotations }}',
labels = '{{ labels }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
etag = '{{ etag }}',
customActions = '{{ customActions }}'
WHERE 
customTargetTypesId = '{{ customTargetTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>custom_target_types</code> resource.

```sql
/*+ delete */
DELETE FROM google.clouddeploy.custom_target_types
WHERE customTargetTypesId = '{{ customTargetTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
