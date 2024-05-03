---
title: enclave_certificate_iam_role_association
hide_title: false
hide_table_of_contents: false
keywords:
  - enclave_certificate_iam_role_association
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

Gets or operates on an individual <code>enclave_certificate_iam_role_association</code> resource, use <code>enclave_certificate_iam_role_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enclave_certificate_iam_role_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.enclave_certificate_iam_role_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.</td></tr>
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
certificate_arn,
role_arn,
certificate_s3_bucket_name,
certificate_s3_object_key,
encryption_kms_key_id
FROM aws.ec2.enclave_certificate_iam_role_association
WHERE data__Identifier = '<CertificateArn>|<RoleArn>';
```

## Permissions

To operate on the <code>enclave_certificate_iam_role_association</code> resource, the following permissions are required:

### Read
```json
ec2:GetAssociatedEnclaveCertificateIamRoles
```

### Delete
```json
ec2:DisassociateEnclaveCertificateIamRole
```

