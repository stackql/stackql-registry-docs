---
title: device_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - device_sessions
  - testing
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

Creates, updates, deletes, gets or lists a <code>device_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>device_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.testing.device_sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Optional. Name of the DeviceSession, e.g. "projects/{project_id}/deviceSessions/{session_id}" |
| <CopyableCode code="activeStartTime" /> | `string` | Output only. The timestamp that the session first became ACTIVE. |
| <CopyableCode code="androidDevice" /> | `object` | A single Android device. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time that the Session was created. |
| <CopyableCode code="displayName" /> | `string` | Output only. The title of the DeviceSession to be presented in the UI. |
| <CopyableCode code="expireTime" /> | `string` | Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED. |
| <CopyableCode code="inactivityTimeout" /> | `string` | Output only. The interval of time that this device must be interacted with before it transitions from ACTIVE to TIMEOUT_INACTIVITY. |
| <CopyableCode code="state" /> | `string` | Output only. Current state of the DeviceSession. |
| <CopyableCode code="stateHistories" /> | `array` | Output only. The historical state transitions of the session_state message including the current session state. |
| <CopyableCode code="ttl" /> | `string` | Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 15 minutes. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deviceSessionsId, projectsId" /> | GET /v1/projects/{project_id}/deviceSessions/{device_session_id} Return a DeviceSession, which documents the allocation status and whether the device is allocated. Clients making requests from this API must poll GetDeviceSession. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | GET /v1/projects/{project_id}/deviceSessions Lists device Sessions owned by the project user. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | POST /v1/projects/{project_id}/deviceSessions |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="deviceSessionsId, projectsId" /> | PATCH /v1/projects/{projectId}/deviceSessions/deviceSessionId}:updateDeviceSession Updates the current device session to the fields described by the update_mask. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deviceSessionsId, projectsId" /> | POST /v1/projects/{project_id}/deviceSessions/{device_session_id}:cancel Changes the DeviceSession to state FINISHED and terminates all connections. Canceled sessions are not deleted and can be retrieved or listed by the user until they expire based on the 28 day deletion policy. |

## `SELECT` examples

GET /v1/projects/{project_id}/deviceSessions Lists device Sessions owned by the project user.

```sql
SELECT
name,
activeStartTime,
androidDevice,
createTime,
displayName,
expireTime,
inactivityTimeout,
state,
stateHistories,
ttl
FROM google.testing.device_sessions
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>device_sessions</code> resource.

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
INSERT INTO google.testing.device_sessions (
projectsId,
name,
ttl,
expireTime,
androidDevice
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ ttl }}',
'{{ expireTime }}',
'{{ androidDevice }}'
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
    - name: state
      value: string
    - name: stateHistories
      value:
        - - name: sessionState
            value: string
          - name: eventTime
            value: string
          - name: stateMessage
            value: string
    - name: ttl
      value: string
    - name: expireTime
      value: string
    - name: inactivityTimeout
      value: string
    - name: createTime
      value: string
    - name: activeStartTime
      value: string
    - name: androidDevice
      value:
        - name: androidModelId
          value: string
        - name: androidVersionId
          value: string
        - name: locale
          value: string
        - name: orientation
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>device_sessions</code> resource.

```sql
/*+ update */
UPDATE google.testing.device_sessions
SET 
name = '{{ name }}',
ttl = '{{ ttl }}',
expireTime = '{{ expireTime }}',
androidDevice = '{{ androidDevice }}'
WHERE 
deviceSessionsId = '{{ deviceSessionsId }}'
AND projectsId = '{{ projectsId }}';
```
