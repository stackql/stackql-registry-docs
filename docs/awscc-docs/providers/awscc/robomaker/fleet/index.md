---
title: fleet
hide_title: false
hide_table_of_contents: false
keywords:
  - fleet
  - robomaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fleet</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleet</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleet</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.robomaker.fleet</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the fleet.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
tags,
name
FROM awscc.robomaker.fleet
WHERE region = 'us-east-1'
AND data__Identifier = '{Arn}';
```

## Permissions

To operate on the <code>fleet</code> resource, the following permissions are required:

### Read
```json
robomaker:DescribeFleet
```

### Delete
```json
robomaker:DeleteFleet
```

### Update
```json
robomaker:TagResource,
robomaker:UntagResource
```

