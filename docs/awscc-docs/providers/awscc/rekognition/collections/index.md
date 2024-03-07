---
title: collections
hide_title: false
hide_table_of_contents: false
keywords:
  - collections
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
Retrieves a list of <code>collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>collections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rekognition.collections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>collection_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
collection_id
FROM awscc.rekognition.collections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>collections</code> resource, the following permissions are required:

### Create
```json
rekognition:CreateCollection,
rekognition:DescribeCollection,
rekognition:ListTagsForResource,
rekognition:TagResource
```

### List
```json
rekognition:ListCollections
```

