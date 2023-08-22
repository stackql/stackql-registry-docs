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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.session_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the session template. |
| `description` | `string` | Optional. Brief description of the template. |
| `runtimeConfig` | `object` | Runtime configuration for a workload. |
| `updateTime` | `string` | Output only. The time template was last updated. |
| `createTime` | `string` | Output only. The time when the template was created. |
| `creator` | `string` | Output only. The email address of the user who created the template. |
| `jupyterSession` | `object` | Jupyter configuration for an interactive session. |
| `labels` | `object` | Optional. The labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| `environmentConfig` | `object` | Environment configuration for a workload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_session_templates_get` | `SELECT` | `locationsId, projectsId, sessionTemplatesId` | Gets the resource representation for a session template. |
| `projects_locations_session_templates_list` | `SELECT` | `locationsId, projectsId` | Lists session templates. |
| `projects_locations_session_templates_create` | `INSERT` | `locationsId, projectsId` | Create an session template, synchronously. |
| `projects_locations_session_templates_delete` | `DELETE` | `locationsId, projectsId, sessionTemplatesId` | Deletes a session template. |
| `_projects_locations_session_templates_list` | `EXEC` | `locationsId, projectsId` | Lists session templates. |
| `projects_locations_session_templates_patch` | `EXEC` | `locationsId, projectsId, sessionTemplatesId` | Updates the session template, synchronously.Disable check for update_mask, because all updates will be full replacements. |
