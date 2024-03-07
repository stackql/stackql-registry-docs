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
Gets an individual <code>trust_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trust_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>trust_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticloadbalancingv2.trust_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the trust store.</td></tr>
<tr><td><code>ca_certificates_bundle_s3_bucket</code></td><td><code>string</code></td><td>The name of the S3 bucket to fetch the CA certificate bundle from.</td></tr>
<tr><td><code>ca_certificates_bundle_s3_key</code></td><td><code>string</code></td><td>The name of the S3 object to fetch the CA certificate bundle from.</td></tr>
<tr><td><code>ca_certificates_bundle_s3_object_version</code></td><td><code>string</code></td><td>The version of the S3 bucket that contains the CA certificate bundle.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the trust store, could be either of ACTIVE or CREATING.</td></tr>
<tr><td><code>number_of_ca_certificates</code></td><td><code>integer</code></td><td>The number of certificates associated with the trust store.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to assign to the trust store.</td></tr>
<tr><td><code>trust_store_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the trust store.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>trust_store</code> resource, the following permissions are required:

### Delete
<pre>
elasticloadbalancing:DescribeTrustStores,
elasticloadbalancing:DeleteTrustStore</pre>

### Read
<pre>
elasticloadbalancing:DescribeTrustStores,
elasticloadbalancing:DescribeTags</pre>

### Update
<pre>
elasticloadbalancing:ModifyTrustStore,
elasticloadbalancing:AddTags,
elasticloadbalancing:RemoveTags,
s3:GetObject,
s3:GetObjectVersion</pre>


## Example
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
FROM awscc.elasticloadbalancingv2.trust_store
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;TrustStoreArn&gt;'
```
