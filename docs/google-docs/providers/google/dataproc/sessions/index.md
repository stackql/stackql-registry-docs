---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
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

Creates, updates, deletes, gets or lists a <code>sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.sessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the session. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the session was created. |
| <CopyableCode code="creator" /> | `string` | Output only. The email address of the user who created the session. |
| <CopyableCode code="environmentConfig" /> | `object` | Environment configuration for a workload. |
| <CopyableCode code="jupyterSession" /> | `object` | Jupyter configuration for an interactive session. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with the session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| <CopyableCode code="runtimeConfig" /> | `object` | Runtime configuration for a workload. |
| <CopyableCode code="runtimeInfo" /> | `object` | Runtime information about workload execution. |
| <CopyableCode code="sessionTemplate" /> | `string` | Optional. The session template used by the session.Only resource names, including project ID and location, are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]The template must be in the same project and Dataproc region as the session. |
| <CopyableCode code="sparkConnectSession" /> | `object` | Spark connect configuration for an interactive session. |
| <CopyableCode code="state" /> | `string` | Output only. A state of the session. |
| <CopyableCode code="stateHistory" /> | `array` | Output only. Historical state information for the session. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Session state details, such as the failure description if the state is FAILED. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time when the session entered the current state. |
| <CopyableCode code="user" /> | `string` | Optional. The email address of the user who owns the session. |
| <CopyableCode code="uuid" /> | `string` | Output only. A session UUID (Unique Universal Identifier). The service generates this value when it creates the session. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_sessions_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Gets the resource representation for an interactive session. |
| <CopyableCode code="projects_locations_sessions_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists interactive sessions. |
| <CopyableCode code="projects_locations_sessions_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create an interactive session asynchronously. |
| <CopyableCode code="projects_locations_sessions_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Deletes the interactive session resource. If the session is not in terminal state, it is terminated, and then deleted. |
| <CopyableCode code="projects_locations_sessions_terminate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Terminates the interactive session. |

## `SELECT` examples

Lists interactive sessions.

```sql
SELECT
name,
createTime,
creator,
environmentConfig,
jupyterSession,
labels,
runtimeConfig,
runtimeInfo,
sessionTemplate,
sparkConnectSession,
state,
stateHistory,
stateMessage,
stateTime,
user,
uuid
FROM google.dataproc.sessions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sessions</code> resource.

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
INSERT INTO google.dataproc.sessions (
locationsId,
projectsId,
name,
jupyterSession,
sparkConnectSession,
labels,
runtimeConfig,
environmentConfig,
user,
sessionTemplate
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ jupyterSession }}',
'{{ sparkConnectSession }}',
'{{ labels }}',
'{{ runtimeConfig }}',
'{{ environmentConfig }}',
'{{ user }}',
'{{ sessionTemplate }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: uuid
      value: string
    - name: createTime
      value: string
    - name: jupyterSession
      value:
        - name: kernel
          value: string
        - name: displayName
          value: string
    - name: sparkConnectSession
      value: []
    - name: runtimeInfo
      value:
        - name: endpoints
          value: object
        - name: outputUri
          value: string
        - name: diagnosticOutputUri
          value: string
        - name: approximateUsage
          value:
            - name: milliDcuSeconds
              value: string
            - name: shuffleStorageGbSeconds
              value: string
            - name: milliAcceleratorSeconds
              value: string
            - name: acceleratorType
              value: string
        - name: currentUsage
          value:
            - name: milliDcu
              value: string
            - name: shuffleStorageGb
              value: string
            - name: milliDcuPremium
              value: string
            - name: shuffleStorageGbPremium
              value: string
            - name: milliAccelerator
              value: string
            - name: acceleratorType
              value: string
            - name: snapshotTime
              value: string
    - name: state
      value: string
    - name: stateMessage
      value: string
    - name: stateTime
      value: string
    - name: creator
      value: string
    - name: labels
      value: object
    - name: runtimeConfig
      value:
        - name: version
          value: string
        - name: containerImage
          value: string
        - name: properties
          value: object
        - name: repositoryConfig
          value:
            - name: pypiRepositoryConfig
              value:
                - name: pypiRepository
                  value: string
        - name: autotuningConfig
          value:
            - name: scenarios
              value:
                - string
        - name: cohort
          value: string
    - name: environmentConfig
      value:
        - name: executionConfig
          value:
            - name: serviceAccount
              value: string
            - name: networkUri
              value: string
            - name: subnetworkUri
              value: string
            - name: networkTags
              value:
                - string
            - name: kmsKey
              value: string
            - name: idleTtl
              value: string
            - name: ttl
              value: string
            - name: stagingBucket
              value: string
        - name: peripheralsConfig
          value:
            - name: metastoreService
              value: string
            - name: sparkHistoryServerConfig
              value:
                - name: dataprocCluster
                  value: string
    - name: user
      value: string
    - name: stateHistory
      value:
        - - name: state
            value: string
          - name: stateMessage
            value: string
          - name: stateStartTime
            value: string
    - name: sessionTemplate
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sessions</code> resource.

```sql
/*+ delete */
DELETE FROM google.dataproc.sessions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sessionsId = '{{ sessionsId }}';
```
