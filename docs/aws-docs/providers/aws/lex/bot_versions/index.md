---
title: bot_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_versions
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
Used to retrieve a list of <code>bot_versions</code> in a region or create a <code>bot_versions</code> resource, use <code>bot_version</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.lex.bot_versions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>bot_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>bot_version</code></td><td><code>undefined</code></td><td></td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
bot_id,
bot_version
FROM aws.lex.bot_versions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>bot_versions</code> resource, the following permissions are required:

### Create
```json
lex:CreateBotVersion,
lex:DescribeBotVersion,
lex:DescribeBot,
lex:DescribeBotLocale,
lex:BuildBotLocale
```

### List
```json
lex:ListBotVersions
```

