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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>trust_store_revocation</code> resource, use <code>trust_store_revocations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store_revocation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStoreRevocation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.trust_store_revocation" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="revocation_contents" /></td><td><code>array</code></td><td>The attributes required to create a trust store revocation.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
revocation_contents,
trust_store_arn,
revocation_id,
trust_store_revocations
FROM aws.elasticloadbalancingv2.trust_store_revocation
WHERE data__Identifier = '<RevocationId>|<TrustStoreArn>';
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

