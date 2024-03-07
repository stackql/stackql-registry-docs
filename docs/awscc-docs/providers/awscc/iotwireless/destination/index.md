---
title: destination
hide_title: false
hide_table_of_contents: false
keywords:
  - destination
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>destination</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>destination</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.destination</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Unique name of destination</td></tr>
<tr><td><code>expression</code></td><td><code>string</code></td><td>Destination expression</td></tr>
<tr><td><code>expression_type</code></td><td><code>string</code></td><td>Must be RuleName</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Destination description</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>AWS role ARN that grants access</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Destination arn. Returned after successful create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>destination</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetDestination,
iotwireless:ListTagsForResource
```

### Update
```json
iam:PassRole,
iotwireless:UpdateDestination,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

### Delete
```json
iotwireless:DeleteDestination
```


## Example
```sql
SELECT
region,
name,
expression,
expression_type,
description,
tags,
role_arn,
arn
FROM awscc.iotwireless.destination
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
