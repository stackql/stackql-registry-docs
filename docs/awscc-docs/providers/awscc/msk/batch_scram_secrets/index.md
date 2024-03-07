---
title: batch_scram_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_scram_secrets
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
Retrieves a list of <code>batch_scram_secrets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>batch_scram_secrets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.batch_scram_secrets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>cluster_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>batch_scram_secrets</code> resource, the following permissions are required:

### Create
```json
kafka:BatchAssociateScramSecret,
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey,
secretsmanager:GetSecretValue
```

### List
```json
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey,
secretsmanager:GetSecretValue
```


## Example
```sql
SELECT
region,
cluster_arn
FROM awscc.msk.batch_scram_secrets
WHERE region = 'us-east-1'
```
