---
title: inference_schedulers
hide_title: false
hide_table_of_contents: false
keywords:
  - inference_schedulers
  - lookoutequipment
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>inference_schedulers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inference_schedulers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>inference_schedulers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lookoutequipment.inference_schedulers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>inference_scheduler_name</code></td><td><code>string</code></td><td>The name of the inference scheduler being created.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
inference_scheduler_name
FROM awscc.lookoutequipment.inference_schedulers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>inference_schedulers</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
lookoutequipment:CreateInferenceScheduler,
lookoutequipment:DescribeInferenceScheduler
```

### List
```json
lookoutequipment:ListInferenceSchedulers
```

