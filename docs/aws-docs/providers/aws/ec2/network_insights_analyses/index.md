---
title: network_insights_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_analyses
  - ec2
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
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networkInsightsPathId` | `string` | The ID of the path. |
| `statusMessage` | `string` | The status message, if the status is &lt;code&gt;failed&lt;/code&gt;. |
| `returnPathComponentSet` | `array` | The components in the path from destination to source. |
| `networkPathFound` | `boolean` | Indicates whether the destination is reachable from the source. |
| `forwardPathComponentSet` | `array` | The components in the path from source to destination. |
| `startDate` | `string` | The time the analysis started. |
| `tagSet` | `array` | The tags. |
| `explanationSet` | `array` | The explanations. For more information, see &lt;a href="https://docs.aws.amazon.com/vpc/latest/reachability/explanation-codes.html"&gt;Reachability Analyzer explanation codes&lt;/a&gt;. |
| `networkInsightsAnalysisId` | `string` | The ID of the network insights analysis. |
| `filterInArnSet` | `array` | The Amazon Resource Names (ARN) of the Amazon Web Services resources that the path must traverse. |
| `alternatePathHintSet` | `array` | Potential intermediate components. |
| `status` | `string` | The status of the network insights analysis. |
| `networkInsightsAnalysisArn` | `string` | The Amazon Resource Name (ARN) of the network insights analysis. |
| `warningMessage` | `string` | The warning message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `network_insights_analyses_Describe` | `SELECT` | `region` |
