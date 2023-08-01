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
| `warningMessage` | `string` | The warning message. |
| `networkInsightsAccessScopeId` | `string` | The ID of the Network Access Scope. |
| `networkInsightsAccessScopeAnalysisArn` | `string` | The Amazon Resource Name (ARN) of the Network Access Scope analysis. |
| `startDate` | `string` | The analysis start date. |
| `networkInsightsAccessScopeAnalysisId` | `string` | The ID of the Network Access Scope analysis. |
| `status` | `string` | The status. |
| `statusMessage` | `string` | The status message. |
| `findingsFound` | `string` | Indicates whether there are findings. |
| `endDate` | `string` | The analysis end date. |
| `analyzedEniCount` | `integer` | The number of network interfaces analyzed. |
| `tagSet` | `array` | The tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `network_insights_access_scope_analyses_Describe` | `SELECT` | `region` |
