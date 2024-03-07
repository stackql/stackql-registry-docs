---
title: bot_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_alias
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
Gets an individual <code>bot_alias</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bot_alias</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lex.bot_alias</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bot_alias_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_alias_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_alias_locale_settings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>bot_alias_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>conversation_log_settings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sentiment_analysis_settings</code></td><td><code>object</code></td><td>Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.</td></tr>
<tr><td><code>bot_alias_tags</code></td><td><code>array</code></td><td>A list of tags to add to the bot alias.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
bot_alias_id,
bot_id,
arn,
bot_alias_status,
bot_alias_locale_settings,
bot_alias_name,
bot_version,
conversation_log_settings,
description,
sentiment_analysis_settings,
bot_alias_tags
FROM awscc.lex.bot_alias
WHERE region = 'us-east-1'
AND data__Identifier = '{BotAliasId}';
AND data__Identifier = '{BotId}';
```

## Permissions

To operate on the <code>bot_alias</code> resource, the following permissions are required:

### Update
```json
lex:UpdateBotAlias,
lex:DescribeBotAlias,
lex:ListTagsForResource,
lex:TagResource,
lex:UntagResource
```

### Read
```json
lex:DescribeBotAlias
```

### Delete
```json
lex:DeleteBotAlias
```

