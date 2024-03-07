---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - redshiftserverless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>namespaces</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.redshiftserverless.namespaces</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>namespace_name</code></td><td><code>string</code></td><td>A unique identifier for the namespace. You use this identifier to refer to the namespace for any subsequent namespace operations such as deleting or modifying. All alphabetical characters must be lower case. Namespace name should be unique for all namespaces within an AWS account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>namespaces</code> resource, the following permissions are required:

### Create
<pre>
iam:PassRole,
kms:TagResource,
kms:UntagResource,
kms:ScheduleKeyDeletion,
kms:CancelKeyDeletion,
kms:Encrypt,
kms:Decrypt,
kms:DescribeKey,
kms:GenerateDataKeyPair,
kms:GenerateDataKey,
kms:CreateGrant,
kms:ListGrants,
kms:RevokeGrant,
kms:RetireGrant,
redshift-serverless:CreateNamespace,
redshift-serverless:GetNamespace,
redshift-serverless:ListSnapshotCopyConfigurations,
redshift-serverless:CreateSnapshotCopyConfiguration,
redshift:GetResourcePolicy,
redshift:PutResourcePolicy,
secretsmanager:CreateSecret,
secretsmanager:TagResource,
secretsmanager:RotateSecret,
secretsmanager:DescribeSecret</pre>

### List
<pre>
iam:PassRole,
redshift-serverless:ListNamespaces</pre>


## Example
```sql
SELECT
region,
namespace_name
FROM awscc.redshiftserverless.namespaces
WHERE region = 'us-east-1'
```
