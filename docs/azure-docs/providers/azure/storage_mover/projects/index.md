---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - storage_mover
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.projects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Project properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets a Project resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Projects in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates or updates a Project resource, which is a logical grouping of related jobs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes a Project resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Projects in a Storage Mover. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for a Project resource. Properties not specified in the request body will be unchanged. |
