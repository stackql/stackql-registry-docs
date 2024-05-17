---
title: network_insights_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_analyses
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
<tr><td><b>Name</b></td><td><code>network_insights_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_analyses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="alternatePathHintSet" /> | `array` | Potential intermediate components. |
| <CopyableCode code="explanationSet" /> | `array` | The explanations. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html"&gt;Reachability Analyzer explanation codes&lt;/a&gt;. |
| <CopyableCode code="filterInArnSet" /> | `array` | The Amazon Resource Names (ARN) of the Amazon Web Services resources that the path must traverse. |
| <CopyableCode code="forwardPathComponentSet" /> | `array` | The components in the path from source to destination. |
| <CopyableCode code="networkInsightsAnalysisArn" /> | `string` | The Amazon Resource Name (ARN) of the network insights analysis. |
| <CopyableCode code="networkInsightsAnalysisId" /> | `string` | The ID of the network insights analysis. |
| <CopyableCode code="networkInsightsPathId" /> | `string` | The ID of the path. |
| <CopyableCode code="networkPathFound" /> | `boolean` | Indicates whether the destination is reachable from the source. |
| <CopyableCode code="returnPathComponentSet" /> | `array` | The components in the path from destination to source. |
| <CopyableCode code="startDate" /> | `string` | The time the analysis started. |
| <CopyableCode code="status" /> | `string` | The status of the network insights analysis. |
| <CopyableCode code="statusMessage" /> | `string` | The status message, if the status is &lt;code&gt;failed&lt;/code&gt;. |
| <CopyableCode code="tagSet" /> | `array` | The tags. |
| <CopyableCode code="warningMessage" /> | `string` | The warning message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="network_insights_analyses_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
