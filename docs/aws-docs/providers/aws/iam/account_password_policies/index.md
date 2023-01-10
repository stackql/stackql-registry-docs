---
title: account_password_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - account_password_policies
  - iam
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_password_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.account_password_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `account_password_policies_Get` | `SELECT` |  | Retrieves the password policy for the Amazon Web Services account. This tells you the complexity requirements and mandatory rotation periods for the IAM user passwords in your account. For more information about using a password policy, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html"&gt;Managing an IAM password policy&lt;/a&gt;. |
| `account_password_policies_Delete` | `DELETE` |  | Deletes the password policy for the Amazon Web Services account. There are no parameters. |
| `account_password_policies_Update` | `EXEC` |  | &lt;p&gt;Updates the password policy settings for the Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation does not support partial updates. No parameters are required, but if you do not specify a parameter, that parameter's value reverts to its default value. See the &lt;b&gt;Request Parameters&lt;/b&gt; section for each parameter's default value. Also note that some parameters do not allow the default parameter to be explicitly set. Instead, to invoke the default value, do not include that parameter when you invoke the operation.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For more information about using a password policy, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html"&gt;Managing an IAM password policy&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
