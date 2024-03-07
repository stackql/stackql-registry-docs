---
title: flow_outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_outputs
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>flow_outputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow_outputs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.flow_outputs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>output_arn</code></td><td><code>string</code></td><td>The ARN of the output.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>flow_outputs</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
mediaconnect:AddFlowOutputs
```

### List
```json
mediaconnect:DescribeFlow
```


## Example
```sql
SELECT
region,
output_arn
FROM awscc.mediaconnect.flow_outputs
WHERE region = 'us-east-1'
```
