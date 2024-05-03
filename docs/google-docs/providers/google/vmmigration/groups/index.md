---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - vmmigration
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
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The Group name. |
| <CopyableCode code="description" /> | `string` | User-provided description of the group. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time timestamp. |
| <CopyableCode code="displayName" /> | `string` | Display name is a user defined name for this group which can be updated. |
| <CopyableCode code="migrationTargetType" /> | `string` | Immutable. The target type of this group. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The update time timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Gets details of a single Group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Groups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Group in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Deletes a single Group. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Groups in a given project and location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Updates the parameters of a single Group. |
