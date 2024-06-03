---
title: service_project_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - service_project_attachments
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
<tr><td><b>Name</b></td><td><code>service_project_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.service_project_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of a ServiceProjectAttachment. Format: "projects/&#123;host-project-id&#125;/locations/global/serviceProjectAttachments/&#123;service-project-id&#125;." |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="serviceProject" /> | `string` | Required. Immutable. Service project name in the format: "projects/abc" or "projects/123". As input, project name with either project id or number are accepted. As output, this field will contain project number. |
| <CopyableCode code="state" /> | `string` | Output only. ServiceProjectAttachment state. |
| <CopyableCode code="uid" /> | `string` | Output only. A globally unique identifier (in UUID4 format) for the `ServiceProjectAttachment`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceProjectAttachmentsId" /> | Gets a service project attachment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists service projects attached to the host project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Attaches a service project to the host project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceProjectAttachmentsId" /> | Deletes a service project attachment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists service projects attached to the host project. |
