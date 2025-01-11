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
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the IdMappingWorkflow</td></tr>
<tr><td><CopyableCode code="input_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id_mapping_techniques" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_name" /></td><td><code>string</code></td><td>The name of the IdMappingWorkflow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got created</td></tr>
<tr><td><CopyableCode code="output_source_config" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_arn" /></td><td><code>string</code></td><td>The default IdMappingWorkflow arn</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The time of this SchemaMapping got last updated at</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-idmappingworkflow.html"><code>AWS::EntityResolution::IdMappingWorkflow</code></a>.

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
Gets all <code>id_mapping_workflows</code> in a region.
```sql
SELECT
region,
description,
input_source_config,
id_mapping_techniques,
workflow_name,
created_at,
output_source_config,
workflow_arn,
updated_at,
role_arn,
tags
FROM aws.entityresolution.id_mapping_workflows
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>id_mapping_workflow</code>.
```sql
SELECT
region,
description,
input_source_config,
id_mapping_techniques,
workflow_name,
created_at,
output_source_config,
workflow_arn,
updated_at,
role_arn,
tags
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
 InputSourceConfig,
 IdMappingTechniques,
 WorkflowName,
 RoleArn,
 region
)
SELECT 
'{{ InputSourceConfig }}',
 '{{ IdMappingTechniques }}',
 '{{ WorkflowName }}',
 '{{ RoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.entityresolution.id_mapping_workflows (
 Description,
 InputSourceConfig,
 IdMappingTechniques,
 WorkflowName,
 OutputSourceConfig,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ InputSourceConfig }}',
 '{{ IdMappingTechniques }}',
 '{{ WorkflowName }}',
 '{{ OutputSourceConfig }}',
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
      - name: Description
        value: '{{ Description }}'
      - name: InputSourceConfig
        value:
          - Type: '{{ Type }}'
            InputSourceARN: '{{ InputSourceARN }}'
            SchemaArn: '{{ SchemaArn }}'
      - name: IdMappingTechniques
        value:
          RuleBasedProperties:
            AttributeMatchingModel: '{{ AttributeMatchingModel }}'
            RuleDefinitionType: '{{ RuleDefinitionType }}'
            Rules:
              - RuleName: '{{ RuleName }}'
                MatchingKeys:
                  - '{{ MatchingKeys[0] }}'
            RecordMatchingModel: '{{ RecordMatchingModel }}'
          ProviderProperties:
            ProviderServiceArn: '{{ ProviderServiceArn }}'
            ProviderConfiguration: {}
            IntermediateSourceConfiguration:
              IntermediateS3Path: '{{ IntermediateS3Path }}'
          IdMappingType: '{{ IdMappingType }}'
      - name: WorkflowName
        value: '{{ WorkflowName }}'
      - name: OutputSourceConfig
        value:
          - KMSArn: '{{ KMSArn }}'
            OutputS3Path: '{{ OutputS3Path }}'
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

### Read
```json
entityresolution:GetIdMappingWorkflow,
entityresolution:ListTagsForResource
```

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

### List
```json
entityresolution:ListIdMappingWorkflows
```

### Delete
```json
entityresolution:DeleteIdMappingWorkflow,
entityresolution:GetIdMappingWorkflow,
entityresolution:UntagResource
```
