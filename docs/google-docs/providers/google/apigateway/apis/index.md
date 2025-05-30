---
title: apis
hide_title: false
hide_table_of_contents: false
keywords:
  - apis
  - apigateway
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

Creates, updates, deletes, gets or lists a <code>apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigateway.apis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the API. Format: projects/{project}/locations/global/apis/{api} |
| <CopyableCode code="createTime" /> | `string` | Output only. Created time. |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| <CopyableCode code="managedService" /> | `string` | Optional. Immutable. The name of a Google Managed Service ( https://cloud.google.com/service-infrastructure/docs/glossary#managed). If not specified, a new Service will automatically be created in the same project as this API. |
| <CopyableCode code="state" /> | `string` | Output only. State of the API. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Updated time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId" /> | Gets details of a single Api. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Apis in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Api in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apisId, locationsId, projectsId" /> | Deletes a single Api. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="apisId, locationsId, projectsId" /> | Updates the parameters of a single Api. |

## `SELECT` examples

Lists Apis in a given project and location.

```sql
SELECT
name,
createTime,
displayName,
labels,
managedService,
state,
updateTime
FROM google.apigateway.apis
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apis</code> resource.

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
INSERT INTO google.apigateway.apis (
locationsId,
projectsId,
labels,
displayName,
managedService
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ displayName }}',
'{{ managedService }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: labels
      value: object
    - name: displayName
      value: string
    - name: managedService
      value: string
    - name: state
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apis</code> resource.

```sql
/*+ update */
UPDATE google.apigateway.apis
SET 
labels = '{{ labels }}',
displayName = '{{ displayName }}',
managedService = '{{ managedService }}'
WHERE 
apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>apis</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigateway.apis
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
