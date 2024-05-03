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
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with this session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| <CopyableCode code="runtimeConfig" /> | `object` | Runtime configuration for a workload. |
| <CopyableCode code="runtimeInfo" /> | `object` | Runtime information about workload execution. |
| <CopyableCode code="sessionTemplate" /> | `string` | Optional. The session template used by the session.Only resource names including project ID and location are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]Note that the template must be in the same project and Dataproc region. |
| <CopyableCode code="state" /> | `string` | Output only. A state of the session. |
| <CopyableCode code="stateHistory" /> | `array` | Output only. Historical state information for the session. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Session state details, such as a failure description if the state is FAILED. |
| <CopyableCode code="stateTime" /> | `string` | Output only. The time when the session entered a current state. |
| <CopyableCode code="user" /> | `string` | Optional. The email address of the user who owns the session. |
| <CopyableCode code="uuid" /> | `string` | Output only. A session UUID (Unique Universal Identifier). The service generates this value when it creates the session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_sessions_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Gets the resource representation for an interactive session. |
| <CopyableCode code="projects_locations_sessions_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists interactive sessions. |
| <CopyableCode code="projects_locations_sessions_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create an interactive session asynchronously. |
| <CopyableCode code="projects_locations_sessions_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Deletes the interactive session resource. If the session is not in terminal state, it will be terminated and deleted afterwards. |
| <CopyableCode code="_projects_locations_sessions_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists interactive sessions. |
| <CopyableCode code="projects_locations_sessions_inject_credentials" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Inject Credentials in the interactive session. |
| <CopyableCode code="projects_locations_sessions_terminate" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sessionsId" /> | Terminates the interactive session. |
