---
title: network_insights_access_scope_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analyses
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_access_scope_analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="analyzedEniCount" /> | `integer` | The number of network interfaces analyzed. |
| <CopyableCode code="endDate" /> | `string` | The analysis end date. |
| <CopyableCode code="findingsFound" /> | `string` | Indicates whether there are findings. |
| <CopyableCode code="networkInsightsAccessScopeAnalysisArn" /> | `string` | The Amazon Resource Name (ARN) of the Network Access Scope analysis. |
| <CopyableCode code="networkInsightsAccessScopeAnalysisId" /> | `string` | The ID of the Network Access Scope analysis. |
| <CopyableCode code="networkInsightsAccessScopeId" /> | `string` | The ID of the Network Access Scope. |
| <CopyableCode code="startDate" /> | `string` | The analysis start date. |
| <CopyableCode code="status" /> | `string` | The status. |
| <CopyableCode code="statusMessage" /> | `string` | The status message. |
| <CopyableCode code="tagSet" /> | `array` | The tags. |
| <CopyableCode code="warningMessage" /> | `string` | The warning message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="network_insights_access_scope_analyses_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
