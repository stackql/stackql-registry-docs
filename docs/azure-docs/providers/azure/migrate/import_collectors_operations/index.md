---
title: import_collectors_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - import_collectors_operations
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
<tr><td><b>Name</b></td><td><code>import_collectors_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.import_collectors_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="importCollectorName, projectName, resourceGroupName, subscriptionId" /> | Get a ImportCollector |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List ImportCollector resources by AssessmentProject |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="importCollectorName, projectName, resourceGroupName, subscriptionId" /> | Create a ImportCollector |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="importCollectorName, projectName, resourceGroupName, subscriptionId" /> | Delete a ImportCollector |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List ImportCollector resources by AssessmentProject |
