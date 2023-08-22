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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the session. |
| `user` | `string` | Optional. The email address of the user who owns the session. |
| `state` | `string` | Output only. A state of the session. |
| `stateTime` | `string` | Output only. The time when the session entered a current state. |
| `sessionTemplate` | `string` | Optional. The session template used by the session.Only resource names including project ID and location are valid.Example: * https://www.googleapis.com/compute/v1/projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id] * projects/[project_id]/locations/[dataproc_region]/sessionTemplates/[template_id]Note that the template must be in the same project and Dataproc region. |
| `jupyterSession` | `object` | Jupyter configuration for an interactive session. |
| `stateHistory` | `array` | Output only. Historical state information for the session. |
| `labels` | `object` | Optional. The labels to associate with this session. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| `environmentConfig` | `object` | Environment configuration for a workload. |
| `uuid` | `string` | Output only. A session UUID (Unique Universal Identifier). The service generates this value when it creates the session. |
| `createTime` | `string` | Output only. The time when the session was created. |
| `stateMessage` | `string` | Output only. Session state details, such as a failure description if the state is FAILED. |
| `creator` | `string` | Output only. The email address of the user who created the session. |
| `runtimeConfig` | `object` | Runtime configuration for a workload. |
| `runtimeInfo` | `object` | Runtime information about workload execution. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_sessions_get` | `SELECT` | `locationsId, projectsId, sessionsId` | Gets the resource representation for an interactive session. |
| `projects_locations_sessions_list` | `SELECT` | `locationsId, projectsId` | Lists interactive sessions. |
| `projects_locations_sessions_create` | `INSERT` | `locationsId, projectsId` | Create an interactive session asynchronously. |
| `projects_locations_sessions_delete` | `DELETE` | `locationsId, projectsId, sessionsId` | Deletes the interactive session resource. If the session is not in terminal state, it will be terminated and deleted afterwards. |
| `_projects_locations_sessions_list` | `EXEC` | `locationsId, projectsId` | Lists interactive sessions. |
| `projects_locations_sessions_inject_credentials` | `EXEC` | `locationsId, projectsId, sessionsId` | Inject Credentials in the interactive session. |
| `projects_locations_sessions_terminate` | `EXEC` | `locationsId, projectsId, sessionsId` | Terminates the interactive session. |
