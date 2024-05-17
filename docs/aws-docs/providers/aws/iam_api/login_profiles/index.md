---
title: login_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - login_profiles
  - iam_api
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>login_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.login_profiles" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="login_profiles_Get" /> | `SELECT` | <CopyableCode code="UserName, region" /> | &lt;p&gt;Retrieves the user name for the specified IAM user. A login profile is created when you create a password for the user to access the Amazon Web Services Management Console. If the user does not exist or does not have a password, the operation returns a 404 (&lt;code&gt;NoSuchEntity&lt;/code&gt;) error.&lt;/p&gt; &lt;p&gt;If you create an IAM user with access to the console, the &lt;code&gt;CreateDate&lt;/code&gt; reflects the date you created the initial password for the user.&lt;/p&gt; &lt;p&gt;If you create an IAM user with programmatic access, and then later add a password for the user to access the Amazon Web Services Management Console, the &lt;code&gt;CreateDate&lt;/code&gt; reflects the initial password creation date. A user with programmatic access does not have a login profile unless you create a password for the user to access the Amazon Web Services Management Console.&lt;/p&gt; |
| <CopyableCode code="login_profiles_Create" /> | `INSERT` | <CopyableCode code="Password, UserName, region" /> | &lt;p&gt;Creates a password for the specified IAM user. A password allows an IAM user to access Amazon Web Services services through the Amazon Web Services Management Console.&lt;/p&gt; &lt;p&gt;You can use the CLI, the Amazon Web Services API, or the &lt;b&gt;Users&lt;/b&gt; page in the IAM console to create a password for any IAM user. Use &lt;a&gt;ChangePassword&lt;/a&gt; to update your own existing password in the &lt;b&gt;My Security Credentials&lt;/b&gt; page in the Amazon Web Services Management Console.&lt;/p&gt; &lt;p&gt;For more information about managing passwords, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html"&gt;Managing passwords&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="login_profiles_Delete" /> | `DELETE` | <CopyableCode code="UserName, region" /> | &lt;p&gt;Deletes the password for the specified IAM user, which terminates the user's ability to access Amazon Web Services services through the Amazon Web Services Management Console.&lt;/p&gt; &lt;p&gt;You can use the CLI, the Amazon Web Services API, or the &lt;b&gt;Users&lt;/b&gt; page in the IAM console to delete a password for any IAM user. You can use &lt;a&gt;ChangePassword&lt;/a&gt; to update, but not delete, your own password in the &lt;b&gt;My Security Credentials&lt;/b&gt; page in the Amazon Web Services Management Console.&lt;/p&gt; &lt;important&gt; &lt;p&gt; Deleting a user's password does not prevent a user from accessing Amazon Web Services through the command line interface or the API. To prevent all user access, you must also either make any access keys inactive or delete them. For more information about making keys inactive or deleting them, see &lt;a&gt;UpdateAccessKey&lt;/a&gt; and &lt;a&gt;DeleteAccessKey&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt; |
| <CopyableCode code="login_profiles_Update" /> | `EXEC` | <CopyableCode code="UserName, region" /> | &lt;p&gt;Changes the password for the specified IAM user. You can use the CLI, the Amazon Web Services API, or the &lt;b&gt;Users&lt;/b&gt; page in the IAM console to change the password for any IAM user. Use &lt;a&gt;ChangePassword&lt;/a&gt; to change your own password in the &lt;b&gt;My Security Credentials&lt;/b&gt; page in the Amazon Web Services Management Console.&lt;/p&gt; &lt;p&gt;For more information about modifying passwords, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html"&gt;Managing passwords&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
