---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - transfer_api
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer_api.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="Arn" /> | `string` |  |
| <CopyableCode code="HomeDirectory" /> | `string` |  |
| <CopyableCode code="HomeDirectoryMappings" /> | `array` |  |
| <CopyableCode code="HomeDirectoryType" /> | `string` |  |
| <CopyableCode code="Policy" /> | `string` |  |
| <CopyableCode code="PosixProfile" /> | `object` | The full POSIX identity, including user ID (&lt;code&gt;Uid&lt;/code&gt;), group ID (&lt;code&gt;Gid&lt;/code&gt;), and any secondary groups IDs (&lt;code&gt;SecondaryGids&lt;/code&gt;), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems. |
| <CopyableCode code="Role" /> | `string` |  |
| <CopyableCode code="SshPublicKeys" /> | `array` |  |
| <CopyableCode code="Tags" /> | `array` |  |
| <CopyableCode code="UserName" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="describe_user" /> | `SELECT` | <CopyableCode code="data__ServerId, data__UserName, region" /> | &lt;p&gt;Describes the user assigned to the specific file transfer protocol-enabled server, as identified by its &lt;code&gt;ServerId&lt;/code&gt; property.&lt;/p&gt; &lt;p&gt;The response from this call returns the properties of the user associated with the &lt;code&gt;ServerId&lt;/code&gt; value that was specified.&lt;/p&gt; |
| <CopyableCode code="list_users" /> | `SELECT` | <CopyableCode code="data__ServerId, region" /> | Lists the users for a file transfer protocol-enabled server that you specify by passing the &lt;code&gt;ServerId&lt;/code&gt; parameter. |
| <CopyableCode code="create_user" /> | `INSERT` | <CopyableCode code="data__Role, data__ServerId, data__UserName, region" /> | Creates a user and associates them with an existing file transfer protocol-enabled server. You can only create and associate users with servers that have the &lt;code&gt;IdentityProviderType&lt;/code&gt; set to &lt;code&gt;SERVICE_MANAGED&lt;/code&gt;. Using parameters for &lt;code&gt;CreateUser&lt;/code&gt;, you can specify the user name, set the home directory, store the user's public key, and assign the user's Identity and Access Management (IAM) role. You can also optionally add a session policy, and assign metadata with tags that can be used to group and search for users. |
| <CopyableCode code="delete_user" /> | `DELETE` | <CopyableCode code="data__ServerId, data__UserName, region" /> | &lt;p&gt;Deletes the user belonging to a file transfer protocol-enabled server you specify.&lt;/p&gt; &lt;p&gt;No response returns from this operation.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you delete a user from a server, the user's information is lost.&lt;/p&gt; &lt;/note&gt; |
| <CopyableCode code="update_user" /> | `UPDATE` | <CopyableCode code="data__ServerId, data__UserName, region" /> | &lt;p&gt;Assigns new properties to a user. Parameters you pass modify any or all of the following: the home directory, role, and policy for the &lt;code&gt;UserName&lt;/code&gt; and &lt;code&gt;ServerId&lt;/code&gt; you specify.&lt;/p&gt; &lt;p&gt;The response returns the &lt;code&gt;ServerId&lt;/code&gt; and the &lt;code&gt;UserName&lt;/code&gt; for the updated user.&lt;/p&gt; |
