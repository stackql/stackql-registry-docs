---
title: policy_statements
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_statements
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

Creates, updates, deletes or gets a <code>policy_statement</code> resource or lists <code>policy_statements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_statements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Policy Statement defined in AWS Entity Resolution Service</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.entityresolution.policy_statements" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn of the resource to which the policy statement is being attached.</td></tr>
<tr><td><CopyableCode code="statement_id" /></td><td><code>string</code></td><td>The Statement Id of the policy statement that is being attached.</td></tr>
<tr><td><CopyableCode code="effect" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="condition" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-entityresolution-policystatement.html"><code>AWS::EntityResolution::PolicyStatement</code></a>.

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
    <td><CopyableCode code="Arn, StatementId, region" /></td>
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
Gets all <code>policy_statements</code> in a region.
```sql
SELECT
region,
arn,
statement_id,
effect,
action,
principal,
condition
FROM aws.entityresolution.policy_statements
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>policy_statement</code>.
```sql
SELECT
region,
arn,
statement_id,
effect,
action,
principal,
condition
FROM aws.entityresolution.policy_statements
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>|<StatementId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policy_statement</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.entityresolution.policy_statements (
 Arn,
 StatementId,
 region
)
SELECT 
'{{ Arn }}',
 '{{ StatementId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.entityresolution.policy_statements (
 Arn,
 StatementId,
 Effect,
 Action,
 Principal,
 Condition,
 region
)
SELECT 
 '{{ Arn }}',
 '{{ StatementId }}',
 '{{ Effect }}',
 '{{ Action }}',
 '{{ Principal }}',
 '{{ Condition }}',
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
  - name: policy_statement
    props:
      - name: Arn
        value: '{{ Arn }}'
      - name: StatementId
        value: '{{ StatementId }}'
      - name: Effect
        value: '{{ Effect }}'
      - name: Action
        value:
          - '{{ Action[0] }}'
      - name: Principal
        value:
          - '{{ Principal[0] }}'
      - name: Condition
        value: '{{ Condition }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.entityresolution.policy_statements
WHERE data__Identifier = '<Arn|StatementId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>policy_statements</code> resource, the following permissions are required:

### Create
```json
entityresolution:AddPolicyStatement
```

### Read
```json
entityresolution:GetPolicy
```

### Update
```json
entityresolution:AddPolicyStatement,
entityresolution:DeletePolicyStatement
```

### Delete
```json
entityresolution:DeletePolicyStatement,
entityresolution:GetPolicy
```

### List
```json
entityresolution:GetPolicy
```
