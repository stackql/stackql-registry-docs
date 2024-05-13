---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - osis
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


Used to retrieve a list of <code>pipelines</code> in a region or to create or delete a <code>pipelines</code> resource, use <code>pipeline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An OpenSearch Ingestion Service Data Prepper pipeline running Data Prepper.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.osis.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pipeline_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the pipeline.</td></tr>
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
    <td><CopyableCode code="MaxUnits, MinUnits, PipelineConfigurationBody, PipelineName, region" /></td>
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
pipeline_arn
FROM aws.osis.pipelines
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>pipeline</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.osis.pipelines (
 MaxUnits,
 MinUnits,
 PipelineConfigurationBody,
 PipelineName,
 region
)
SELECT 
'{{ MaxUnits }}',
 '{{ MinUnits }}',
 '{{ PipelineConfigurationBody }}',
 '{{ PipelineName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.osis.pipelines (
 BufferOptions,
 EncryptionAtRestOptions,
 LogPublishingOptions,
 MaxUnits,
 MinUnits,
 PipelineConfigurationBody,
 PipelineName,
 Tags,
 VpcOptions,
 region
)
SELECT 
 '{{ BufferOptions }}',
 '{{ EncryptionAtRestOptions }}',
 '{{ LogPublishingOptions }}',
 '{{ MaxUnits }}',
 '{{ MinUnits }}',
 '{{ PipelineConfigurationBody }}',
 '{{ PipelineName }}',
 '{{ Tags }}',
 '{{ VpcOptions }}',
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
  - name: pipeline
    props:
      - name: BufferOptions
        value:
          PersistentBufferEnabled: '{{ PersistentBufferEnabled }}'
      - name: EncryptionAtRestOptions
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
      - name: LogPublishingOptions
        value:
          IsLoggingEnabled: '{{ IsLoggingEnabled }}'
          CloudWatchLogDestination:
            LogGroup: '{{ LogGroup }}'
      - name: MaxUnits
        value: '{{ MaxUnits }}'
      - name: MinUnits
        value: '{{ MinUnits }}'
      - name: PipelineConfigurationBody
        value: '{{ PipelineConfigurationBody }}'
      - name: PipelineName
        value: '{{ PipelineName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcOptions
        value:
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.osis.pipelines
WHERE data__Identifier = '<PipelineArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
osis:CreatePipeline,
osis:GetPipeline,
osis:TagResource,
osis:ListTagsForResource,
iam:PassRole,
iam:CreateServiceLinkedRole,
logs:CreateLogDelivery,
kms:DescribeKey
```

### Delete
```json
osis:DeletePipeline,
osis:GetPipeline,
logs:GetLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries
```

### List
```json
osis:ListPipelines
```

