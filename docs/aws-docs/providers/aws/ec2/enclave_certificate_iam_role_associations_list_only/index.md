---
title: enclave_certificate_iam_role_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - enclave_certificate_iam_role_associations_list_only
  - ec2
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

Lists <code>enclave_certificate_iam_role_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/enclave_certificate_iam_role_associations/"><code>enclave_certificate_iam_role_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enclave_certificate_iam_role_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.enclave_certificate_iam_role_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.</td></tr>
<tr><td><CopyableCode code="certificate_s3_bucket_name" /></td><td><code>string</code></td><td>The name of the Amazon S3 bucket to which the certificate was uploaded.</td></tr>
<tr><td><CopyableCode code="certificate_s3_object_key" /></td><td><code>string</code></td><td>The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored.</td></tr>
<tr><td><CopyableCode code="encryption_kms_key_id" /></td><td><code>string</code></td><td>The ID of the AWS KMS CMK used to encrypt the private key of the certificate.</td></tr>
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
Lists all <code>enclave_certificate_iam_role_associations</code> in a region.
```sql
SELECT
region,
certificate_arn,
role_arn
FROM aws.ec2.enclave_certificate_iam_role_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>enclave_certificate_iam_role_associations_list_only</code> resource, see <a href="/providers/aws/ec2/enclave_certificate_iam_role_associations/#permissions"><code>enclave_certificate_iam_role_associations</code></a>


