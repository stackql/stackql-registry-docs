---
title: network_insights_access_scope_analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scope_analysis
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
Gets an individual <code>network_insights_access_scope_analysis</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_access_scope_analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_insights_access_scope_analysis</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_insights_access_scope_analysis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>network_insights_access_scope_analysis_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_insights_access_scope_analysis_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_insights_access_scope_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>start_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>end_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>findings_found</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>analyzed_eni_count</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
network_insights_access_scope_analysis_id,
network_insights_access_scope_analysis_arn,
network_insights_access_scope_id,
status,
status_message,
start_date,
end_date,
findings_found,
analyzed_eni_count,
tags
FROM awscc.ec2.network_insights_access_scope_analysis
WHERE data__Identifier = '<NetworkInsightsAccessScopeAnalysisId>';
```

## Permissions

To operate on the <code>network_insights_access_scope_analysis</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeNetworkInsightsAccessScopeAnalyses
```

### Update
```json
ec2:DescribeNetworkInsightsAccessScopeAnalyses,
ec2:CreateTags,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteNetworkInsightsAccessScopeAnalysis,
ec2:DeleteTags
```

