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


Used to retrieve a list of <code>id_mapping_workflows</code> in a region or to create or delete a <code>id_mapping_workflows</code> resource, use <code>id_mapping_workflow</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_mapping_workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>IdMappingWorkflow defined in AWS Entity Resolution service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.id_mapping_workflows" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>undefined</code></td><td>The name of the IdMappingWorkflow</td></tr>
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
workflow_name
FROM aws.entityresolution.id_mapping_workflows
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>id_mapping_workflow</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- id_mapping_workflow.iql (required properties only)
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
-- id_mapping_workflow.iql (all properties)
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

## `DELETE` Example

```sql
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

