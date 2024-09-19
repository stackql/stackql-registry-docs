---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - apphub
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

Creates, updates, deletes, gets or lists a <code>applications</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of an Application. Format: "projects/{host-project-id}/locations/{location}/applications/{application-id}" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of an Application. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Application. Can have a maximum length of 63 characters. |
| <CopyableCode code="scope" /> | `object` | Scope of an application. |
| <CopyableCode code="state" /> | `string` | Output only. Application state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (in UUID4 format) for the `Application`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Gets an Application in a host project and location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Applications in a host project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Application in a host project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Deletes an Application in a host project and location. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Updates an Application in a host project and location. |

## `SELECT` examples

Lists Applications in a host project and location.

```sql
SELECT
name,
description,
attributes,
createTime,
displayName,
scope,
state,
uid,
updateTime
FROM google.apphub.applications
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>applications</code> resource.

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
INSERT INTO google.apphub.applications (
locationsId,
projectsId,
name,
displayName,
description,
attributes,
scope
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ attributes }}',
'{{ scope }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: attributes
      value:
        - name: criticality
          value:
            - name: type
              value: string
        - name: environment
          value:
            - name: type
              value: string
        - name: developerOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
        - name: operatorOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
        - name: businessOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: scope
      value:
        - name: type
          value: string
    - name: uid
      value: string
    - name: state
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>applications</code> resource.

```sql
/*+ update */
UPDATE google.apphub.applications
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
attributes = '{{ attributes }}',
scope = '{{ scope }}'
WHERE 
applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>applications</code> resource.

```sql
/*+ delete */
DELETE FROM google.apphub.applications
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
