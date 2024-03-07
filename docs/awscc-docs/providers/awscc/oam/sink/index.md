---
title: sink
hide_title: false
hide_table_of_contents: false
keywords:
  - sink
  - oam
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>sink</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sink</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sink</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.oam.sink</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the ObservabilityAccessManager Sink</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the ObservabilityAccessManager Sink.</td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>The policy of this ObservabilityAccessManager Sink.</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>Tags to apply to the sink</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>sink</code> resource, the following permissions are required:

### Delete
```json
oam:DeleteSink,
oam:GetSinkPolicy,
oam:GetSink
```

### Read
```json
oam:GetSinkPolicy,
oam:GetSink
```

### Update
```json
oam:PutSinkPolicy,
oam:GetSinkPolicy,
oam:GetSink,
oam:TagResource,
oam:UntagResource
```


## Example
```sql
SELECT
region,
arn,
name,
policy,
tags
FROM awscc.oam.sink
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
