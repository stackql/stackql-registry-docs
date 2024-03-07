---
title: batch_scram_secret
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_scram_secret
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>batch_scram_secret</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>batch_scram_secret</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.batch_scram_secret</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>secret_arn_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>batch_scram_secret</code> resource, the following permissions are required:

### Delete
```json
kafka:BatchDisassociateScramSecret,
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey
```

### Read
```json
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey,
secretsmanager:GetSecretValue
```

### Update
```json
kafka:BatchAssociateScramSecret,
kafka:BatchDisassociateScramSecret,
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey,
secretsmanager:GetSecretValue
```


## Example
```sql
SELECT
region,
cluster_arn,
secret_arn_list
FROM awscc.msk.batch_scram_secret
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ClusterArn&gt;'
```
