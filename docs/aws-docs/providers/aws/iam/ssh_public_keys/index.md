---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
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
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.ssh_public_keys</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ssh_public_keys_Get` | `SELECT` | `Encoding, SSHPublicKeyId, UserName` | &lt;p&gt;Retrieves the specified SSH public key, including metadata about the key.&lt;/p&gt; &lt;p&gt;The SSH public key retrieved by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see &lt;a href="https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html"&gt;Set up CodeCommit for SSH connections&lt;/a&gt; in the &lt;i&gt;CodeCommit User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ssh_public_keys_List` | `SELECT` |  | &lt;p&gt;Returns information about the SSH public keys associated with the specified IAM user. If none exists, the operation returns an empty list.&lt;/p&gt; &lt;p&gt;The SSH public keys returned by this operation are used only for authenticating the IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see &lt;a href="https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html"&gt;Set up CodeCommit for SSH connections&lt;/a&gt; in the &lt;i&gt;CodeCommit User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Although each user is limited to a small number of keys, you can still paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `ssh_public_keys_Delete` | `DELETE` | `SSHPublicKeyId, UserName` | &lt;p&gt;Deletes the specified SSH public key.&lt;/p&gt; &lt;p&gt;The SSH public key deleted by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see &lt;a href="https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html"&gt;Set up CodeCommit for SSH connections&lt;/a&gt; in the &lt;i&gt;CodeCommit User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ssh_public_keys_Update` | `EXEC` | `SSHPublicKeyId, Status, UserName` | &lt;p&gt;Sets the status of an IAM user's SSH public key to active or inactive. SSH public keys that are inactive cannot be used for authentication. This operation can be used to disable a user's SSH public key as part of a key rotation work flow.&lt;/p&gt; &lt;p&gt;The SSH public key affected by this operation is used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see &lt;a href="https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html"&gt;Set up CodeCommit for SSH connections&lt;/a&gt; in the &lt;i&gt;CodeCommit User Guide&lt;/i&gt;.&lt;/p&gt; |
| `ssh_public_keys_Upload` | `EXEC` | `SSHPublicKeyBody, UserName` | &lt;p&gt;Uploads an SSH public key and associates it with the specified IAM user.&lt;/p&gt; &lt;p&gt;The SSH public key uploaded by this operation can be used only for authenticating the associated IAM user to an CodeCommit repository. For more information about using SSH keys to authenticate to an CodeCommit repository, see &lt;a href="https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-credentials-ssh.html"&gt;Set up CodeCommit for SSH connections&lt;/a&gt; in the &lt;i&gt;CodeCommit User Guide&lt;/i&gt;.&lt;/p&gt; |
