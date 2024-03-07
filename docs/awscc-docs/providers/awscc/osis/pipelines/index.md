---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - osis
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>pipelines</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.osis.pipelines</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>pipeline_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
<pre>
osis:CreatePipeline,
osis:GetPipeline,
osis:TagResource,
osis:ListTagsForResource,
iam:PassRole,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
kms:DescribeKey</pre>

### List
<pre>
osis:ListPipelines</pre>


## Example
```sql
SELECT
region,
pipeline_arn
FROM awscc.osis.pipelines
WHERE region = 'us-east-1'
```
