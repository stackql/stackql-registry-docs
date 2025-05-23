---
title: app_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - app_gateways
  - beyondcorp
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

Creates, updates, deletes, gets or lists a <code>app_gateways</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.beyondcorp.app_gateways" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Unique resource name of the AppGateway. The name is ignored when creating an AppGateway. |
| <CopyableCode code="allocatedConnections" /> | `array` | Output only. A list of connections allocated for the Gateway |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when the resource was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. An arbitrary user-provided name for the AppGateway. Cannot exceed 64 characters. |
| <CopyableCode code="hostType" /> | `string` | Required. The type of hosting used by the AppGateway. |
| <CopyableCode code="labels" /> | `object` | Optional. Resource labels to represent user provided metadata. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the AppGateway. |
| <CopyableCode code="type" /> | `string` | Required. The type of network connectivity used by the AppGateway. |
| <CopyableCode code="uid" /> | `string` | Output only. A unique identifier for the instance generated by the system. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when the resource was last modified. |
| <CopyableCode code="uri" /> | `string` | Output only. Server-defined URI for this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_app_gateways_get" /> | `SELECT` | <CopyableCode code="appGatewaysId, locationsId, projectsId" /> | Gets details of a single AppGateway. |
| <CopyableCode code="projects_locations_app_gateways_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists AppGateways in a given project and location. |
| <CopyableCode code="projects_locations_app_gateways_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new AppGateway in a given project and location. |
| <CopyableCode code="projects_locations_app_gateways_delete" /> | `DELETE` | <CopyableCode code="appGatewaysId, locationsId, projectsId" /> | Deletes a single AppGateway. |
| <CopyableCode code="projects_locations_app_gateways_should_throttle" /> | `EXEC` | <CopyableCode code="appGatewaysId, locationsId, projectsId" /> | Calls the Bouncer method ShouldThrottle to check if a request should be throttled. |

## `SELECT` examples

Lists AppGateways in a given project and location.

```sql
SELECT
name,
allocatedConnections,
createTime,
displayName,
hostType,
labels,
satisfiesPzi,
satisfiesPzs,
state,
type,
uid,
updateTime,
uri
FROM google.beyondcorp.app_gateways
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>app_gateways</code> resource.

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
INSERT INTO google.beyondcorp.app_gateways (
locationsId,
projectsId,
name,
labels,
displayName,
type,
hostType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ labels }}',
'{{ displayName }}',
'{{ type }}',
'{{ hostType }}'
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
    - name: uid
      value: string
    - name: type
      value: string
    - name: state
      value: string
    - name: uri
      value: string
    - name: allocatedConnections
      value:
        - - name: pscUri
            value: string
          - name: ingressPort
            value: integer
    - name: hostType
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: satisfiesPzi
      value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>app_gateways</code> resource.

```sql
/*+ delete */
DELETE FROM google.beyondcorp.app_gateways
WHERE appGatewaysId = '{{ appGatewaysId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
