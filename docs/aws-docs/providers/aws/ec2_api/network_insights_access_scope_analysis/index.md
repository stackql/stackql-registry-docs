---
title: network_insights_access_scope_analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analysis
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
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_access_scope_analysis" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_insights_access_scope_analysis_Delete" /> | `DELETE` | <CopyableCode code="NetworkInsightsAccessScopeAnalysisId, region" /> | Deletes the specified Network Access Scope analysis. |
| <CopyableCode code="network_insights_access_scope_analysis_Start" /> | `EXEC` | <CopyableCode code="ClientToken, NetworkInsightsAccessScopeId, region" /> | Starts analyzing the specified Network Access Scope. |
