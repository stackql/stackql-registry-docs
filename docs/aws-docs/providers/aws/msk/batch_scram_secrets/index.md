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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>batch_scram_secrets</code> in a region or to create or delete a <code>batch_scram_secrets</code> resource, use <code>batch_scram_secret</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_scram_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::MSK::BatchScramSecret</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.msk.batch_scram_secrets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="cluster_arn" /></td><td><code>string</code></td><td></td></tr>
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
cluster_arn
FROM aws.msk.batch_scram_secrets
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
 "ClusterArn": "{{ ClusterArn }}"
}
>>>
--required properties only
INSERT INTO aws.msk.batch_scram_secrets (
 ClusterArn,
 region
)
SELECT 
{{ ClusterArn }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ClusterArn": "{{ ClusterArn }}",
 "SecretArnList": [
  "{{ SecretArnList[0] }}"
 ]
}
>>>
--all properties
INSERT INTO aws.msk.batch_scram_secrets (
 ClusterArn,
 SecretArnList,
 region
)
SELECT 
 {{ ClusterArn }},
 {{ SecretArnList }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.msk.batch_scram_secrets
WHERE data__Identifier = '<ClusterArn>'
AND region = 'us-east-1';
```

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

### Delete
```json
kafka:BatchDisassociateScramSecret,
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey
```

### List
```json
kafka:ListScramSecrets,
kms:CreateGrant,
kms:DescribeKey,
secretsmanager:GetSecretValue
```

