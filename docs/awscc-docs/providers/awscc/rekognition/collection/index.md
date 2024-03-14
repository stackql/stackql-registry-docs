---
title: collection
hide_title: false
hide_table_of_contents: false
keywords:
  - collection
  - rekognition
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>collection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rekognition.collection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>collection_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
arn,
collection_id,
tags
FROM awscc.rekognition.collection
WHERE data__Identifier = '<CollectionId>';
```

## Permissions

To operate on the <code>collection</code> resource, the following permissions are required:

### Read
```json
rekognition:DescribeCollection,
rekognition:ListTagsForResource
```

### Update
```json
rekognition:TagResource,
rekognition:UntagResource,
rekognition:DescribeCollection,
rekognition:ListTagsForResource
```

### Delete
```json
rekognition:DeleteCollection
```

