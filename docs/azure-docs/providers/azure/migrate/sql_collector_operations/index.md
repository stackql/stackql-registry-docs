---
title: sql_collector_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_collector_operations
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
<tr><td><b>Name</b></td><td><code>sql_collector_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_collector_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="collectorName, projectName, resourceGroupName, subscriptionId" /> | Get a SqlCollector |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List SqlCollector resources by AssessmentProject |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="collectorName, projectName, resourceGroupName, subscriptionId" /> | Create a SqlCollector |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="collectorName, projectName, resourceGroupName, subscriptionId" /> | Delete a SqlCollector |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List SqlCollector resources by AssessmentProject |
