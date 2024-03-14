---
title: key_value_store
hide_title: false
hide_table_of_contents: false
keywords:
  - key_value_store
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
Gets an individual <code>key_value_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_value_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>key_value_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudfront.key_value_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>comment</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>import_source</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
id,
status,
name,
comment,
import_source
FROM awscc.cloudfront.key_value_store
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>key_value_store</code> resource, the following permissions are required:

### Delete
```json
cloudfront:DeleteKeyValueStore,
cloudfront:DescribeKeyValueStore
```

### Read
```json
cloudfront:DescribeKeyValueStore
```

### Update
```json
cloudfront:UpdateKeyValueStore,
cloudfront:DescribeKeyValueStore
```

