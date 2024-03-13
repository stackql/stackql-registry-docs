---
title: bot
hide_title: false
hide_table_of_contents: false
keywords:
  - bot
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
Gets an individual <code>bot</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bot</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lex.bot</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>data_privacy</code></td><td><code>object</code></td><td>Data privacy setting of the Bot.</td></tr>
<tr><td><code>idle_session_ttl_in_seconds</code></td><td><code>integer</code></td><td>IdleSessionTTLInSeconds of the resource</td></tr>
<tr><td><code>bot_locales</code></td><td><code>array</code></td><td>List of bot locales</td></tr>
<tr><td><code>bot_file_s3_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>bot_tags</code></td><td><code>array</code></td><td>A list of tags to add to the bot, which can only be added at bot creation.</td></tr>
<tr><td><code>test_bot_alias_tags</code></td><td><code>array</code></td><td>A list of tags to add to the test alias for a bot, , which can only be added at bot&#x2F;bot alias creation.</td></tr>
<tr><td><code>auto_build_bot_locales</code></td><td><code>boolean</code></td><td>Specifies whether to build the bot locales after bot creation completes.</td></tr>
<tr><td><code>test_bot_alias_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
name,
description,
role_arn,
data_privacy,
idle_session_ttl_in_seconds,
bot_locales,
bot_file_s3_location,
bot_tags,
test_bot_alias_tags,
auto_build_bot_locales,
test_bot_alias_settings
FROM awscc.lex.bot
WHERE region = 'us-east-1'
AND data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>bot</code> resource, the following permissions are required:

### Read
```json
lex:DescribeBot,
lex:ListTagsForResource
```

### Update
```json
iam:PassRole,
lex:DescribeBot,
lex:CreateUploadUrl,
lex:StartImport,
lex:DescribeImport,
lex:ListTagsForResource,
lex:TagResource,
lex:UntagResource,
lex:CreateBot,
lex:CreateBotLocale,
lex:CreateIntent,
lex:CreateSlot,
lex:CreateSlotType,
lex:UpdateBot,
lex:UpdateBotLocale,
lex:UpdateIntent,
lex:UpdateSlot,
lex:UpdateSlotType,
lex:DeleteBotLocale,
lex:DeleteIntent,
lex:DeleteSlot,
lex:DeleteSlotType,
lex:DescribeBotLocale,
lex:BuildBotLocale,
lex:ListBots,
lex:ListBotLocales,
lex:CreateCustomVocabulary,
lex:UpdateCustomVocabulary,
lex:DeleteCustomVocabulary,
s3:GetObject,
lex:UpdateBotAlias
```

### Delete
```json
lex:DeleteBot,
lex:DescribeBot,
lex:DeleteBotLocale,
lex:DeleteIntent,
lex:DeleteSlotType,
lex:DeleteSlot,
lex:DeleteBotVersion,
lex:DeleteBotChannel,
lex:DeleteBotAlias,
lex:DeleteCustomVocabulary
```

