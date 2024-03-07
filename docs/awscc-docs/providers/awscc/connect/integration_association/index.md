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
Gets an individual <code>integration_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.integration_association</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>integration_association</code> resource, the following permissions are required:

### Read
<pre>
connect:ListBots,
connect:ListLambdaFunctions,
connect:ListIntegrationAssociations</pre>

### Update
<pre>
</pre>

### Delete
<pre>
connect:DescribeInstance,
ds:DescribeDirectories,
app-integrations:DeleteEventIntegrationAssociation,
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
iam:PutRolePolicy</pre>


## Example
```sql
SELECT
region,
integration_association_id,
instance_id,
integration_arn,
integration_type
FROM awscc.connect.integration_association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;InstanceId&gt;'
AND data__Identifier = '&lt;IntegrationType&gt;'
AND data__Identifier = '&lt;IntegrationArn&gt;'
```
