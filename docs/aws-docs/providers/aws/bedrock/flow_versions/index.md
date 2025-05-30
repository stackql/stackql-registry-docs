---
title: flow_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_versions
  - bedrock
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

Creates, updates, deletes or gets a <code>flow_version</code> resource or lists <code>flow_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::FlowVersion Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.flow_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>Arn representation of the Flow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td>Flow definition</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow version</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>ARN of a IAM role</td></tr>
<tr><td><CopyableCode code="flow_id" /></td><td><code>string</code></td><td>Identifier for a Flow</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for the flow</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Schema Type for Flow APIs</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Numerical Version.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flowversion.html"><code>AWS::Bedrock::FlowVersion</code></a>.

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
    <td><CopyableCode code="FlowArn, region" /></td>
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
Gets all <code>flow_versions</code> in a region.
```sql
SELECT
region,
flow_arn,
created_at,
definition,
description,
execution_role_arn,
flow_id,
name,
status,
version,
customer_encryption_key_arn
FROM aws.bedrock.flow_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow_version</code>.
```sql
SELECT
region,
flow_arn,
created_at,
definition,
description,
execution_role_arn,
flow_id,
name,
status,
version,
customer_encryption_key_arn
FROM aws.bedrock.flow_versions
WHERE region = 'us-east-1' AND data__Identifier = '<FlowArn>|<Version>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.flow_versions (
 FlowArn,
 region
)
SELECT 
'{{ FlowArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.flow_versions (
 FlowArn,
 Description,
 region
)
SELECT 
 '{{ FlowArn }}',
 '{{ Description }}',
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
  - name: flow_version
    props:
      - name: FlowArn
        value: '{{ FlowArn }}'
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.flow_versions
WHERE data__Identifier = '<FlowArn|Version>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flow_versions</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateFlowVersion,
bedrock:GetFlowVersion,
kms:GenerateDataKey,
kms:Decrypt,
bedrock:CreateGuardrail,
bedrock:CreateGuardrailVersion,
bedrock:GetGuardrail
```

### Read
```json
bedrock:GetFlowVersion,
kms:Decrypt,
bedrock:GetGuardrail
```

### Delete
```json
bedrock:DeleteFlowVersion,
bedrock:GetFlowVersion,
bedrock:DeleteGuardrail,
bedrock:GetGuardrail
```

### List
```json
bedrock:ListFlowVersions,
bedrock:ListGuardrails
```

### Update
```json
noservice:NoAction
```
