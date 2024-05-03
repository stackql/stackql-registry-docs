---
title: machines_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - machines_operations
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
<tr><td><b>Name</b></td><td><code>machines_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.machines_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="machineName, projectName, resourceGroupName, subscriptionId" /> | Get a Machine |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List Machine resources by AssessmentProject |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List Machine resources by AssessmentProject |
