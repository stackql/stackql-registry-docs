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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>service_project_attachments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_project_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.service_project_attachments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of a ServiceProjectAttachment. Format: "projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}." |
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

## `SELECT` examples

Lists service projects attached to the host project.

```sql
SELECT
name,
createTime,
serviceProject,
state,
uid
FROM google.apphub.service_project_attachments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_project_attachments</code> resource.

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
INSERT INTO google.apphub.service_project_attachments (
locationsId,
projectsId,
name,
serviceProject
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ serviceProject }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
serviceProject: string
createTime: string
uid: string
state: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>service_project_attachments</code> resource.

```sql
/*+ delete */
DELETE FROM google.apphub.service_project_attachments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceProjectAttachmentsId = '{{ serviceProjectAttachmentsId }}';
```
