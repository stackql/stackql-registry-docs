---
title: network_insights_access_scope_analysis_findings
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analysis_findings
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
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analysis_findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_access_scope_analysis_findings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="findingComponentSet" /> | `array` | The finding components. |
| <CopyableCode code="findingId" /> | `string` | The ID of the finding. |
| <CopyableCode code="networkInsightsAccessScopeAnalysisId" /> | `string` | The ID of the Network Access Scope analysis. |
| <CopyableCode code="networkInsightsAccessScopeId" /> | `string` | The ID of the Network Access Scope. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="network_insights_access_scope_analysis_findings_Get" /> | `SELECT` | <CopyableCode code="NetworkInsightsAccessScopeAnalysisId, region" /> |
