---
title: trust_store_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - trust_store_tags
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

Expands all tag keys and values for <code>trust_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticLoadBalancingV2::TrustStore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.trust_store_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the trust store.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_bucket" /></td><td><code>string</code></td><td>The name of the S3 bucket to fetch the CA certificate bundle from.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_key" /></td><td><code>string</code></td><td>The name of the S3 object to fetch the CA certificate bundle from.</td></tr>
<tr><td><CopyableCode code="ca_certificates_bundle_s3_object_version" /></td><td><code>string</code></td><td>The version of the S3 bucket that contains the CA certificate bundle.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the trust store, could be either of ACTIVE or CREATING.</td></tr>
<tr><td><CopyableCode code="number_of_ca_certificates" /></td><td><code>integer</code></td><td>The number of certificates associated with the trust store.</td></tr>
<tr><td><CopyableCode code="trust_store_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>trust_stores</code> in a region.
```sql
SELECT
region,
name,
ca_certificates_bundle_s3_bucket,
ca_certificates_bundle_s3_key,
ca_certificates_bundle_s3_object_version,
status,
number_of_ca_certificates,
trust_store_arn,
tag_key,
tag_value
FROM aws.elasticloadbalancingv2.trust_store_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>trust_store_tags</code> resource, see <a href="/providers/aws/elasticloadbalancingv2/trust_stores/#permissions"><code>trust_stores</code></a>

