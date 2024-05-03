---
title: workspace_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_private_link_resources
  - healthcare
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>workspace_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.healthcare.workspace_private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a private link resource that need to be created for a workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the private link resources that need to be created for a workspace. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the private link resources that need to be created for a workspace. |
