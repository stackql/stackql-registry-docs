---
title: network_insights_access_scope_analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analyses
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
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_access_scope_analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networkInsightsAccessScopeId` | `string` | The ID of the Network Access Scope. |
| `startDate` | `string` | The analysis start date. |
| `status` | `string` | The status. |
| `analyzedEniCount` | `integer` | The number of network interfaces analyzed. |
| `statusMessage` | `string` | The status message. |
| `networkInsightsAccessScopeAnalysisArn` | `string` | The Amazon Resource Name (ARN) of the Network Access Scope analysis. |
| `endDate` | `string` | The analysis end date. |
| `tagSet` | `array` | The tags. |
| `networkInsightsAccessScopeAnalysisId` | `string` | The ID of the Network Access Scope analysis. |
| `findingsFound` | `string` | Indicates whether there are findings. |
| `warningMessage` | `string` | The warning message. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `network_insights_access_scope_analyses_Describe` | `SELECT` |  |
