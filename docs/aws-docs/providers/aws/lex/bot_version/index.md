---
title: bot_version
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_version
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
Gets an individual <code>bot_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>bot_version</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lex.bot_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bot_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_version</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bot_version_locale_specification</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
bot_id,
bot_version,
description,
bot_version_locale_specification
FROM aws.lex.bot_version
WHERE region = 'us-east-1'
AND data__Identifier = '<BotId>'
AND data__Identifier = '<BotVersion>'
```
