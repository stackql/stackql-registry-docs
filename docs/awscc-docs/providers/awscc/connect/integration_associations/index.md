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
Retrieves a list of <code>integration_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.integration_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_id</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>integration_type</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>integration_arn</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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
iam:AttachRolePolicy,
iam:CreateServiceLinkedRole,
iam:GetRolePolicy,
iam:PutRolePolicy
```

### List
```json
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations
```


## Example
```sql
SELECT
region,
instance_id,
integration_type,
integration_arn
FROM awscc.connect.integration_associations
WHERE region = 'us-east-1'
```
