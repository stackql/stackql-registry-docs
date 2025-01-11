---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - datapipeline
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
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datapipeline.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="activate" /></td><td><code>boolean</code></td><td>Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to true.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the pipeline.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the pipeline.</td></tr>
<tr><td><CopyableCode code="parameter_objects" /></td><td><code>array</code></td><td>The parameter objects used with the pipeline.</td></tr>
<tr><td><CopyableCode code="parameter_values" /></td><td><code>array</code></td><td>The parameter values used with the pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_objects" /></td><td><code>array</code></td><td>The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see Editing Your Pipeline in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><CopyableCode code="pipeline_tags" /></td><td><code>array</code></td><td>A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see Controlling Access to Pipelines and Resources in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><CopyableCode code="pipeline_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html"><code>AWS::DataPipeline::Pipeline</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>pipelines</code> in a region.
```sql
SELECT
region,
activate,
description,
name,
parameter_objects,
parameter_values,
pipeline_objects,
pipeline_tags,
pipeline_id
FROM aws.datapipeline.pipelines
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>pipeline</code>.
```sql
SELECT
region,
activate,
description,
name,
parameter_objects,
parameter_values,
pipeline_objects,
pipeline_tags,
pipeline_id
FROM aws.datapipeline.pipelines
WHERE region = 'us-east-1' AND data__Identifier = '<PipelineId>';
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
INSERT INTO aws.datapipeline.pipelines (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datapipeline.pipelines (
 Activate,
 Description,
 Name,
 ParameterObjects,
 ParameterValues,
 PipelineObjects,
 PipelineTags,
 region
)
SELECT 
 '{{ Activate }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ ParameterObjects }}',
 '{{ ParameterValues }}',
 '{{ PipelineObjects }}',
 '{{ PipelineTags }}',
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
      - name: Activate
        value: '{{ Activate }}'
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: ParameterObjects
        value:
          - Attributes:
              - Key: '{{ Key }}'
                StringValue: '{{ StringValue }}'
            Id: '{{ Id }}'
      - name: ParameterValues
        value:
          - Id: '{{ Id }}'
            StringValue: '{{ StringValue }}'
      - name: PipelineObjects
        value:
          - Fields:
              - Key: '{{ Key }}'
                RefValue: '{{ RefValue }}'
                StringValue: '{{ StringValue }}'
            Id: '{{ Id }}'
            Name: '{{ Name }}'
      - name: PipelineTags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datapipeline.pipelines
WHERE data__Identifier = '<PipelineId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pipelines</code> resource, the following permissions are required:

### Create
```json
datapipeline:CreatePipeline,
datapipeline:PutPipelineDefinition,
datapipeline:GetPipelineDefinition,
datapipeline:DescribePipelines,
datapipeline:ValidatePipelineDefinition,
datapipeline:ActivatePipeline,
datapipeline:AddTags,
iam:PassRole
```

### Read
```json
datapipeline:GetPipelineDefinition,
datapipeline:DescribePipelines
```

### Update
```json
datapipeline:PutPipelineDefinition,
datapipeline:AddTags,
datapipeline:RemoveTags,
datapipeline:DeactivatePipeline,
datapipeline:GetPipelineDefinition,
datapipeline:ActivatePipeline,
datapipeline:ValidatePipelineDefinition,
datapipeline:DescribePipelines,
datapipeline:AddTags,
datapipeline:RemoveTags,
iam:PassRole
```

### Delete
```json
datapipeline:DeletePipeline,
datapipeline:DescribePipelines,
datapipeline:GetPipelineDefinition,
datapipeline:RemoveTags
```

### List
```json
datapipeline:ListPipelines
```
