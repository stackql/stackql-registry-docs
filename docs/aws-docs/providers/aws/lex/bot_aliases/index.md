---
title: bot_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_aliases
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
Retrieves a list of <code>bot_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bot_aliases</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lex.bot_aliases</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>BotAliasId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BotId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BotAliasStatus</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BotAliasLocaleSettings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>BotAliasName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>BotVersion</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>ConversationLogSettings</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SentimentAnalysisSettings</code></td><td><code>object</code></td><td>Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.</td></tr>
<tr><td><code>BotAliasTags</code></td><td><code>array</code></td><td>A list of tags to add to the bot alias.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.lex.bot_aliases<br/>WHERE region = 'us-east-1'
</pre>
