---
title: network_insights_analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_analysis
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
Gets an individual <code>network_insights_analysis</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_insights_analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>network_insights_analysis</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.network_insights_analysis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>return_path_components</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>network_insights_analysis_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_insights_path_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_path_found</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>suggested_accounts</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>filter_in_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>network_insights_analysis_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>start_date</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>alternate_path_hints</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>explanations</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>forward_path_components</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>additional_accounts</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
status,
return_path_components,
network_insights_analysis_id,
network_insights_path_id,
network_path_found,
suggested_accounts,
filter_in_arns,
network_insights_analysis_arn,
status_message,
start_date,
alternate_path_hints,
explanations,
forward_path_components,
additional_accounts,
tags
FROM awscc.ec2.network_insights_analysis
WHERE data__Identifier = '<NetworkInsightsAnalysisId>';
```

## Permissions

To operate on the <code>network_insights_analysis</code> resource, the following permissions are required:

### Read
```json
ec2:Describe*
```

### Update
```json
ec2:CreateTags,
ec2:Describe*,
ec2:DeleteTags
```

### Delete
```json
ec2:DeleteNetworkInsightsAnalysis,
ec2:DeleteTags
```

