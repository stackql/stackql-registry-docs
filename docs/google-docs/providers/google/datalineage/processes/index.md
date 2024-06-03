---
title: processes
hide_title: false
hide_table_of_contents: false
keywords:
  - processes
  - datalineage
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
<tr><td><b>Name</b></td><td><code>processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datalineage.processes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the lineage process. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/processes/&#123;process&#125;`. Can be specified or auto-assigned. &#123;process&#125; must be not longer than 200 characters and only contain characters in a set: `a-zA-Z0-9_-:.` |
| <CopyableCode code="attributes" /> | `object` | Optional. The attributes of the process. Should only be used for the purpose of non-semantic management (classifying, describing or labeling the process). Up to 100 attributes are allowed. |
| <CopyableCode code="displayName" /> | `string` | Optional. A human-readable name you can set to display in a user interface. Must be not longer than 200 characters and only contain UTF-8 letters or numbers, spaces or characters like `_-:&.` |
| <CopyableCode code="origin" /> | `object` | Origin of a process. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, processesId, projectsId" /> | Gets the details of the specified process. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | List processes in the given project and location. List order is descending by insertion time. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new process. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, processesId, projectsId" /> | Deletes the process with the specified name. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, processesId, projectsId" /> | Updates a process. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | List processes in the given project and location. List order is descending by insertion time. |
