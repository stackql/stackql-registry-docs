---
title: annotation_store
hide_title: false
hide_table_of_contents: false
keywords:
  - annotation_store
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
Gets an individual <code>annotation_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>annotation_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>annotation_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.omics.annotation_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>reference</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sse_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status_message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>store_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>store_format</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>store_options</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>store_size_bytes</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>update_time</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
creation_time,
description,
id,
name,
reference,
sse_config,
status,
status_message,
store_arn,
store_format,
store_options,
store_size_bytes,
tags,
update_time
FROM awscc.omics.annotation_store
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>annotation_store</code> resource, the following permissions are required:

### Read
```json
omics:GetAnnotationStore
```

### Update
```json
omics:UpdateAnnotationStore,
omics:TagResource,
omics:UntagResource,
omics:GetAnnotationStore,
omics:ListTagsForResource
```

### Delete
```json
omics:DeleteAnnotationStore,
omics:ListAnnotationStores
```

