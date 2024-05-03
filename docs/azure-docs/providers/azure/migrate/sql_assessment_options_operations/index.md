---
title: sql_assessment_options_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_assessment_options_operations
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
<tr><td><b>Name</b></td><td><code>sql_assessment_options_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.sql_assessment_options_operations" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assessmentOptionsName, projectName, resourceGroupName, subscriptionId" /> | Get a SqlAssessmentOptions |
| <CopyableCode code="list_by_assessment_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List SqlAssessmentOptions resources by AssessmentProject |
| <CopyableCode code="_list_by_assessment_project" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | List SqlAssessmentOptions resources by AssessmentProject |
