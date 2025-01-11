---
title: variant_store_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - variant_store_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>variant_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variant_store_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Omics::VariantStore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.omics.variant_store_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="reference" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_message" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="store_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="store_size_bytes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>variant_stores</code> in a region.
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
store_size_bytes,
update_time,
tag_key,
tag_value
FROM aws.omics.variant_store_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>variant_store_tags</code> resource, see <a href="/providers/aws/omics/variant_stores/#permissions"><code>variant_stores</code></a>

