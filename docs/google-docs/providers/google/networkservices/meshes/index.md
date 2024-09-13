---
title: meshes
hide_title: false
hide_table_of_contents: false
keywords:
  - meshes
  - networkservices
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

Creates, updates, deletes, gets or lists a <code>meshes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>meshes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.meshes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the Mesh resource. It matches pattern `projects/*/locations/global/meshes/`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="envoyHeaders" /> | `string` | Optional. Determines if envoy will insert internal debug headers into upstream requests. Other Envoy headers may still be injected. By default, envoy will not insert any debug headers. |
| <CopyableCode code="interceptionPort" /> | `integer` | Optional. If set to a valid TCP port (1-65535), instructs the SIDECAR proxy to listen on the specified port of localhost (127.0.0.1) address. The SIDECAR proxy will expect all traffic to be redirected to this port regardless of its actual ip:port destination. If unset, a port '15001' is used as the interception port. This is applicable only for sidecar proxy deployments. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the Mesh resource. |
| <CopyableCode code="selfLink" /> | `string` | Output only. Server-defined URL of this resource |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, meshesId, projectsId" /> | Gets details of a single Mesh. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Meshes in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Mesh in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, meshesId, projectsId" /> | Deletes a single Mesh. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, meshesId, projectsId" /> | Updates the parameters of a single Mesh. |

## `SELECT` examples

Lists Meshes in a given project and location.

```sql
SELECT
name,
description,
createTime,
envoyHeaders,
interceptionPort,
labels,
selfLink,
updateTime
FROM google.networkservices.meshes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>meshes</code> resource.

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
INSERT INTO google.networkservices.meshes (
locationsId,
projectsId,
name,
selfLink,
createTime,
updateTime,
labels,
description,
interceptionPort,
envoyHeaders
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ selfLink }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ interceptionPort }}',
'{{ envoyHeaders }}'
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
      - name: selfLink
        value: '{{ selfLink }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: interceptionPort
        value: '{{ interceptionPort }}'
      - name: envoyHeaders
        value: '{{ envoyHeaders }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>meshes</code> resource.

```sql
/*+ update */
UPDATE google.networkservices.meshes
SET 
name = '{{ name }}',
selfLink = '{{ selfLink }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
interceptionPort = '{{ interceptionPort }}',
envoyHeaders = '{{ envoyHeaders }}'
WHERE 
locationsId = '{{ locationsId }}'
AND meshesId = '{{ meshesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>meshes</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.meshes
WHERE locationsId = '{{ locationsId }}'
AND meshesId = '{{ meshesId }}'
AND projectsId = '{{ projectsId }}';
```
