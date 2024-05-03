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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>sequence_store</code> resource, use <code>sequence_stores</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sequence_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::SequenceStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.sequence_store" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The store's ARN.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>When the store was created.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the store.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the store.</td></tr>
<tr><td><CopyableCode code="fallback_location" /></td><td><code>string</code></td><td>An S3 URI representing the bucket and folder to store failed read set uploads.</td></tr>
<tr><td><CopyableCode code="sequence_store_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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

