---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - quicksight
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

Creates, updates, deletes or gets a <code>topic</code> resource or lists <code>topics</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of the AWS::QuickSight::Topic Resource Type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.quicksight.topics" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="data_sets" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="topic_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="user_experience_version" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>topics</code> in a region.
```sql
SELECT
region,
aws_account_id,
topic_id
FROM aws.quicksight.topics
WHERE region = 'us-east-1';
```
Gets all properties from a <code>topic</code>.
```sql
SELECT
region,
arn,
aws_account_id,
data_sets,
description,
name,
topic_id,
user_experience_version
FROM aws.quicksight.topics
WHERE region = 'us-east-1' AND data__Identifier = '<AwsAccountId>|<TopicId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>topic</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.quicksight.topics (
 AwsAccountId,
 DataSets,
 Description,
 Name,
 TopicId,
 UserExperienceVersion,
 region
)
SELECT 
'{{ AwsAccountId }}',
 '{{ DataSets }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ TopicId }}',
 '{{ UserExperienceVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.quicksight.topics (
 AwsAccountId,
 DataSets,
 Description,
 Name,
 TopicId,
 UserExperienceVersion,
 region
)
SELECT 
 '{{ AwsAccountId }}',
 '{{ DataSets }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ TopicId }}',
 '{{ UserExperienceVersion }}',
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
  - name: topic
    props:
      - name: AwsAccountId
        value: '{{ AwsAccountId }}'
      - name: DataSets
        value:
          - DatasetArn: '{{ DatasetArn }}'
            DatasetName: '{{ DatasetName }}'
            DatasetDescription: '{{ DatasetDescription }}'
            DataAggregation:
              DatasetRowDateGranularity: '{{ DatasetRowDateGranularity }}'
              DefaultDateColumnName: '{{ DefaultDateColumnName }}'
            Filters:
              - FilterDescription: '{{ FilterDescription }}'
                FilterClass: '{{ FilterClass }}'
                FilterName: '{{ FilterName }}'
                FilterSynonyms:
                  - '{{ FilterSynonyms[0] }}'
                OperandFieldName: '{{ OperandFieldName }}'
                FilterType: '{{ FilterType }}'
                CategoryFilter:
                  CategoryFilterFunction: '{{ CategoryFilterFunction }}'
                  CategoryFilterType: '{{ CategoryFilterType }}'
                  Constant:
                    ConstantType: '{{ ConstantType }}'
                    SingularConstant: '{{ SingularConstant }}'
                    CollectiveConstant:
                      ValueList:
                        - '{{ ValueList[0] }}'
                  Inverse: '{{ Inverse }}'
                NumericEqualityFilter:
                  Constant:
                    ConstantType: null
                    SingularConstant: '{{ SingularConstant }}'
                  Aggregation: '{{ Aggregation }}'
                NumericRangeFilter:
                  Inclusive: '{{ Inclusive }}'
                  Constant:
                    ConstantType: null
                    RangeConstant:
                      Minimum: '{{ Minimum }}'
                      Maximum: '{{ Maximum }}'
                  Aggregation: null
                DateRangeFilter:
                  Inclusive: '{{ Inclusive }}'
                  Constant: null
                RelativeDateFilter:
                  TimeGranularity: null
                  RelativeDateFilterFunction: '{{ RelativeDateFilterFunction }}'
                  Constant: null
            Columns:
              - ColumnName: '{{ ColumnName }}'
                ColumnFriendlyName: '{{ ColumnFriendlyName }}'
                ColumnDescription: '{{ ColumnDescription }}'
                ColumnSynonyms:
                  - '{{ ColumnSynonyms[0] }}'
                ColumnDataRole: '{{ ColumnDataRole }}'
                Aggregation: '{{ Aggregation }}'
                IsIncludedInTopic: '{{ IsIncludedInTopic }}'
                DisableIndexing: '{{ DisableIndexing }}'
                ComparativeOrder:
                  UseOrdering: '{{ UseOrdering }}'
                  SpecifedOrder:
                    - '{{ SpecifedOrder[0] }}'
                  TreatUndefinedSpecifiedValues: '{{ TreatUndefinedSpecifiedValues }}'
                SemanticType:
                  TypeName: '{{ TypeName }}'
                  SubTypeName: '{{ SubTypeName }}'
                  TypeParameters: {}
                  TruthyCellValue: '{{ TruthyCellValue }}'
                  TruthyCellValueSynonyms:
                    - '{{ TruthyCellValueSynonyms[0] }}'
                  FalseyCellValue: '{{ FalseyCellValue }}'
                  FalseyCellValueSynonyms:
                    - '{{ FalseyCellValueSynonyms[0] }}'
                TimeGranularity: null
                AllowedAggregations:
                  - '{{ AllowedAggregations[0] }}'
                NotAllowedAggregations:
                  - null
                DefaultFormatting:
                  DisplayFormat: '{{ DisplayFormat }}'
                  DisplayFormatOptions:
                    UseBlankCellFormat: '{{ UseBlankCellFormat }}'
                    BlankCellFormat: '{{ BlankCellFormat }}'
                    DateFormat: '{{ DateFormat }}'
                    DecimalSeparator: '{{ DecimalSeparator }}'
                    GroupingSeparator: '{{ GroupingSeparator }}'
                    UseGrouping: '{{ UseGrouping }}'
                    FractionDigits: null
                    Prefix: '{{ Prefix }}'
                    Suffix: '{{ Suffix }}'
                    UnitScaler: '{{ UnitScaler }}'
                    NegativeFormat:
                      Prefix: '{{ Prefix }}'
                      Suffix: '{{ Suffix }}'
                    CurrencySymbol: '{{ CurrencySymbol }}'
                NeverAggregateInFilter: '{{ NeverAggregateInFilter }}'
                CellValueSynonyms:
                  - CellValue: '{{ CellValue }}'
                    Synonyms:
                      - '{{ Synonyms[0] }}'
                NonAdditive: '{{ NonAdditive }}'
            CalculatedFields:
              - CalculatedFieldName: '{{ CalculatedFieldName }}'
                CalculatedFieldDescription: '{{ CalculatedFieldDescription }}'
                Expression: '{{ Expression }}'
                CalculatedFieldSynonyms:
                  - '{{ CalculatedFieldSynonyms[0] }}'
                IsIncludedInTopic: '{{ IsIncludedInTopic }}'
                DisableIndexing: '{{ DisableIndexing }}'
                ColumnDataRole: null
                TimeGranularity: null
                DefaultFormatting: null
                Aggregation: null
                ComparativeOrder: null
                SemanticType: null
                AllowedAggregations:
                  - null
                NotAllowedAggregations:
                  - null
                NeverAggregateInFilter: '{{ NeverAggregateInFilter }}'
                CellValueSynonyms:
                  - null
                NonAdditive: '{{ NonAdditive }}'
            NamedEntities:
              - EntityName: '{{ EntityName }}'
                EntityDescription: '{{ EntityDescription }}'
                EntitySynonyms:
                  - '{{ EntitySynonyms[0] }}'
                SemanticEntityType:
                  TypeName: '{{ TypeName }}'
                  SubTypeName: '{{ SubTypeName }}'
                  TypeParameters: null
                Definition:
                  - FieldName: '{{ FieldName }}'
                    PropertyName: '{{ PropertyName }}'
                    PropertyRole: '{{ PropertyRole }}'
                    PropertyUsage: '{{ PropertyUsage }}'
                    Metric:
                      Aggregation: '{{ Aggregation }}'
                      AggregationFunctionParameters: {}
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: TopicId
        value: '{{ TopicId }}'
      - name: UserExperienceVersion
        value: '{{ UserExperienceVersion }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.quicksight.topics
WHERE data__Identifier = '<AwsAccountId|TopicId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>topics</code> resource, the following permissions are required:

### Create
```json
quicksight:CreateTopic,
quicksight:PassDataSet,
quicksight:DescribeTopicRefresh
```

### Read
```json
quicksight:DescribeTopic
```

### Update
```json
quicksight:UpdateTopic,
quicksight:PassDataSet,
quicksight:DescribeTopicRefresh
```

### Delete
```json
quicksight:DeleteTopic
```

### List
```json
quicksight:ListTopics
```

