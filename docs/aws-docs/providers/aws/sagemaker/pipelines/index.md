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


Used to retrieve a list of <code>pipelines</code> in a region or to create or delete a <code>pipelines</code> resource, use <code>pipeline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::Pipeline</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.pipelines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="pipeline_name" /></td><td><code>string</code></td><td>The name of the Pipeline.</td></tr>
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
pipeline_name
FROM aws.sagemaker.pipelines
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "PipelineName": "{{ PipelineName }}",
 "PipelineDefinition": {},
 "RoleArn": "{{ RoleArn }}"
}
>>>
--required properties only
INSERT INTO aws.sagemaker.pipelines (
 PipelineName,
 PipelineDefinition,
 RoleArn,
 region
)
SELECT 
{{ .PipelineName }},
 {{ .PipelineDefinition }},
 {{ .RoleArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "PipelineName": "{{ PipelineName }}",
 "PipelineDisplayName": "{{ PipelineDisplayName }}",
 "PipelineDescription": "{{ PipelineDescription }}",
 "PipelineDefinition": {},
 "RoleArn": "{{ RoleArn }}",
 "Tags": [
  {
   "Value": "{{ Value }}",
   "Key": "{{ Key }}"
  }
 ],
 "ParallelismConfiguration": {
  "MaxParallelExecutionSteps": "{{ MaxParallelExecutionSteps }}"
 }
}
>>>
--all properties
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
 {{ .PipelineName }},
 {{ .PipelineDisplayName }},
 {{ .PipelineDescription }},
 {{ .PipelineDefinition }},
 {{ .RoleArn }},
 {{ .Tags }},
 {{ .ParallelismConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
sagemaker:DeletePipeline
```

### List
```json
sagemaker:ListPipelines
```

