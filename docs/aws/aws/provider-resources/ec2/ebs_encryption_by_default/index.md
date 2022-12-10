---
title: ebs_encryption_by_default
hide_title: false
hide_table_of_contents: false
keywords:
  - ebs_encryption_by_default
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
<tr><td><b>Name</b></td><td><code>ebs_encryption_by_default</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.ebs_encryption_by_default</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ebs_encryption_by_default_Get` | `SELECT` |  | &lt;p&gt;Describes whether EBS encryption by default is enabled for your account in the current Region.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ebs_encryption_by_default_Disable` | `EXEC` |  | &lt;p&gt;Disables EBS encryption by default for your account in the current Region.&lt;/p&gt; &lt;p&gt;After you disable encryption by default, you can still create encrypted volumes by enabling encryption when you create each volume.&lt;/p&gt; &lt;p&gt;Disabling encryption by default does not change the encryption status of your existing volumes.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ebs_encryption_by_default_Enable` | `EXEC` |  | &lt;p&gt;Enables EBS encryption by default for your account in the current Region.&lt;/p&gt; &lt;p&gt;After you enable encryption by default, the EBS volumes that you create are always encrypted, either using the default KMS key or the KMS key that you specified when you created each volume. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html"&gt;Amazon EBS encryption&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can specify the default KMS key for encryption by default using &lt;a&gt;ModifyEbsDefaultKmsKeyId&lt;/a&gt; or &lt;a&gt;ResetEbsDefaultKmsKeyId&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Enabling encryption by default has no effect on the encryption status of your existing volumes.&lt;/p&gt; &lt;p&gt;After you enable encryption by default, you can no longer launch instances using instance types that do not support encryption. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#EBSEncryption_supported_instances"&gt;Supported instance types&lt;/a&gt;.&lt;/p&gt; |
