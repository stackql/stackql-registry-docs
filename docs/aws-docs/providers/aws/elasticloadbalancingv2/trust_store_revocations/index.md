---
title: trust_store_revocations
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_store_revocations
  - elasticloadbalancingv2
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

Creates, updates, deletes or gets a <code>trust_store_revocation</code> resource or lists <code>trust_store_revocations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store_revocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStoreRevocation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.trust_store_revocations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="revocation_contents" /></td><td><code>array</code></td><td>The attributes required to create a trust store revocation.</td></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
<tr><td><CopyableCode code="revocation_id" /></td><td><code>integer</code></td><td>The ID associated with the revocation.</td></tr>
<tr><td><CopyableCode code="trust_store_revocations" /></td><td><code>array</code></td><td>The data associated with a trust store revocation</td></tr>
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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>trust_store_revocations</code> in a region.
```sql
SELECT
region,
revocation_contents,
trust_store_arn,
revocation_id,
trust_store_revocations
FROM aws.elasticloadbalancingv2.trust_store_revocations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>trust_store_revocation</code>.
```sql
SELECT
region,
revocation_contents,
trust_store_arn,
revocation_id,
trust_store_revocations
FROM aws.elasticloadbalancingv2.trust_store_revocations
WHERE region = 'us-east-1' AND data__Identifier = '<RevocationId>|<TrustStoreArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>trust_store_revocation</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticloadbalancingv2.trust_store_revocations (
 RevocationContents,
 TrustStoreArn,
 region
)
SELECT 
'{{ RevocationContents }}',
 '{{ TrustStoreArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticloadbalancingv2.trust_store_revocations (
 RevocationContents,
 TrustStoreArn,
 region
)
SELECT 
 '{{ RevocationContents }}',
 '{{ TrustStoreArn }}',
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
  - name: trust_store_revocation
    props:
      - name: RevocationContents
        value:
          - S3Bucket: '{{ S3Bucket }}'
            S3Key: '{{ S3Key }}'
            S3ObjectVersion: '{{ S3ObjectVersion }}'
            RevocationType: '{{ RevocationType }}'
      - name: TrustStoreArn
        value: '{{ TrustStoreArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticloadbalancingv2.trust_store_revocations
WHERE data__Identifier = '<RevocationId|TrustStoreArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trust_store_revocations</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:AddTrustStoreRevocations,
elasticloadbalancing:DescribeTrustStoreRevocations,
s3:GetObject,
s3:GetObjectVersion
```

### Delete
```json
elasticloadbalancing:DescribeTrustStoreRevocations,
elasticloadbalancing:RemoveTrustStoreRevocations
```

### List
```json
elasticloadbalancing:DescribeTrustStoreRevocations
```

### Read
```json
elasticloadbalancing:DescribeTrustStoreRevocations
```

