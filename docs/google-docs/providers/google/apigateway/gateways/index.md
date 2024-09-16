---
title: gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - gateways
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

Creates, updates, deletes, gets or lists a <code>gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigateway.gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name of the Gateway. Format: projects/{project}/locations/{location}/gateways/{gateway} |
| <CopyableCode code="apiConfig" /> | `string` | Required. Resource name of the API Config for this Gateway. Format: projects/{project}/locations/global/apis/{api}/configs/{apiConfig} |
| <CopyableCode code="createTime" /> | `string` | Output only. Created time. |
| <CopyableCode code="defaultHostname" /> | `string` | Output only. The default API Gateway host name of the form `{gateway_id}-{hash}.{region_code}.gateway.dev`. |
| <CopyableCode code="displayName" /> | `string` | Optional. Display name. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the Gateway. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Updated time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Gets details of a single Gateway. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Gateways in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Gateway in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Deletes a single Gateway. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="gatewaysId, locationsId, projectsId" /> | Updates the parameters of a single Gateway. |

## `SELECT` examples

Lists Gateways in a given project and location.

```sql
SELECT
name,
apiConfig,
createTime,
defaultHostname,
displayName,
labels,
state,
updateTime
FROM google.apigateway.gateways
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>gateways</code> resource.

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
INSERT INTO google.apigateway.gateways (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
displayName,
apiConfig,
state,
defaultHostname
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ displayName }}',
'{{ apiConfig }}',
'{{ state }}',
'{{ defaultHostname }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: apiConfig
      value: '{{ apiConfig }}'
    - name: state
      value: '{{ state }}'
    - name: defaultHostname
      value: '{{ defaultHostname }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>gateways</code> resource.

```sql
/*+ update */
UPDATE google.apigateway.gateways
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
displayName = '{{ displayName }}',
apiConfig = '{{ apiConfig }}',
state = '{{ state }}',
defaultHostname = '{{ defaultHostname }}'
WHERE 
gatewaysId = '{{ gatewaysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>gateways</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigateway.gateways
WHERE gatewaysId = '{{ gatewaysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
