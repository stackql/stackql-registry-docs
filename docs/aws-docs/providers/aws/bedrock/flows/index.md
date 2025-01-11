---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
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

Creates, updates, deletes or gets a <code>flow</code> resource or lists <code>flows</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Bedrock::Flow Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.bedrock.flows" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn representation of the Flow</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="definition" /></td><td><code>object</code></td><td>Flow definition</td></tr>
<tr><td><CopyableCode code="definition_string" /></td><td><code>string</code></td><td>A JSON string containing a Definition with the same schema as the Definition property of this resource</td></tr>
<tr><td><CopyableCode code="definition_s3_location" /></td><td><code>object</code></td><td>An Amazon S3 location.</td></tr>
<tr><td><CopyableCode code="definition_substitutions" /></td><td><code>object</code></td><td>When supplied with DefinitionString or DefinitionS3Location, substrings in the definition matching $&#123;keyname&#125; will be replaced with the associated value from this map</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>ARN of a IAM role</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Identifier for a Flow</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name for the flow</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Schema Type for Flow APIs</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>Time Stamp.</td></tr>
<tr><td><CopyableCode code="customer_encryption_key_arn" /></td><td><code>string</code></td><td>A KMS key ARN</td></tr>
<tr><td><CopyableCode code="validations" /></td><td><code>array</code></td><td>List of flow validations</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Draft Version.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="test_alias_tags" /></td><td><code>object</code></td><td>A map of tag keys and values</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrock-flow.html"><code>AWS::Bedrock::Flow</code></a>.

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
    <td><CopyableCode code="ExecutionRoleArn, Name, region" /></td>
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
Gets all <code>flows</code> in a region.
```sql
SELECT
region,
arn,
created_at,
definition,
definition_string,
definition_s3_location,
definition_substitutions,
description,
execution_role_arn,
id,
name,
status,
updated_at,
customer_encryption_key_arn,
validations,
version,
tags,
test_alias_tags
FROM aws.bedrock.flows
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>flow</code>.
```sql
SELECT
region,
arn,
created_at,
definition,
definition_string,
definition_s3_location,
definition_substitutions,
description,
execution_role_arn,
id,
name,
status,
updated_at,
customer_encryption_key_arn,
validations,
version,
tags,
test_alias_tags
FROM aws.bedrock.flows
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flow</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.bedrock.flows (
 ExecutionRoleArn,
 Name,
 region
)
SELECT 
'{{ ExecutionRoleArn }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.bedrock.flows (
 Definition,
 DefinitionString,
 DefinitionS3Location,
 DefinitionSubstitutions,
 Description,
 ExecutionRoleArn,
 Name,
 CustomerEncryptionKeyArn,
 Tags,
 TestAliasTags,
 region
)
SELECT 
 '{{ Definition }}',
 '{{ DefinitionString }}',
 '{{ DefinitionS3Location }}',
 '{{ DefinitionSubstitutions }}',
 '{{ Description }}',
 '{{ ExecutionRoleArn }}',
 '{{ Name }}',
 '{{ CustomerEncryptionKeyArn }}',
 '{{ Tags }}',
 '{{ TestAliasTags }}',
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
  - name: flow
    props:
      - name: Definition
        value:
          Nodes:
            - Name: '{{ Name }}'
              Type: '{{ Type }}'
              Configuration: null
              Inputs:
                - Name: '{{ Name }}'
                  Type: '{{ Type }}'
                  Expression: '{{ Expression }}'
              Outputs:
                - Name: '{{ Name }}'
                  Type: null
          Connections:
            - Type: '{{ Type }}'
              Name: '{{ Name }}'
              Source: '{{ Source }}'
              Target: '{{ Target }}'
              Configuration: null
      - name: DefinitionString
        value: '{{ DefinitionString }}'
      - name: DefinitionS3Location
        value:
          URI: '{{ URI }}'
      - name: DefinitionSubstitutions
        value: {}
      - name: Description
        value: '{{ Description }}'
      - name: ExecutionRoleArn
        value: '{{ ExecutionRoleArn }}'
      - name: Name
        value: '{{ Name }}'
      - name: CustomerEncryptionKeyArn
        value: '{{ CustomerEncryptionKeyArn }}'
      - name: Tags
        value: {}
      - name: TestAliasTags
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.bedrock.flows
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>flows</code> resource, the following permissions are required:

### Create
```json
bedrock:CreateFlow,
bedrock:GetFlow,
bedrock:PrepareFlow,
iam:PassRole,
s3:GetObject,
s3:GetObjectVersion,
bedrock:TagResource,
bedrock:ListTagsForResource,
kms:GenerateDataKey,
kms:Decrypt,
bedrock:CreateGuardrail,
bedrock:CreateGuardrailVersion,
bedrock:GetGuardrail
```

### Read
```json
bedrock:GetFlow,
bedrock:ListTagsForResource,
kms:Decrypt,
bedrock:GetGuardrail
```

### Update
```json
bedrock:UpdateFlow,
bedrock:GetFlow,
bedrock:PrepareFlow,
iam:PassRole,
s3:GetObject,
s3:GetObjectVersion,
bedrock:TagResource,
bedrock:UntagResource,
bedrock:ListTagsForResource,
kms:GenerateDataKey,
kms:Decrypt,
bedrock:UpdateGuardrail,
bedrock:GetGuardrail
```

### Delete
```json
bedrock:DeleteFlow,
bedrock:GetFlow,
bedrock:DeleteGuardrail,
bedrock:GetGuardrail
```

### List
```json
bedrock:ListFlows,
bedrock:ListGuardrails
```
