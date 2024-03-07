---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
  - quicksight
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>analyses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analyses</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.quicksight.analyses</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>analysis_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>analyses</code> resource, the following permissions are required:

### Create
<pre>
quicksight:DescribeAnalysis,
quicksight:DescribeAnalysisPermissions,
quicksight:CreateAnalysis,
quicksight:DescribeTemplate,
quicksight:DescribeTheme,
quicksight:PassDataSet,
quicksight:TagResource,
quicksight:UntagResource,
quicksight:ListTagsForResource</pre>

### List
<pre>
quicksight:ListAnalyses</pre>


## Example
```sql
SELECT
region,
analysis_id,
aws_account_id
FROM awscc.quicksight.analyses
WHERE region = 'us-east-1'
```
