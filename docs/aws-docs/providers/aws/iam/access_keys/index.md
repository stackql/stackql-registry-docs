---
title: access_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - access_keys
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
<tr><td><b>Name</b></td><td><code>access_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.access_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `AccessKeyId` | `string` | The ID for this access key. |
| `CreateDate` | `string` | The date when the access key was created. |
| `Status` | `string` | The status of the access key. &lt;code&gt;Active&lt;/code&gt; means that the key is valid for API calls; &lt;code&gt;Inactive&lt;/code&gt; means it is not. |
| `UserName` | `string` | The name of the IAM user that the key is associated with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `access_keys_List` | `SELECT` | `region` | &lt;p&gt;Returns information about the access key IDs associated with the specified IAM user. If there is none, the operation returns an empty list.&lt;/p&gt; &lt;p&gt;Although each user is limited to a small number of keys, you can still paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;UserName&lt;/code&gt; field is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; &lt;note&gt; &lt;p&gt;To ensure the security of your Amazon Web Services account, the secret access key is accessible only during key and user creation.&lt;/p&gt; &lt;/note&gt; |
| `access_keys_Create` | `INSERT` | `region` | &lt;p&gt; Creates a new Amazon Web Services secret access key and corresponding Amazon Web Services access key ID for the specified user. The default status for new keys is &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials. This is true even if the Amazon Web Services account has no associated users.&lt;/p&gt; &lt;p&gt; For information about quotas on the number of keys you can create, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM and STS quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;To ensure the security of your Amazon Web Services account, the secret access key is accessible only during key and user creation. You must save the key (for example, in a text file) if you want to be able to access it again. If a secret key is lost, you can delete the access keys for the associated user and then create new keys.&lt;/p&gt; &lt;/important&gt; |
| `access_keys_Delete` | `DELETE` | `AccessKeyId, region` | &lt;p&gt;Deletes the access key pair associated with the specified IAM user.&lt;/p&gt; &lt;p&gt;If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; |
| `access_keys_Update` | `EXEC` | `AccessKeyId, Status, region` | &lt;p&gt;Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotation workflow.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;UserName&lt;/code&gt; is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; &lt;p&gt;For information about rotating keys, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html"&gt;Managing keys and certificates&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
