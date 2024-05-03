---
title: groups_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_operations
  - migrate
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
<tr><td><b>Name</b></td><td><code>groups_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.groups_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, projectName, resourceGroupName, subscriptionId" /> | Get a Group |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List Group resources by AssessmentProject |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="groupName, projectName, resourceGroupName, subscriptionId" /> | Create a Group |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupName, projectName, resourceGroupName, subscriptionId" /> | Delete a Group |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List Group resources by AssessmentProject |
