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


Used to retrieve a list of <code>integration_associations</code> in a region or to create or delete a <code>integration_associations</code> resource, use <code>integration_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::IntegrationAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.integration_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="integration_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="integration_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
instance_id,
integration_type,
integration_arn
FROM aws.connect.integration_associations
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
 "InstanceId": "{{ InstanceId }}",
 "IntegrationArn": "{{ IntegrationArn }}",
 "IntegrationType": "{{ IntegrationType }}"
}
>>>
--required properties only
INSERT INTO aws.connect.integration_associations (
 InstanceId,
 IntegrationArn,
 IntegrationType,
 region
)
SELECT 
{{ .InstanceId }},
 {{ .IntegrationArn }},
 {{ .IntegrationType }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "InstanceId": "{{ InstanceId }}",
 "IntegrationArn": "{{ IntegrationArn }}",
 "IntegrationType": "{{ IntegrationType }}"
}
>>>
--all properties
INSERT INTO aws.connect.integration_associations (
 InstanceId,
 IntegrationArn,
 IntegrationType,
 region
)
SELECT 
 {{ .InstanceId }},
 {{ .IntegrationArn }},
 {{ .IntegrationType }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

