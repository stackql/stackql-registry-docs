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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>batch_scram_secret</code> resource, use <code>batch_scram_secrets</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secret</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::BatchScramSecret</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.batch_scram_secret" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="secret_arn_list" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
cluster_arn,
secret_arn_list
FROM aws.msk.batch_scram_secret
WHERE region = 'us-east-1' AND data__Identifier = '<ClusterArn>';
```


## Permissions

To operate on the <code>batch_scram_secret</code> resource, the following permissions are required:

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

