---
title: id_mapping_workflow
hide_title: false
hide_table_of_contents: false
keywords:
  - id_mapping_workflow
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
Gets an individual <code>id_mapping_workflow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>id_mapping_workflow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>id_mapping_workflow</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.entityresolution.id_mapping_workflow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workflow_name</code></td><td><code>string</code></td><td>The name of the IdMappingWorkflow</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the IdMappingWorkflow</td></tr>
<tr><td><code>input_source_config</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>output_source_config</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id_mapping_techniques</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>workflow_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.entityresolution.id_mapping_workflow
WHERE region = 'us-east-1'
AND data__Identifier = '{WorkflowName}';
```

## Permissions

To operate on the <code>id_mapping_workflow</code> resource, the following permissions are required:

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

