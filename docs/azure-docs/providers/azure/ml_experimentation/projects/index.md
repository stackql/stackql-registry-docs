---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - ml_experimentation
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_experimentation.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This cannot be changed after the resource is created. |
| <CopyableCode code="properties" /> | `object` | The properties of a machine learning project. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, projectName, resourceGroupName, subscriptionId, workspaceName" /> | Gets the properties of the specified machine learning project. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all the available machine learning projects under the specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, projectName, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a project with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, projectName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a project. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, workspaceName" /> | Lists all the available machine learning projects under the specified workspace. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, projectName, resourceGroupName, subscriptionId, workspaceName" /> | Updates a project with the specified parameters. |
