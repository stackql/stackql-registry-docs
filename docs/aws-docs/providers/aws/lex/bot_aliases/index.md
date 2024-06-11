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

Creates, updates, deletes or gets a <code>bot_alias</code> resource or lists <code>bot_aliases</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A Bot Alias enables you to change the version of a bot without updating applications that use the bot</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bot_aliases" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bot_alias_id" /></td><td><code>Unique ID of resource</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_id" /></td><td><code>Unique ID of resource</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_alias_status" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_alias_locale_settings" /></td><td><code>A list of bot alias locale settings to add to the bot alias.</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_alias_name" /></td><td><code>A unique identifier for a resource.</code></td><td></td></tr>
<tr><td><CopyableCode code="bot_version" /></td><td><code>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</code></td><td></td></tr>
<tr><td><CopyableCode code="conversation_log_settings" /></td><td><code>Contains information about code hooks that Amazon Lex calls during a conversation.</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>A description of the version. Use the description to help identify the version in lists.</code></td><td></td></tr>
<tr><td><CopyableCode code="sentiment_analysis_settings" /></td><td><code>object</code></td><td>Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.</td></tr>
<tr><td><CopyableCode code="bot_alias_tags" /></td><td><code>array</code></td><td>A list of tags to add to the bot alias.</td></tr>
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
    <td><CopyableCode code="BotId, BotAliasName, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>bot_aliases</code> in a region.
```sql
SELECT
region,
bot_alias_id,
bot_id
FROM aws.lex.bot_aliases
WHERE region = 'us-east-1';
```
Gets all properties from a <code>bot_alias</code>.
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
FROM aws.lex.bot_aliases
WHERE region = 'us-east-1' AND data__Identifier = '<BotAliasId>|<BotId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bot_alias</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
lex:ListBotAliases
```

