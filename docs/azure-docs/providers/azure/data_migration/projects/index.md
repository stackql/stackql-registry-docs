---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - data_migration
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Project-specific properties |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` |  | The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource. |
| <CopyableCode code="update" /> | `EXEC` |  | The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project. |
