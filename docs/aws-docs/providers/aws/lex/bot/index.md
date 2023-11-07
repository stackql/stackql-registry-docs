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
<tr><td><b>Id</b></td><td><code>aws.lex.bot</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>DataPrivacy</code></td><td><code>object</code></td><td>Data privacy setting of the Bot.</td></tr>
<tr><td><code>IdleSessionTTLInSeconds</code></td><td><code>integer</code></td><td>IdleSessionTTLInSeconds of the resource</td></tr>
<tr><td><code>BotLocales</code></td><td><code>array</code></td><td>List of bot locales</td></tr>
<tr><td><code>BotFileS3Location</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>BotTags</code></td><td><code>array</code></td><td>A list of tags to add to the bot, which can only be added at bot creation.</td></tr>
<tr><td><code>TestBotAliasTags</code></td><td><code>array</code></td><td>A list of tags to add to the test alias for a bot, , which can only be added at bot&#x2F;bot alias creation.</td></tr>
<tr><td><code>AutoBuildBotLocales</code></td><td><code>boolean</code></td><td>Specifies whether to build the bot locales after bot creation completes.</td></tr>
<tr><td><code>TestBotAliasSettings</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lex.bot
WHERE region = 'us-east-1' AND data__Identifier = '&lt;Id&gt;'
</pre>
