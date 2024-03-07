---
title: functions
hide_title: false
hide_table_of_contents: false
keywords:
  - functions
  - cloudfront
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>functions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>functions</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.functions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>function_ar_n</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
function_ar_n
FROM awscc.cloudfront.functions

```

## Permissions

To operate on the <code>functions</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateFunction,
cloudfront:PublishFunction,
cloudfront:DescribeFunction
```

### List
```json
cloudfront:ListFunctions
```

