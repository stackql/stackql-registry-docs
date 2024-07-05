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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>bot_version</code> resource or lists <code>bot_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bot_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bot_id" /></td><td><code>string</code></td><td>Unique ID of resource</td></tr>
<tr><td><CopyableCode code="bot_version" /></td><td><code>object</code></td><td>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the version. Use the description to help identify the version in lists.</td></tr>
<tr><td><CopyableCode code="bot_version_locale_specification" /></td><td><code>array</code></td><td>Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale.</td></tr>
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
    <td><CopyableCode code="BotId, BotVersionLocaleSpecification, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>bot_versions</code> in a region.
```sql
SELECT
region,
bot_id,
bot_version,
description,
bot_version_locale_specification
FROM aws.lex.bot_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>bot_version</code>.
```sql
SELECT
region,
bot_id,
bot_version,
description,
bot_version_locale_specification
FROM aws.lex.bot_versions
WHERE region = 'us-east-1' AND data__Identifier = '<BotId>|<BotVersion>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bot_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lex.bot_versions (
 BotId,
 BotVersionLocaleSpecification,
 region
)
SELECT 
'{{ BotId }}',
 '{{ BotVersionLocaleSpecification }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lex.bot_versions (
 BotId,
 Description,
 BotVersionLocaleSpecification,
 region
)
SELECT 
 '{{ BotId }}',
 '{{ Description }}',
 '{{ BotVersionLocaleSpecification }}',
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
  - name: bot_version
    props:
      - name: BotId
        value: '{{ BotId }}'
      - name: Description
        value: '{{ Description }}'
      - name: BotVersionLocaleSpecification
        value:
          - LocaleId: '{{ LocaleId }}'
            BotVersionLocaleDetails:
              SourceBotVersion:
                BotId: null
                Description: null
                BotVersionLocaleSpecification: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lex.bot_versions
WHERE data__Identifier = '<BotId|BotVersion>'
AND region = 'us-east-1';
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

### Read
```json
lex:DescribeBotVersion
```

### Delete
```json
lex:DeleteBotVersion,
lex:DescribeBotVersion
```

### List
```json
lex:ListBotVersions
```

