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
Gets or operates on an individual <code>bot_alias</code> resource, use <code>bot_aliases</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Bot Alias enables you to change the version of a bot without updating applications that use the bot</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lex.bot_alias</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.lex.bot_alias
WHERE data__Identifier = '<BotAliasId>|<BotId>';
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

