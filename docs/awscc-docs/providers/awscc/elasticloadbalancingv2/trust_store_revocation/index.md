---
title: trust_store_revocation
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_store_revocation
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
Gets an individual <code>trust_store_revocation</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store_revocation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_store_revocation</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticloadbalancingv2.trust_store_revocation</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>revocation_contents</code></td><td><code>array</code></td><td>The attributes required to create a trust store revocation.</td></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
<tr><td><code>revocation_id</code></td><td><code>integer</code></td><td>The ID associated with the revocation.</td></tr>
<tr><td><code>trust_store_revocations</code></td><td><code>array</code></td><td>The data associated with a trust store revocation</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
revocation_contents,
trust_store_arn,
revocation_id,
trust_store_revocations
FROM awscc.elasticloadbalancingv2.trust_store_revocation
WHERE region = 'us-east-1'
AND data__Identifier = '{RevocationId}';
AND data__Identifier = '{TrustStoreArn}';
```

## Permissions

To operate on the <code>trust_store_revocation</code> resource, the following permissions are required:

### Delete
```json
elasticloadbalancing:DescribeTrustStoreRevocations,
elasticloadbalancing:RemoveTrustStoreRevocations
```

### Read
```json
elasticloadbalancing:DescribeTrustStoreRevocations
```

