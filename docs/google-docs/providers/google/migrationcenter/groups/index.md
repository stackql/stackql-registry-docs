---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - migrationcenter
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The name of the group. |
| <CopyableCode code="description" /> | `string` | Optional. The description of the group. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the group was created. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-friendly display name. |
| <CopyableCode code="labels" /> | `object` | Labels as key value pairs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the group was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Gets the details of a group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all groups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new group in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Deletes a group. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Updates the parameters of a group. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all groups in a given project and location. |
