---
title: integration_association
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_association
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
Gets or operates on an individual <code>integration_association</code> resource, use <code>integration_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::IntegrationAssociation</td></tr>
<tr><td><b>Id</b></td><td><code>aws.connect.integration_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>integration_association_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>integration_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
integration_association_id,
instance_id,
integration_arn,
integration_type
FROM aws.connect.integration_association
WHERE data__Identifier = '<InstanceId>|<IntegrationType>|<IntegrationArn>';
```

## Permissions

To operate on the <code>integration_association</code> resource, the following permissions are required:

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

