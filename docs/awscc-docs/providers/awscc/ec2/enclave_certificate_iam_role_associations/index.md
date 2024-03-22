---
title: enclave_certificate_iam_role_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - enclave_certificate_iam_role_associations
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
Retrieves a list of <code>enclave_certificate_iam_role_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enclave_certificate_iam_role_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>enclave_certificate_iam_role_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.enclave_certificate_iam_role_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>certificate_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.</td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
certificate_arn,
role_arn
FROM awscc.ec2.enclave_certificate_iam_role_associations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>enclave_certificate_iam_role_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateEnclaveCertificateIamRole
```

### List
```json
ec2:GetAssociatedEnclaveCertificateIamRoles
```

