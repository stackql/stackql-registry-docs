---
title: server_collectors_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - server_collectors_operations
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
<tr><td><b>Name</b></td><td><code>server_collectors_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.server_collectors_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, serverCollectorName, subscriptionId" /> | Get a ServerCollector |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List ServerCollector resources by AssessmentProject |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectName, resourceGroupName, serverCollectorName, subscriptionId" /> | Create a ServerCollector |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectName, resourceGroupName, serverCollectorName, subscriptionId" /> | Delete a ServerCollector |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List ServerCollector resources by AssessmentProject |
