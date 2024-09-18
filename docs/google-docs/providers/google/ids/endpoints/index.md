---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - ids
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

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.ids.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the endpoint. |
| <CopyableCode code="description" /> | `string` | User-provided description of the endpoint |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time timestamp. |
| <CopyableCode code="endpointForwardingRule" /> | `string` | Output only. The fully qualified URL of the endpoint's ILB Forwarding Rule. |
| <CopyableCode code="endpointIp" /> | `string` | Output only. The IP address of the IDS Endpoint's ILB. |
| <CopyableCode code="labels" /> | `object` | The labels of the endpoint. |
| <CopyableCode code="network" /> | `string` | Required. The fully qualified URL of the network to which the IDS Endpoint is attached. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. [Output Only] Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. [Output Only] Reserved for future use. |
| <CopyableCode code="severity" /> | `string` | Required. Lowest threat severity that this endpoint will alert on. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the endpoint. |
| <CopyableCode code="threatExceptions" /> | `array` | List of threat IDs to be excepted from generating alerts. |
| <CopyableCode code="trafficLogs" /> | `boolean` | Whether the endpoint should report traffic logs in addition to threat logs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Gets details of a single Endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Endpoints in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Endpoint in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Deletes a single Endpoint. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="endpointsId, locationsId, projectsId" /> | Updates the parameters of a single Endpoint. |

## `SELECT` examples

Lists Endpoints in a given project and location.

```sql
SELECT
name,
description,
createTime,
endpointForwardingRule,
endpointIp,
labels,
network,
satisfiesPzi,
satisfiesPzs,
severity,
state,
threatExceptions,
trafficLogs,
updateTime
FROM google.ids.endpoints
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

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
INSERT INTO google.ids.endpoints (
locationsId,
projectsId,
labels,
network,
description,
severity,
threatExceptions,
trafficLogs
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ network }}',
'{{ description }}',
'{{ severity }}',
'{{ threatExceptions }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
labels: object
network: string
endpointForwardingRule: string
endpointIp: string
description: string
severity: string
threatExceptions:
  - type: string
state: string
trafficLogs: boolean
satisfiesPzs: boolean
satisfiesPzi: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>endpoints</code> resource.

```sql
/*+ update */
UPDATE google.ids.endpoints
SET 
labels = '{{ labels }}',
network = '{{ network }}',
description = '{{ description }}',
severity = '{{ severity }}',
threatExceptions = '{{ threatExceptions }}',
trafficLogs = true|false
WHERE 
endpointsId = '{{ endpointsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.ids.endpoints
WHERE endpointsId = '{{ endpointsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
