---
title: solutions_solution
hide_title: false
hide_table_of_contents: false
keywords:
  - solutions_solution
  - migrate_projects
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solutions_solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.solutions_solution" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of this REST resource. |
| <CopyableCode code="etag" /> | `string` | Gets or sets the ETAG for optimistic concurrency control. |
| <CopyableCode code="properties" /> | `object` | Class for solution properties. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, solutionName, subscriptionId" /> | Delete the solution. Deleting non-existent project is a no-operation. |
