---
title: notification_rule_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rule_tags
  - codestarnotifications
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

Expands all tag keys and values for <code>notification_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_rule_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CodeStarNotifications::NotificationRule</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codestarnotifications.notification_rule_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_type_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_address" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_type_ids" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="detail_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>notification_rules</code> in a region.
```sql
SELECT
region,
event_type_id,
created_by,
target_address,
event_type_ids,
status,
detail_type,
resource,
targets,
name,
arn,
tag_key,
tag_value
FROM aws.codestarnotifications.notification_rule_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>notification_rule_tags</code> resource, see <a href="/providers/aws/codestarnotifications/notification_rules/#permissions"><code>notification_rules</code></a>

