---
title: enclave_certificate_iam_role
hide_title: false
hide_table_of_contents: false
keywords:
  - enclave_certificate_iam_role
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
<tr><td><b>Name</b></td><td><code>enclave_certificate_iam_role</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.enclave_certificate_iam_role</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enclave_certificate_iam_role_Associate` | `EXEC` |  | &lt;p&gt;Associates an Identity and Access Management (IAM) role with an Certificate Manager (ACM) certificate. This enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave. For more information, see &lt;a href="https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html"&gt;Certificate Manager for Nitro Enclaves&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Nitro Enclaves User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When the IAM role is associated with the ACM certificate, the certificate, certificate chain, and encrypted private key are placed in an Amazon S3 bucket that only the associated IAM role can access. The private key of the certificate is encrypted with an Amazon Web Services managed key that has an attached attestation-based key policy.&lt;/p&gt; &lt;p&gt;To enable the IAM role to access the Amazon S3 object, you must grant it permission to call &lt;code&gt;s3:GetObject&lt;/code&gt; on the Amazon S3 bucket returned by the command. To enable the IAM role to access the KMS key, you must grant it permission to call &lt;code&gt;kms:Decrypt&lt;/code&gt; on the KMS key returned by the command. For more information, see &lt;a href="https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-refapp.html#add-policy"&gt; Grant the role permission to access the certificate and encryption key&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Nitro Enclaves User Guide&lt;/i&gt;.&lt;/p&gt; |
| `enclave_certificate_iam_role_Disassociate` | `EXEC` |  | Disassociates an IAM role from an Certificate Manager (ACM) certificate. Disassociating an IAM role from an ACM certificate removes the Amazon S3 object that contains the certificate, certificate chain, and encrypted private key from the Amazon S3 bucket. It also revokes the IAM role's permission to use the KMS key used to encrypt the private key. This effectively revokes the role's permission to use the certificate. |
