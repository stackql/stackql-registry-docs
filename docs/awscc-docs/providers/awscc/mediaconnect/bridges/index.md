---
title: bridges
hide_title: false
hide_table_of_contents: false
keywords:
  - bridges
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
Retrieves a list of <code>bridges</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bridges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bridges</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.bridges</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bridge_arn</code></td><td><code>string</code></td><td>The Amazon Resource Number (ARN) of the bridge.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>bridges</code> resource, the following permissions are required:

### Create
```json
mediaconnect:CreateBridge,
mediaconnect:DescribeBridge
```

### List
```json
mediaconnect:ListBridges
```


## Example
```sql
SELECT
region,
bridge_arn
FROM awscc.mediaconnect.bridges
WHERE region = 'us-east-1'
```
