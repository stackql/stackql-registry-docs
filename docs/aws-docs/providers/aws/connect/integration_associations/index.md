---
title: integration_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_associations
  - connect
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

Creates, updates, deletes or gets an <code>integration_association</code> resource or lists <code>integration_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::IntegrationAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.integration_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="integration_association_id" /></td><td><code>string</code></td><td>Identifier of the association with Connect Instance</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>Amazon Connect instance identifier</td></tr>
<tr><td><CopyableCode code="integration_arn" /></td><td><code>string</code></td><td>ARN of Integration being associated with the instance</td></tr>
<tr><td><CopyableCode code="integration_type" /></td><td><code>string</code></td><td>Specifies the integration type to be associated with the instance</td></tr>
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
    <td><CopyableCode code="InstanceId, IntegrationType, IntegrationArn, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>integration_associations</code> in a region.
```sql
SELECT
region,
instance_id,
integration_type,
integration_arn
FROM aws.connect.integration_associations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>integration_association</code>.
```sql
SELECT
region,
integration_association_id,
instance_id,
integration_arn,
integration_type
FROM aws.connect.integration_associations
WHERE region = 'us-east-1' AND data__Identifier = '<InstanceId>|<IntegrationType>|<IntegrationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.integration_associations (
 InstanceId,
 IntegrationArn,
 IntegrationType,
 region
)
SELECT 
'{{ InstanceId }}',
 '{{ IntegrationArn }}',
 '{{ IntegrationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.integration_associations (
 InstanceId,
 IntegrationArn,
 IntegrationType,
 region
)
SELECT 
 '{{ InstanceId }}',
 '{{ IntegrationArn }}',
 '{{ IntegrationType }}',
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
  - name: integration_association
    props:
      - name: InstanceId
        value: '{{ InstanceId }}'
      - name: IntegrationArn
        value: '{{ IntegrationArn }}'
      - name: IntegrationType
        value: '{{ IntegrationType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.integration_associations
WHERE data__Identifier = '<InstanceId|IntegrationType|IntegrationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>integration_associations</code> resource, the following permissions are required:

### Create
```json
connect:DescribeInstance,
ds:DescribeDirectories,
app-integrations:CreateEventIntegrationAssociation,
mobiletargeting:GetApp,
cases:GetDomain,
wisdom:GetAssistant,
wisdom:GetKnowledgeBase,
wisdom:TagResource,
voiceid:DescribeDomain,
events:PutTargets,
events:PutRule,
connect:AssociateBot,
connect:AssociateLambdaFunction,
connect:CreateIntegrationAssociation,
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations,
lambda:addPermission,
lex:GetBot,
lex:DescribeBotAlias,
lex:CreateResourcePolicy,
lex:UpdateResourcePolicy,
lex:CreateResourcePolicyStatement,
lambda:AddPermission,
app-integrations:GetApplication,
app-integrations:CreateApplicationAssociation,
iam:AttachRolePolicy,
iam:CreateServiceLinkedRole,
iam:GetRolePolicy,
iam:PutRolePolicy
```

### Read
```json
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations
```

### Delete
```json
connect:DescribeInstance,
ds:DescribeDirectories,
app-integrations:DeleteEventIntegrationAssociation,
app-integrations:DeleteApplicationAssociation,
events:ListTargetsByRule,
events:RemoveTargets,
events:DeleteRule,
connect:DisassociateBot,
connect:DisassociateLambdaFunction,
connect:DeleteIntegrationAssociation,
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations,
lex:DeleteResourcePolicy,
lex:DeleteResourcePolicyStatement,
lambda:RemovePermission,
iam:GetRolePolicy,
iam:DeleteRolePolicy,
iam:PutRolePolicy
```

### List
```json
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations
```

