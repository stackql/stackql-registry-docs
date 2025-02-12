---
title: service_connection_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_tokens
  - networkconnectivity
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

Creates, updates, deletes, gets or lists a <code>service_connection_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_connection_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.service_connection_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of a ServiceConnectionToken. Format: projects/{project}/locations/{location}/ServiceConnectionTokens/{service_connection_token} See: https://google.aip.dev/122#fields-representing-resource-names |
| <CopyableCode code="description" /> | `string` | A description of this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the ServiceConnectionToken was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="expireTime" /> | `string` | Output only. The time to which this token is valid. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | The resource path of the network associated with this token. Example: projects/{projectNumOrId}/global/networks/{resourceId}. |
| <CopyableCode code="token" /> | `string` | Output only. The token generated by Automation. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the ServiceConnectionToken was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceConnectionTokensId" /> | Gets details of a single ServiceConnectionToken. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceConnectionTokens in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServiceConnectionToken in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceConnectionTokensId" /> | Deletes a single ServiceConnectionToken. |

## `SELECT` examples

Lists ServiceConnectionTokens in a given project and location.

```sql
SELECT
name,
description,
createTime,
etag,
expireTime,
labels,
network,
token,
updateTime
FROM google.networkconnectivity.service_connection_tokens
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_connection_tokens</code> resource.

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
INSERT INTO google.networkconnectivity.service_connection_tokens (
locationsId,
projectsId,
name,
labels,
description,
network,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ description }}',
'{{ network }}',
'{{ etag }}'
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
    - name: description
      value: string
    - name: network
      value: string
    - name: token
      value: string
    - name: expireTime
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>service_connection_tokens</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkconnectivity.service_connection_tokens
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceConnectionTokensId = '{{ serviceConnectionTokensId }}';
```
