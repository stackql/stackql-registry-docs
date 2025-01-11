---
title: mail_manager_traffic_policy_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - mail_manager_traffic_policy_tags
  - ses
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

Expands all tag keys and values for <code>mail_manager_traffic_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mail_manager_traffic_policy_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::SES::MailManagerTrafficPolicy Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.mail_manager_traffic_policy_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="default_action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_message_size_bytes" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_statements" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="traffic_policy_name" /></td><td><code>string</code></td><td></td></tr>
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
Expands tags for all <code>mail_manager_traffic_policies</code> in a region.
```sql
SELECT
region,
default_action,
max_message_size_bytes,
policy_statements,
traffic_policy_arn,
traffic_policy_id,
traffic_policy_name,
tag_key,
tag_value
FROM aws.ses.mail_manager_traffic_policy_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>mail_manager_traffic_policy_tags</code> resource, see <a href="/providers/aws/ses/mail_manager_traffic_policies/#permissions"><code>mail_manager_traffic_policies</code></a>

