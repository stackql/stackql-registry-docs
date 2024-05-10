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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>bot_aliases</code> in a region or to create or delete a <code>bot_aliases</code> resource, use <code>bot_alias</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Bot Alias enables you to change the version of a bot without updating applications that use the bot</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bot_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bot_alias_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
bot_alias_id,
bot_id
FROM aws.lex.bot_aliases
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>bot_alias</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- bot_alias.iql (required properties only)
INSERT INTO aws.lex.bot_aliases (
 BotId,
 BotAliasName,
 region
)
SELECT 
'{{ BotId }}',
 '{{ BotAliasName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- bot_alias.iql (all properties)
INSERT INTO aws.lex.bot_aliases (
 BotId,
 BotAliasLocaleSettings,
 BotAliasName,
 BotVersion,
 ConversationLogSettings,
 Description,
 SentimentAnalysisSettings,
 BotAliasTags,
 region
)
SELECT 
 '{{ BotId }}',
 '{{ BotAliasLocaleSettings }}',
 '{{ BotAliasName }}',
 '{{ BotVersion }}',
 '{{ ConversationLogSettings }}',
 '{{ Description }}',
 '{{ SentimentAnalysisSettings }}',
 '{{ BotAliasTags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: bot_alias
    props:
      - name: BotId
        value: '{{ BotId }}'
      - name: BotAliasLocaleSettings
        value:
          - LocaleId: '{{ LocaleId }}'
            BotAliasLocaleSetting:
              CodeHookSpecification:
                LambdaCodeHook:
                  CodeHookInterfaceVersion: '{{ CodeHookInterfaceVersion }}'
                  LambdaArn: '{{ LambdaArn }}'
              Enabled: '{{ Enabled }}'
      - name: BotAliasName
        value: '{{ BotAliasName }}'
      - name: BotVersion
        value:
          BotId: null
          Description: '{{ Description }}'
          BotVersionLocaleSpecification:
            - LocaleId: '{{ LocaleId }}'
              BotVersionLocaleDetails:
                SourceBotVersion: null
      - name: ConversationLogSettings
        value:
          AudioLogSettings:
            - Destination:
                S3Bucket:
                  S3BucketArn: '{{ S3BucketArn }}'
                  LogPrefix: '{{ LogPrefix }}'
                  KmsKeyArn: '{{ KmsKeyArn }}'
              Enabled: '{{ Enabled }}'
          TextLogSettings:
            - Destination:
                CloudWatch:
                  CloudWatchLogGroupArn: '{{ CloudWatchLogGroupArn }}'
                  LogPrefix: '{{ LogPrefix }}'
              Enabled: '{{ Enabled }}'
      - name: Description
        value: null
      - name: SentimentAnalysisSettings
        value:
          DetectSentiment: '{{ DetectSentiment }}'
      - name: BotAliasTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lex.bot_aliases
WHERE data__Identifier = '<BotAliasId|BotId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>bot_aliases</code> resource, the following permissions are required:

### Create
```json
lex:CreateBotAlias,
lex:DescribeBot
```

### Delete
```json
lex:DeleteBotAlias
```

### List
```json
lex:ListBotAliases
```

