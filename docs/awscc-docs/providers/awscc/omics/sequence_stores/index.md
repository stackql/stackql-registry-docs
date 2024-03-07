---
title: sequence_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - sequence_stores
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
Retrieves a list of <code>sequence_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sequence_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>sequence_stores</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.omics.sequence_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>sequence_store_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>sequence_stores</code> resource, the following permissions are required:

### Create
```json
omics:CreateSequenceStore,
omics:TagResource
```

### List
```json
omics:ListSequenceStores
```


## Example
```sql
SELECT
region,
sequence_store_id
FROM awscc.omics.sequence_stores
WHERE region = 'us-east-1'
```
