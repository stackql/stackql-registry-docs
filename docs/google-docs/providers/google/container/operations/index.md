---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - container
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
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="container.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="missingZones" /> | `array` | If any zones are listed here, the list of operations returned may be missing the operations from those zones. |
| <CopyableCode code="operations" /> | `array` | A list of operations in the project in the specified zone. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_operations_get" /> | `SELECT` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Gets the specified operation. |
| <CopyableCode code="projects_locations_operations_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all operations in a project in a specific zone or all zones. |
| <CopyableCode code="projects_zones_operations_get" /> | `SELECT` | <CopyableCode code="operationId, projectId, zone" /> | Gets the specified operation. |
| <CopyableCode code="projects_zones_operations_list" /> | `SELECT` | <CopyableCode code="projectId, zone" /> | Lists all operations in a project in a specific zone or all zones. |
| <CopyableCode code="projects_locations_operations_cancel" /> | `EXEC` | <CopyableCode code="locationsId, operationsId, projectsId" /> | Cancels the specified operation. |
| <CopyableCode code="projects_zones_operations_cancel" /> | `EXEC` | <CopyableCode code="operationId, projectId, zone" /> | Cancels the specified operation. |
