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

Creates, updates, deletes or gets a <code>job</code> resource or lists <code>jobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Job.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.jobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td>Dataset name</td></tr>
<tr><td><CopyableCode code="encryption_key_arn" /></td><td><code>string</code></td><td>Encryption Key Arn</td></tr>
<tr><td><CopyableCode code="encryption_mode" /></td><td><code>string</code></td><td>Encryption mode</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Job name</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Job type</td></tr>
<tr><td><CopyableCode code="log_subscription" /></td><td><code>string</code></td><td>Log subscription</td></tr>
<tr><td><CopyableCode code="max_capacity" /></td><td><code>integer</code></td><td>Max capacity</td></tr>
<tr><td><CopyableCode code="max_retries" /></td><td><code>integer</code></td><td>Max retries</td></tr>
<tr><td><CopyableCode code="outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_catalog_outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="database_outputs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="output_location" /></td><td><code>object</code></td><td>Output location</td></tr>
<tr><td><CopyableCode code="project_name" /></td><td><code>string</code></td><td>Project name</td></tr>
<tr><td><CopyableCode code="recipe" /></td><td><code>object</code></td><td>Resource schema for AWS::DataBrew::Recipe.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role arn</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="timeout" /></td><td><code>integer</code></td><td>Timeout</td></tr>
<tr><td><CopyableCode code="job_sample" /></td><td><code>object</code></td><td>Job Sample</td></tr>
<tr><td><CopyableCode code="profile_configuration" /></td><td><code>object</code></td><td>Profile Job configuration</td></tr>
<tr><td><CopyableCode code="validation_configurations" /></td><td><code>array</code></td><td>Data quality rules configuration</td></tr>
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
    <td><CopyableCode code="Name, RoleArn, Type, region" /></td>
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
Gets all <code>jobs</code> in a region.
```sql
SELECT
region,
dataset_name,
encryption_key_arn,
encryption_mode,
name,
type,
log_subscription,
max_capacity,
max_retries,
outputs,
data_catalog_outputs,
database_outputs,
output_location,
project_name,
recipe,
role_arn,
tags,
timeout,
job_sample,
profile_configuration,
validation_configurations
FROM aws.databrew.jobs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>job</code>.
```sql
SELECT
region,
dataset_name,
encryption_key_arn,
encryption_mode,
name,
type,
log_subscription,
max_capacity,
max_retries,
outputs,
data_catalog_outputs,
database_outputs,
output_location,
project_name,
recipe,
role_arn,
tags,
timeout,
job_sample,
profile_configuration,
validation_configurations
FROM aws.databrew.jobs
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
databrew:DescribeJob,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateProfileJob,
databrew:UpdateRecipeJob,
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

