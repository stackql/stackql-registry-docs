---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - iotanalytics
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


Used to retrieve a list of <code>datasets</code> in a region or to create or delete a <code>datasets</code> resource, use <code>dataset</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IoTAnalytics::Dataset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotanalytics.datasets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="dataset_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="Actions, region" /></td>
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
dataset_name
FROM aws.iotanalytics.datasets
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>dataset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotanalytics.datasets (
 Actions,
 region
)
SELECT 
'{{ Actions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotanalytics.datasets (
 Actions,
 LateDataRules,
 DatasetName,
 ContentDeliveryRules,
 Triggers,
 VersioningConfiguration,
 RetentionPeriod,
 Tags,
 region
)
SELECT 
 '{{ Actions }}',
 '{{ LateDataRules }}',
 '{{ DatasetName }}',
 '{{ ContentDeliveryRules }}',
 '{{ Triggers }}',
 '{{ VersioningConfiguration }}',
 '{{ RetentionPeriod }}',
 '{{ Tags }}',
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
  - name: dataset
    props:
      - name: Actions
        value:
          - ActionName: '{{ ActionName }}'
            ContainerAction:
              Variables:
                - VariableName: '{{ VariableName }}'
                  DatasetContentVersionValue:
                    DatasetName: '{{ DatasetName }}'
                  StringValue: '{{ StringValue }}'
                  DoubleValue: null
                  OutputFileUriValue:
                    FileName: '{{ FileName }}'
              ExecutionRoleArn: '{{ ExecutionRoleArn }}'
              Image: '{{ Image }}'
              ResourceConfiguration:
                VolumeSizeInGB: '{{ VolumeSizeInGB }}'
                ComputeType: '{{ ComputeType }}'
            QueryAction:
              Filters:
                - Filter: '{{ Filter }}'
                  Next: '{{ Next }}'
                  Name: '{{ Name }}'
              SqlQuery: '{{ SqlQuery }}'
      - name: LateDataRules
        value:
          - RuleConfiguration:
              DeltaTimeSessionWindowConfiguration:
                TimeoutInMinutes: '{{ TimeoutInMinutes }}'
            RuleName: '{{ RuleName }}'
      - name: DatasetName
        value: '{{ DatasetName }}'
      - name: ContentDeliveryRules
        value:
          - Destination:
              IotEventsDestinationConfiguration:
                InputName: '{{ InputName }}'
                RoleArn: '{{ RoleArn }}'
              S3DestinationConfiguration:
                GlueConfiguration:
                  DatabaseName: '{{ DatabaseName }}'
                  TableName: '{{ TableName }}'
                Bucket: '{{ Bucket }}'
                Key: '{{ Key }}'
                RoleArn: '{{ RoleArn }}'
            EntryName: '{{ EntryName }}'
      - name: Triggers
        value:
          - TriggeringDataset:
              DatasetName: '{{ DatasetName }}'
            Schedule:
              ScheduleExpression: '{{ ScheduleExpression }}'
      - name: VersioningConfiguration
        value:
          Unlimited: '{{ Unlimited }}'
          MaxVersions: '{{ MaxVersions }}'
      - name: RetentionPeriod
        value:
          NumberOfDays: '{{ NumberOfDays }}'
          Unlimited: '{{ Unlimited }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.iotanalytics.datasets
WHERE data__Identifier = '<DatasetName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>datasets</code> resource, the following permissions are required:

### Create
```json
iotanalytics:CreateDataset
```

### Delete
```json
iotanalytics:DeleteDataset
```

### List
```json
iotanalytics:ListDatasets
```

