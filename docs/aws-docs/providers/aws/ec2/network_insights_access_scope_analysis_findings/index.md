---
title: network_insights_access_scope_analysis_findings
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analysis_findings
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analysis_findings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.network_insights_access_scope_analysis_findings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `findingComponentSet` | `array` | The finding components. |
| `findingId` | `string` | The ID of the finding. |
| `networkInsightsAccessScopeAnalysisId` | `string` | The ID of the Network Access Scope analysis. |
| `networkInsightsAccessScopeId` | `string` | The ID of the Network Access Scope. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `network_insights_access_scope_analysis_findings_Get` | `SELECT` | `NetworkInsightsAccessScopeAnalysisId` |
