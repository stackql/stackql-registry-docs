---
title: custom_action_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_action_tags
  - chatbot
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

Expands all tag keys and values for <code>custom_actions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_action_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Chatbot::CustomAction Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.chatbot.custom_action_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="action_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="alias_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attachments" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_action_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>custom_actions</code> in a region.
```sql
SELECT
region,
action_name,
alias_name,
attachments,
custom_action_arn,
definition,
tag_key,
tag_value
FROM aws.chatbot.custom_action_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>custom_action_tags</code> resource, see <a href="/providers/aws/chatbot/custom_actions/#permissions"><code>custom_actions</code></a>

