---
title: sequence_store
hide_title: false
hide_table_of_contents: false
keywords:
  - sequence_store
  - omics
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>sequence_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sequence_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::SequenceStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.omics.sequence_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The store's ARN.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>When the store was created.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description for the store.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name for the store.</td></tr>
<tr><td><code>fallback_location</code></td><td><code>string</code></td><td>An S3 URI representing the bucket and folder to store failed read set uploads.</td></tr>
<tr><td><code>sequence_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sse_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
creation_time,
description,
name,
fallback_location,
sequence_store_id,
sse_config,
tags
FROM aws.omics.sequence_store
WHERE data__Identifier = '<SequenceStoreId>';
```

## Permissions

To operate on the <code>sequence_store</code> resource, the following permissions are required:

### Read
```json
omics:GetSequenceStore,
omics:ListTagsForResource
```

### Delete
```json
omics:DeleteSequenceStore
```

