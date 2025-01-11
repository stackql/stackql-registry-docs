---
title: collaboration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - collaboration_tags
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

Expands all tag keys and values for <code>collaborations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collaboration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a collaboration between AWS accounts that allows for secure data collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.collaboration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_member_abilities" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_ml_member_abilities" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_encryption_metadata" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="members" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_log_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="analytics_engine" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creator_payment_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>collaborations</code> in a region.
```sql
SELECT
region,
arn,
collaboration_identifier,
creator_display_name,
creator_member_abilities,
creator_ml_member_abilities,
data_encryption_metadata,
description,
members,
name,
query_log_status,
analytics_engine,
creator_payment_configuration,
tag_key,
tag_value
FROM aws.cleanrooms.collaboration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>collaboration_tags</code> resource, see <a href="/providers/aws/cleanrooms/collaborations/#permissions"><code>collaborations</code></a>

