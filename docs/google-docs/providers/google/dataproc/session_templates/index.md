---
title: session_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - session_templates
  - dataproc
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

Creates, updates, deletes, gets or lists a <code>session_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.session_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the session template. |
| <CopyableCode code="description" /> | `string` | Optional. Brief description of the template. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the template was created. |
| <CopyableCode code="creator" /> | `string` | Output only. The email address of the user who created the template. |
| <CopyableCode code="environmentConfig" /> | `object` | Environment configuration for a workload. |
| <CopyableCode code="jupyterSession" /> | `object` | Jupyter configuration for an interactive session. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty, but, if present, must contain 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| <CopyableCode code="runtimeConfig" /> | `object` | Runtime configuration for a workload. |
| <CopyableCode code="sparkConnectSession" /> | `object` | Spark connect configuration for an interactive session. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the template was last updated. |
| <CopyableCode code="uuid" /> | `string` | Output only. A session template UUID (Unique Universal Identifier). The service generates this value when it creates the session template. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_session_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Gets the resource representation for a session template. |
| <CopyableCode code="projects_locations_session_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists session templates. |
| <CopyableCode code="projects_locations_session_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create a session template synchronously. |
| <CopyableCode code="projects_locations_session_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Deletes a session template. |
| <CopyableCode code="projects_locations_session_templates_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Updates the session template synchronously. |

## `SELECT` examples

Lists session templates.

```sql
SELECT
name,
description,
createTime,
creator,
environmentConfig,
jupyterSession,
labels,
runtimeConfig,
sparkConnectSession,
updateTime,
uuid
FROM google.dataproc.session_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>session_templates</code> resource.

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
INSERT INTO google.dataproc.session_templates (
locationsId,
projectsId,
name,
description,
createTime,
jupyterSession,
sparkConnectSession,
creator,
labels,
runtimeConfig,
environmentConfig,
updateTime,
uuid
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ jupyterSession }}',
'{{ sparkConnectSession }}',
'{{ creator }}',
'{{ labels }}',
'{{ runtimeConfig }}',
'{{ environmentConfig }}',
'{{ updateTime }}',
'{{ uuid }}'
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
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: jupyterSession
        value: '{{ jupyterSession }}'
      - name: sparkConnectSession
        value: '{{ sparkConnectSession }}'
      - name: creator
        value: '{{ creator }}'
      - name: labels
        value: '{{ labels }}'
      - name: runtimeConfig
        value: '{{ runtimeConfig }}'
      - name: environmentConfig
        value: '{{ environmentConfig }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: uuid
        value: '{{ uuid }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>session_templates</code> resource.

```sql
/*+ update */
UPDATE google.dataproc.session_templates
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
jupyterSession = '{{ jupyterSession }}',
sparkConnectSession = '{{ sparkConnectSession }}',
creator = '{{ creator }}',
labels = '{{ labels }}',
runtimeConfig = '{{ runtimeConfig }}',
environmentConfig = '{{ environmentConfig }}',
updateTime = '{{ updateTime }}',
uuid = '{{ uuid }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sessionTemplatesId = '{{ sessionTemplatesId }}';
```

## `DELETE` example

Deletes the specified <code>session_templates</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.session_templates
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sessionTemplatesId = '{{ sessionTemplatesId }}';
```
