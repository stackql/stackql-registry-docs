---
title: data_source
hide_title: false
hide_table_of_contents: false
keywords:
  - data_source
  - kendra
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>data_source</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_source</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_source</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.kendra.data_source</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>index_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_source_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>schedule</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Tags for labeling the data source</td></tr>
<tr><td><code>custom_document_enrichment_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>language_code</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
name,
index_id,
type,
data_source_configuration,
description,
schedule,
role_arn,
tags,
custom_document_enrichment_configuration,
language_code
FROM awscc.kendra.data_source
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
AND data__Identifier = '{IndexId}';
```

## Permissions

To operate on the <code>data_source</code> resource, the following permissions are required:

### Read
```json
kendra:DescribeDataSource,
kendra:ListTagsForResource
```

### Delete
```json
kendra:DescribeDataSource,
kendra:DeleteDataSource
```

### Update
```json
kendra:DescribeDataSource,
kendra:UpdateDataSource,
kendra:ListTagsForResource,
kendra:TagResource,
kendra:UntagResource,
iam:PassRole
```

