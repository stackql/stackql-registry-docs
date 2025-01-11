---
title: transformers
hide_title: false
hide_table_of_contents: false
keywords:
  - transformers
  - logs
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

Creates, updates, deletes or gets a <code>transformer</code> resource or lists <code>transformers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a transformer on the log group to transform logs into consistent structured and information rich format.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.logs.transformers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="log_group_identifier" /></td><td><code>string</code></td><td>Existing log group that you want to associate with this transformer.</td></tr>
<tr><td><CopyableCode code="transformer_config" /></td><td><code>array</code></td><td>List of processors in a transformer</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-transformer.html"><code>AWS::Logs::Transformer</code></a>.

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
    <td><CopyableCode code="LogGroupIdentifier, TransformerConfig, region" /></td>
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
Gets all <code>transformers</code> in a region.
```sql
SELECT
region,
log_group_identifier,
transformer_config
FROM aws.logs.transformers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transformer</code>.
```sql
SELECT
region,
log_group_identifier,
transformer_config
FROM aws.logs.transformers
WHERE region = 'us-east-1' AND data__Identifier = '<LogGroupIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transformer</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.logs.transformers (
 LogGroupIdentifier,
 TransformerConfig,
 region
)
SELECT 
'{{ LogGroupIdentifier }}',
 '{{ TransformerConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.logs.transformers (
 LogGroupIdentifier,
 TransformerConfig,
 region
)
SELECT 
 '{{ LogGroupIdentifier }}',
 '{{ TransformerConfig }}',
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
  - name: transformer
    props:
      - name: LogGroupIdentifier
        value: '{{ LogGroupIdentifier }}'
      - name: TransformerConfig
        value:
          - ParseCloudfront:
              Source: '{{ Source }}'
            ParseVPC:
              Source: null
            ParseWAF:
              Source: null
            ParseJSON:
              Source: '{{ Source }}'
              Destination: '{{ Destination }}'
            ParseRoute53:
              Source: null
            ParsePostgres:
              Source: null
            ParseKeyValue:
              Source: null
              Destination: null
              FieldDelimiter: '{{ FieldDelimiter }}'
              KeyValueDelimiter: '{{ KeyValueDelimiter }}'
              KeyPrefix: null
              NonMatchValue: null
              OverwriteIfExists: '{{ OverwriteIfExists }}'
            CopyValue:
              Entries:
                - Source: null
                  Target: null
                  OverwriteIfExists: '{{ OverwriteIfExists }}'
            Csv:
              QuoteCharacter: '{{ QuoteCharacter }}'
              Delimiter: '{{ Delimiter }}'
              Source: '{{ Source }}'
              Columns:
                - null
            DateTimeConverter:
              Source: null
              Target: null
              TargetFormat: '{{ TargetFormat }}'
              MatchPatterns:
                - null
              SourceTimezone: '{{ SourceTimezone }}'
              TargetTimezone: '{{ TargetTimezone }}'
              Locale: '{{ Locale }}'
            DeleteKeys:
              WithKeys:
                - '{{ WithKeys[0] }}'
            Grok:
              Source: null
              Match: '{{ Match }}'
            ListToMap:
              Source: null
              Key: null
              ValueKey: null
              Target: null
              Flatten: '{{ Flatten }}'
              FlattenedElement: '{{ FlattenedElement }}'
            AddKeys:
              Entries:
                - Key: null
                  Value: '{{ Value }}'
                  OverwriteIfExists: '{{ OverwriteIfExists }}'
            MoveKeys:
              Entries:
                - Source: null
                  Target: null
                  OverwriteIfExists: '{{ OverwriteIfExists }}'
            RenameKeys:
              Entries:
                - Key: null
                  RenameTo: null
                  OverwriteIfExists: '{{ OverwriteIfExists }}'
            LowerCaseString:
              WithKeys:
                - null
            SplitString:
              Entries:
                - Source: null
                  Delimiter: '{{ Delimiter }}'
            SubstituteString:
              Entries:
                - Source: null
                  From: null
                  To: null
            TrimString:
              WithKeys:
                - null
            UpperCaseString:
              WithKeys:
                - null
            TypeConverter:
              Entries:
                - Key: null
                  Type: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.logs.transformers
WHERE data__Identifier = '<LogGroupIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transformers</code> resource, the following permissions are required:

### Create
```json
logs:PutTransformer,
logs:GetTransformer
```

### Read
```json
logs:GetTransformer
```

### Update
```json
logs:GetTransformer,
logs:PutTransformer
```

### Delete
```json
logs:DeleteTransformer
```

### List
```json
logs:DescribeLogGroups,
logs:GetTransformer
```
