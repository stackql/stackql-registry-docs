---
title: associated_enclave_certificate_iam_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - associated_enclave_certificate_iam_roles
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associated_enclave_certificate_iam_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.associated_enclave_certificate_iam_roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `certificateS3BucketName` | `string` | The name of the Amazon S3 bucket in which the Amazon S3 object is stored. |
| `certificateS3ObjectKey` | `string` | The key of the Amazon S3 object ey where the certificate, certificate chain, and encrypted private key bundle is stored. The object key is formated as follows: &lt;code&gt;role_arn&lt;/code&gt;/&lt;code&gt;certificate_arn&lt;/code&gt;.  |
| `encryptionKmsKeyId` | `string` | The ID of the KMS customer master key (CMK) used to encrypt the private key. |
| `associatedRoleArn` | `string` | The ARN of the associated IAM role. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `associated_enclave_certificate_iam_roles_Get` | `SELECT` |  |
