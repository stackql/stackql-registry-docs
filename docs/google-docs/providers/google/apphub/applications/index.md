---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - apphub
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apphub.applications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of an Application. Format: "projects/&#123;host-project-id&#125;/locations/&#123;location&#125;/applications/&#123;application-id&#125;" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of an Application. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Application. Can have a maximum length of 63 characters. |
| <CopyableCode code="scope" /> | `object` | Scope of an application. |
| <CopyableCode code="state" /> | `string` | Output only. Application state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (in UUID4 format) for the `Application`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Gets an Application in a host project and location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Applications in a host project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Application in a host project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Deletes an Application in a host project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Applications in a host project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Updates an Application in a host project and location. |
