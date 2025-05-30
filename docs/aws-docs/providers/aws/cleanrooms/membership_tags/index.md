---
title: membership_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - membership_tags
  - cleanrooms
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

Expands all tag keys and values for <code>memberships</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>membership_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an AWS account that is a part of a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.membership_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_creator_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_log_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_result_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="payment_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>memberships</code> in a region.
```sql
SELECT
region,
arn,
collaboration_arn,
collaboration_creator_account_id,
collaboration_identifier,
membership_identifier,
query_log_status,
default_result_configuration,
payment_configuration,
tag_key,
tag_value
FROM aws.cleanrooms.membership_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>membership_tags</code> resource, see <a href="/providers/aws/cleanrooms/memberships/#permissions"><code>memberships</code></a>

