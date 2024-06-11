---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - sagemaker
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

Creates, updates, deletes or gets a <code>pipeline</code> resource or lists <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Pipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>The name of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_display_name" /></td><td><code>string</code></td><td>The display name of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_description" /></td><td><code>string</code></td><td>The description of the Pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>Role Arn</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="parallelism_configuration" /></td><td><code>object</code></td><td></td></tr>
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
    <td><CopyableCode code="PipelineName, PipelineDefinition, RoleArn, region" /></td>
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
List all <code>pipelines</code> in a region.
```sql
SELECT
region,
pipeline_name
FROM aws.sagemaker.pipelines
WHERE region = 'us-east-1';
```
Gets all properties from a <code>pipeline</code>.
```sql
SELECT
region,
pipeline_name,
pipeline_display_name,
pipeline_description,
pipeline_definition,
role_arn,
tags,
parallelism_configuration
FROM aws.sagemaker.pipelines
WHERE region = 'us-east-1' AND data__Identifier = '<PipelineName>';
```


## `INSERT` example

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
INSERT INTO aws.sagemaker.pipelines (
 PipelineName,
 PipelineDefinition,
 RoleArn,
 region
)
SELECT 
'{{ PipelineName }}',
 '{{ PipelineDefinition }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sagemaker.pipelines (
 PipelineName,
 PipelineDisplayName,
 PipelineDescription,
 PipelineDefinition,
 RoleArn,
 Tags,
 ParallelismConfiguration,
 region
)
SELECT 
 '{{ PipelineName }}',
 '{{ PipelineDisplayName }}',
 '{{ PipelineDescription }}',
 '{{ PipelineDefinition }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ ParallelismConfiguration }}',
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
      - name: PipelineName
        value: '{{ PipelineName }}'
      - name: PipelineDisplayName
        value: '{{ PipelineDisplayName }}'
      - name: PipelineDescription
        value: '{{ PipelineDescription }}'
      - name: PipelineDefinition
        value: {}
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'
      - name: ParallelismConfiguration
        value:
          MaxParallelExecutionSteps: '{{ MaxParallelExecutionSteps }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sagemaker.pipelines
WHERE data__Identifier = '<PipelineName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
s3:GetObject,
sagemaker:CreatePipeline,
sagemaker:DescribePipeline,
sagemaker:AddTags,
sagemaker:ListTags
```

### Read
```json
sagemaker:DescribePipeline,
sagemaker:ListTags
```

### Update
```json
iam:PassRole,
s3:GetObject,
sagemaker:UpdatePipeline,
sagemaker:DescribePipeline,
sagemaker:AddTags,
sagemaker:DeleteTags,
sagemaker:ListTags
```

### Delete
```json
sagemaker:DeletePipeline
```

### List
```json
sagemaker:ListPipelines
```

