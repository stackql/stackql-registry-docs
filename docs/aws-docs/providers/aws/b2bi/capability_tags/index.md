---
title: capability_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - capability_tags
  - b2bi
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

Expands all tag keys and values for <code>capabilities</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>capability_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::B2BI::Capability Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.b2bi.capability_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="capability_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capability_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="instructions_documents" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="modified_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>capabilities</code> in a region.
```sql
SELECT
region,
capability_arn,
capability_id,
configuration,
created_at,
instructions_documents,
modified_at,
name,
type,
tag_key,
tag_value
FROM aws.b2bi.capability_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>capability_tags</code> resource, see <a href="/providers/aws/b2bi/capabilities/#permissions"><code>capabilities</code></a>


