---
title: assessed_sql_instance_v2_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assessed_sql_instance_v2_operations
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
<tr><td><b>Name</b></td><td><code>assessed_sql_instance_v2_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.assessed_sql_instance_v2_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessedSqlInstanceName, assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | Get a AssessedSqlInstanceV2 |
| <CopyableCode code="list_by_sql_assessment_v2" /> | `SELECT` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | List AssessedSqlInstanceV2 resources by SqlAssessmentV2 |
| <CopyableCode code="_list_by_sql_assessment_v2" /> | `EXEC` | <CopyableCode code="assessmentName, groupName, projectName, resourceGroupName, subscriptionId" /> | List AssessedSqlInstanceV2 resources by SqlAssessmentV2 |
