---
title: analysis
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis
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
Gets an individual <code>analysis</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analysis</td></tr>
<tr><td><b>Id</b></td><td><code>aws.quicksight.analysis</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>analysis_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_set_arns</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>errors</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>last_updated_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>permissions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>sheets</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>source_entity</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>theme_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
analysis_id,
arn,
aws_account_id,
created_time,
data_set_arns,
definition,
errors,
last_updated_time,
name,
parameters,
permissions,
sheets,
source_entity,
status,
tags,
theme_arn
FROM aws.quicksight.analysis
WHERE region = 'us-east-1'
AND data__Identifier = '<AnalysisId>'
AND data__Identifier = '<AwsAccountId>'
```
