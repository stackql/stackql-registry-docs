---
title: migrate_project
hide_title: false
hide_table_of_contents: false
keywords:
  - migrate_project
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
<tr><td><b>Name</b></td><td><code>migrate_project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.migrate_project" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the relative URL to get this migrate project. |
| <CopyableCode code="name" /> | `string` | Gets the name of the migrate project. |
| <CopyableCode code="eTag" /> | `string` | Gets or sets the eTag for concurrency control. |
| <CopyableCode code="location" /> | `string` | Gets or sets the Azure location in which migrate project is created. |
| <CopyableCode code="properties" /> | `object` | Class for migrate project properties. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the tags. |
| <CopyableCode code="type" /> | `string` | Handled by resource provider. Type = Microsoft.Migrate/MigrateProject. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, migrateProjectName, resourceGroupName, subscriptionId" /> | Delete the migrate project. Deleting non-existent project is a no-operation. |
