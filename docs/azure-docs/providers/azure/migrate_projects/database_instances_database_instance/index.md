---
title: database_instances_database_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - database_instances_database_instance
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
<tr><td><b>Name</b></td><td><code>database_instances_database_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate_projects.database_instances_database_instance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the relative URL to get to this REST resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of this REST resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the database instance resource. |
| <CopyableCode code="type" /> | `string` | Gets the type of this REST resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, databaseInstanceName, migrateProjectName, resourceGroupName, subscriptionId" /> |
