---
title: billing_group_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_group_tags
  - billingconductor
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

Expands all tag keys and values for <code>billing_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_group_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A billing group is a set of linked account which belong to the same end customer. It can be seen as a virtual consolidated billing family.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.billing_group_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="primary_account_id" /></td><td><code>string</code></td><td>This account will act as a virtual payer account of the billing group</td></tr>
<tr><td><CopyableCode code="computation_preference" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="account_grouping" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="size" /></td><td><code>integer</code></td><td>Number of accounts in the billing group</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
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
Expands tags for all <code>billing_groups</code> in a region.
```sql
SELECT
region,
arn,
name,
description,
primary_account_id,
computation_preference,
account_grouping,
size,
status,
status_reason,
creation_time,
last_modified_time,
tag_key,
tag_value
FROM aws.billingconductor.billing_group_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>billing_group_tags</code> resource, see <a href="/providers/aws/billingconductor/billing_groups/#permissions"><code>billing_groups</code></a>


