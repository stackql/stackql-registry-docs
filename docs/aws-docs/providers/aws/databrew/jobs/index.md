---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - databrew
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


Used to retrieve a list of <code>jobs</code> in a region or to create or delete a <code>jobs</code> resource, use <code>job</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.jobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Job name</td></tr>
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
name
FROM aws.databrew.jobs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>job</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- job.iql (required properties only)
INSERT INTO aws.databrew.jobs (
 Name,
 Type,
 RoleArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ Type }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- job.iql (all properties)
INSERT INTO aws.databrew.jobs (
 DatasetName,
 EncryptionKeyArn,
 EncryptionMode,
 Name,
 Type,
 LogSubscription,
 MaxCapacity,
 MaxRetries,
 Outputs,
 DataCatalogOutputs,
 DatabaseOutputs,
 OutputLocation,
 ProjectName,
 Recipe,
 RoleArn,
 Tags,
 Timeout,
 JobSample,
 ProfileConfiguration,
 ValidationConfigurations,
 region
)
SELECT 
 '{{ DatasetName }}',
 '{{ EncryptionKeyArn }}',
 '{{ EncryptionMode }}',
 '{{ Name }}',
 '{{ Type }}',
 '{{ LogSubscription }}',
 '{{ MaxCapacity }}',
 '{{ MaxRetries }}',
 '{{ Outputs }}',
 '{{ DataCatalogOutputs }}',
 '{{ DatabaseOutputs }}',
 '{{ OutputLocation }}',
 '{{ ProjectName }}',
 '{{ Recipe }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ Timeout }}',
 '{{ JobSample }}',
 '{{ ProfileConfiguration }}',
 '{{ ValidationConfigurations }}',
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
  - name: job
    props:
      - name: DatasetName
        value: '{{ DatasetName }}'
      - name: EncryptionKeyArn
        value: '{{ EncryptionKeyArn }}'
      - name: EncryptionMode
        value: '{{ EncryptionMode }}'
      - name: Name
        value: '{{ Name }}'
      - name: Type
        value: '{{ Type }}'
      - name: LogSubscription
        value: '{{ LogSubscription }}'
      - name: MaxCapacity
        value: '{{ MaxCapacity }}'
      - name: MaxRetries
        value: '{{ MaxRetries }}'
      - name: Outputs
        value:
          - CompressionFormat: '{{ CompressionFormat }}'
            Format: '{{ Format }}'
            FormatOptions:
              Csv:
                Delimiter: '{{ Delimiter }}'
            PartitionColumns:
              - '{{ PartitionColumns[0] }}'
            Location:
              Bucket: '{{ Bucket }}'
              Key: '{{ Key }}'
            Overwrite: '{{ Overwrite }}'
            MaxOutputFiles: '{{ MaxOutputFiles }}'
      - name: DataCatalogOutputs
        value:
          - CatalogId: '{{ CatalogId }}'
            DatabaseName: '{{ DatabaseName }}'
            TableName: '{{ TableName }}'
            S3Options:
              Location: null
            DatabaseOptions:
              TempDirectory: null
              TableName: '{{ TableName }}'
            Overwrite: '{{ Overwrite }}'
      - name: DatabaseOutputs
        value:
          - GlueConnectionName: '{{ GlueConnectionName }}'
            DatabaseOutputMode: '{{ DatabaseOutputMode }}'
            DatabaseOptions: null
      - name: OutputLocation
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
          BucketOwner: '{{ BucketOwner }}'
      - name: ProjectName
        value: '{{ ProjectName }}'
      - name: Recipe
        value:
          Description: '{{ Description }}'
          Name: '{{ Name }}'
          Steps:
            - Action:
                Operation: '{{ Operation }}'
                Parameters: null
              ConditionExpressions:
                - Condition: '{{ Condition }}'
                  Value: '{{ Value }}'
                  TargetColumn: '{{ TargetColumn }}'
          Tags:
            - Key: '{{ Key }}'
              Value: '{{ Value }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - null
      - name: Timeout
        value: '{{ Timeout }}'
      - name: JobSample
        value:
          Mode: '{{ Mode }}'
          Size: '{{ Size }}'
      - name: ProfileConfiguration
        value:
          DatasetStatisticsConfiguration:
            IncludedStatistics:
              - '{{ IncludedStatistics[0] }}'
            Overrides:
              - Statistic: null
                Parameters: {}
          ProfileColumns:
            - Regex: '{{ Regex }}'
              Name: '{{ Name }}'
          ColumnStatisticsConfigurations:
            - Selectors:
                - null
              Statistics: null
          EntityDetectorConfiguration:
            EntityTypes:
              - '{{ EntityTypes[0] }}'
            AllowedStatistics:
              Statistics:
                - null
      - name: ValidationConfigurations
        value:
          - RulesetArn: '{{ RulesetArn }}'
            ValidationMode: '{{ ValidationMode }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.databrew.jobs
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>jobs</code> resource, the following permissions are required:

### Create
```json
databrew:CreateProfileJob,
databrew:CreateRecipeJob,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### Delete
```json
databrew:DeleteJob
```

### List
```json
databrew:ListJobs,
databrew:ListTagsForResource,
iam:ListRoles
```

