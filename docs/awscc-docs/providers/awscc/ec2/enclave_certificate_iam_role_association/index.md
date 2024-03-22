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
Gets an individual <code>enclave_certificate_iam_role_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enclave_certificate_iam_role_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>enclave_certificate_iam_role_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.enclave_certificate_iam_role_association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.</td></tr>
<tr><td><code>certificate_s3_bucket_name</code></td><td><code>string</code></td><td>The name of the Amazon S3 bucket to which the certificate was uploaded.</td></tr>
<tr><td><code>certificate_s3_object_key</code></td><td><code>string</code></td><td>The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored.</td></tr>
<tr><td><code>encryption_kms_key_id</code></td><td><code>string</code></td><td>The ID of the AWS KMS CMK used to encrypt the private key of the certificate.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_arn,
role_arn,
certificate_s3_bucket_name,
certificate_s3_object_key,
encryption_kms_key_id
FROM awscc.ec2.enclave_certificate_iam_role_association
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

