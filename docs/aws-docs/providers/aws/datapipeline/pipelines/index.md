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


Used to retrieve a list of <code>pipelines</code> in a region or to create or delete a <code>pipelines</code> resource, use <code>pipeline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datapipeline.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pipeline_id" /></td><td><code>string</code></td><td></td></tr>
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
pipeline_id
FROM aws.datapipeline.pipelines
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
-- pipeline.iql (required properties only)
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
-- pipeline.iql (all properties)
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

## `DELETE` Example

```sql
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

