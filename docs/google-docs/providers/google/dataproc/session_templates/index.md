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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>session_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dataproc.session_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the session template. |
| <CopyableCode code="description" /> | `string` | Optional. Brief description of the template. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the template was created. |
| <CopyableCode code="creator" /> | `string` | Output only. The email address of the user who created the template. |
| <CopyableCode code="environmentConfig" /> | `object` | Environment configuration for a workload. |
| <CopyableCode code="jupyterSession" /> | `object` | Jupyter configuration for an interactive session. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels to associate with sessions created using this template. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a session. |
| <CopyableCode code="runtimeConfig" /> | `object` | Runtime configuration for a workload. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time template was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_session_templates_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Gets the resource representation for a session template. |
| <CopyableCode code="projects_locations_session_templates_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists session templates. |
| <CopyableCode code="projects_locations_session_templates_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Create an session template, synchronously. |
| <CopyableCode code="projects_locations_session_templates_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Deletes a session template. |
| <CopyableCode code="_projects_locations_session_templates_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists session templates. |
| <CopyableCode code="projects_locations_session_templates_patch" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, sessionTemplatesId" /> | Updates the session template, synchronously.Disable check for update_mask, because all updates will be full replacements. |
