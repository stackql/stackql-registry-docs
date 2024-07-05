---
title: bots_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - bots_list_only
  - lex
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

Lists <code>bots</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/bots/"><code>bots</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bots_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Unique ID of resource</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique identifier for a resource.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the version. Use the description to help identify the version in lists.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that has permission to access the bot.</td></tr>
<tr><td><CopyableCode code="data_privacy" /></td><td><code>object</code></td><td>Data privacy setting of the Bot.</td></tr>
<tr><td><CopyableCode code="idle_session_ttl_in_seconds" /></td><td><code>integer</code></td><td>IdleSessionTTLInSeconds of the resource</td></tr>
<tr><td><CopyableCode code="bot_locales" /></td><td><code>array</code></td><td>List of bot locales</td></tr>
<tr><td><CopyableCode code="bot_file_s3_location" /></td><td><code>object</code></td><td>S3 location of bot definitions zip file, if it's not defined inline in CloudFormation.</td></tr>
<tr><td><CopyableCode code="bot_tags" /></td><td><code>array</code></td><td>A list of tags to add to the bot, which can only be added at bot creation.</td></tr>
<tr><td><CopyableCode code="test_bot_alias_tags" /></td><td><code>array</code></td><td>A list of tags to add to the test alias for a bot, , which can only be added at bot/bot alias creation.</td></tr>
<tr><td><CopyableCode code="auto_build_bot_locales" /></td><td><code>boolean</code></td><td>Specifies whether to build the bot locales after bot creation completes.</td></tr>
<tr><td><CopyableCode code="test_bot_alias_settings" /></td><td><code>object</code></td><td>Configuring the test bot alias settings for a given bot</td></tr>
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
Lists all <code>bots</code> in a region.
```sql
SELECT
region,
id
FROM aws.lex.bots_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>bots_list_only</code> resource, see <a href="/providers/aws/lex/bots/#permissions"><code>bots</code></a>


