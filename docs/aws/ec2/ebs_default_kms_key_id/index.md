---
title: ebs_default_kms_key_id
hide_title: false
hide_table_of_contents: false
keywords:
  - ebs_default_kms_key_id
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
<tr><td><b>Name</b></td><td><code>ebs_default_kms_key_id</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ebs_default_kms_key_id</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ebs_default_kms_key_id_Get` | `SELECT` |  | &lt;p&gt;Describes the default KMS key for EBS encryption by default for your account in this Region. You can change the default KMS key for encryption by default using &lt;a&gt;ModifyEbsDefaultKmsKeyId&lt;/a&gt; or &lt;a&gt;ResetEbsDefaultKmsKeyId&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ebs_default_kms_key_id_Modify` | `EXEC` | `KmsKeyId` | &lt;p&gt;Changes the default KMS key for EBS encryption by default for your account in this Region.&lt;/p&gt; &lt;p&gt;Amazon Web Services creates a unique Amazon Web Services managed KMS key in each Region for use with encryption by default. If you change the default KMS key to a symmetric customer managed KMS key, it is used instead of the Amazon Web Services managed KMS key. To reset the default KMS key to the Amazon Web Services managed KMS key for EBS, use &lt;a&gt;ResetEbsDefaultKmsKeyId&lt;/a&gt;. Amazon EBS does not support asymmetric KMS keys.&lt;/p&gt; &lt;p&gt;If you delete or disable the customer managed KMS key that you specified for use with encryption by default, your instances will fail to launch.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ebs_default_kms_key_id_Reset` | `EXEC` |  | &lt;p&gt;Resets the default KMS key for EBS encryption for your account in this Region to the Amazon Web Services managed KMS key for EBS.&lt;/p&gt; &lt;p&gt;After resetting the default KMS key to the Amazon Web Services managed KMS key, you can continue to encrypt by a customer managed KMS key by specifying it when you create the volume. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
