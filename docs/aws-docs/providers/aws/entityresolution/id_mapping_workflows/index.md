---
title: id_mapping_workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - id_mapping_workflows
  - entityresolution
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

Creates, updates, deletes or gets an <code>id_mapping_workflow</code> resource or lists <code>id_mapping_workflows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_mapping_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdMappingWorkflow defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.id_mapping_workflows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the IdMappingWorkflow</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the IdMappingWorkflow</td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="output_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id_mapping_techniques" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_arn" /></td><td><code>The default IdMappingWorkflow arn</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>The time of this SchemaMapping got created</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>The time of this SchemaMapping got last updated at</code></td><td></td></tr>
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
    <td><CopyableCode code="WorkflowName, InputSourceConfig, IdMappingTechniques, RoleArn, region" /></td>
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
List all <code>id_mapping_workflows</code> in a region.
```sql
SELECT
region,
workflow_name
FROM aws.entityresolution.id_mapping_workflows
WHERE region = 'us-east-1';
```
Gets all properties from an <code>id_mapping_workflow</code>.
```sql
SELECT
region,
workflow_name,
description,
input_source_config,
output_source_config,
id_mapping_techniques,
role_arn,
tags,
workflow_arn,
created_at,
updated_at
FROM aws.entityresolution.id_mapping_workflows
WHERE region = 'us-east-1' AND data__Identifier = '<WorkflowName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>id_mapping_workflow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.entityresolution.id_mapping_workflows (
 WorkflowName,
 InputSourceConfig,
 IdMappingTechniques,
 RoleArn,
 region
)
SELECT 
'{{ WorkflowName }}',
 '{{ InputSourceConfig }}',
 '{{ IdMappingTechniques }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.entityresolution.id_mapping_workflows (
 WorkflowName,
 Description,
 InputSourceConfig,
 OutputSourceConfig,
 IdMappingTechniques,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ WorkflowName }}',
 '{{ Description }}',
 '{{ InputSourceConfig }}',
 '{{ OutputSourceConfig }}',
 '{{ IdMappingTechniques }}',
 '{{ RoleArn }}',
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
  - name: id_mapping_workflow
    props:
      - name: WorkflowName
        value: '{{ WorkflowName }}'
      - name: Description
        value: '{{ Description }}'
      - name: InputSourceConfig
        value:
          - InputSourceARN: '{{ InputSourceARN }}'
            SchemaArn: '{{ SchemaArn }}'
            Type: '{{ Type }}'
      - name: OutputSourceConfig
        value:
          - OutputS3Path: '{{ OutputS3Path }}'
            KMSArn: '{{ KMSArn }}'
      - name: IdMappingTechniques
        value:
          IdMappingType: '{{ IdMappingType }}'
          ProviderProperties:
            ProviderServiceArn: '{{ ProviderServiceArn }}'
            ProviderConfiguration: {}
            IntermediateSourceConfiguration:
              IntermediateS3Path: '{{ IntermediateS3Path }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.entityresolution.id_mapping_workflows
WHERE data__Identifier = '<WorkflowName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>id_mapping_workflows</code> resource, the following permissions are required:

### Create
```json
entityresolution:CreateIdMappingWorkflow,
entityresolution:GetIdMappingWorkflow,
entityresolution:TagResource,
kms:CreateGrant,
kms:DescribeKey,
iam:PassRole
```

### Update
```json
entityresolution:GetIdMappingWorkflow,
entityresolution:UpdateIdMappingWorkflow,
entityresolution:ListTagsForResource,
entityresolution:TagResource,
entityresolution:UntagResource,
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey
```

### Read
```json
entityresolution:GetIdMappingWorkflow,
entityresolution:ListTagsForResource
```

### Delete
```json
entityresolution:DeleteIdMappingWorkflow,
entityresolution:GetIdMappingWorkflow,
entityresolution:UntagResource
```

### List
```json
entityresolution:ListIdMappingWorkflows
```

