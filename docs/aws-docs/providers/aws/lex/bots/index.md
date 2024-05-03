---
title: bots
hide_title: false
hide_table_of_contents: false
keywords:
  - bots
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

Used to retrieve a list of <code>bots</code> in a region or create a <code>bots</code> resource, use <code>bot</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Amazon Lex conversational bot performing automated tasks such as ordering a pizza, booking a hotel, and so on.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bots" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id
FROM aws.lex.bots
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>bots</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
lex:DescribeBot,
lex:CreateUploadUrl,
lex:StartImport,
lex:DescribeImport,
lex:ListTagsForResource,
lex:TagResource,
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

### List
```json
lex:ListBots
```

