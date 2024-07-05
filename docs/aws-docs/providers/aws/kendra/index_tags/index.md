---
title: index_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - index_tags
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>indices</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Kendra index</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kendra.index_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of index</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the index</td></tr>
<tr><td><CopyableCode code="server_side_encryption_configuration" /></td><td><code>object</code></td><td>Server side encryption configuration</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of index</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="edition" /></td><td><code>string</code></td><td>Edition of index</td></tr>
<tr><td><CopyableCode code="document_metadata_configurations" /></td><td><code>array</code></td><td>Document metadata configurations</td></tr>
<tr><td><CopyableCode code="capacity_units" /></td><td><code>object</code></td><td>Capacity units</td></tr>
<tr><td><CopyableCode code="user_context_policy" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_token_configurations" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>indices</code> in a region.
```sql
SELECT
region,
id,
arn,
description,
server_side_encryption_configuration,
name,
role_arn,
edition,
document_metadata_configurations,
capacity_units,
user_context_policy,
user_token_configurations,
tag_key,
tag_value
FROM aws.kendra.index_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>index_tags</code> resource, see <a href="/providers/aws/kendra/indices/#permissions"><code>indices</code></a>


