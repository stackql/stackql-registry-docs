---
title: trust_store
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_store
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

Gets or operates on an individual <code>trust_store</code> resource, use <code>trust_stores</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.trust_store" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the trust store.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_bucket" /></td><td><code>string</code></td><td>The name of the S3 bucket to fetch the CA certificate bundle from.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_key" /></td><td><code>string</code></td><td>The name of the S3 object to fetch the CA certificate bundle from.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_object_version" /></td><td><code>string</code></td><td>The version of the S3 bucket that contains the CA certificate bundle.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the trust store, could be either of ACTIVE or CREATING.</td></tr>
<tr><td><CopyableCode code="number_of_ca_certificates" /></td><td><code>integer</code></td><td>The number of certificates associated with the trust store.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the trust store.</td></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
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
name,
ca_certificates_bundle_s3_bucket,
ca_certificates_bundle_s3_key,
ca_certificates_bundle_s3_object_version,
status,
number_of_ca_certificates,
tags,
trust_store_arn
FROM aws.elasticloadbalancingv2.trust_store
WHERE data__Identifier = '<TrustStoreArn>';
```

## Permissions

To operate on the <code>trust_store</code> resource, the following permissions are required:

### Delete
```json
elasticloadbalancing:DescribeTrustStores,
elasticloadbalancing:DeleteTrustStore
```

### Read
```json
elasticloadbalancing:DescribeTrustStores,
elasticloadbalancing:DescribeTags
```

### Update
```json
elasticloadbalancing:ModifyTrustStore,
elasticloadbalancing:AddTags,
elasticloadbalancing:RemoveTags,
s3:GetObject,
s3:GetObjectVersion
```

