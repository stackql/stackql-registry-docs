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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.network_insights_analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `alternatePathHintSet` | `array` | Potential intermediate components. |
| `explanationSet` | `array` | The explanations. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html"&gt;Reachability Analyzer explanation codes&lt;/a&gt;. |
| `filterInArnSet` | `array` | The Amazon Resource Names (ARN) of the Amazon Web Services resources that the path must traverse. |
| `forwardPathComponentSet` | `array` | The components in the path from source to destination. |
| `networkInsightsAnalysisArn` | `string` | The Amazon Resource Name (ARN) of the network insights analysis. |
| `networkInsightsAnalysisId` | `string` | The ID of the network insights analysis. |
| `networkInsightsPathId` | `string` | The ID of the path. |
| `networkPathFound` | `boolean` | Indicates whether the destination is reachable from the source. |
| `returnPathComponentSet` | `array` | The components in the path from destination to source. |
| `startDate` | `string` | The time the analysis started. |
| `status` | `string` | The status of the network insights analysis. |
| `statusMessage` | `string` | The status message, if the status is &lt;code&gt;failed&lt;/code&gt;. |
| `tagSet` | `array` | The tags. |
| `warningMessage` | `string` | The warning message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `network_insights_analyses_Describe` | `SELECT` | `region` |
