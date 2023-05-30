---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Arn` | `string` | &lt;p&gt;The Amazon Resource Name (ARN). ARNs are unique identifiers for Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;For more information about ARNs, go to &lt;a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. &lt;/p&gt; |
| `CreateDate` | `string` | The date and time, in &lt;a href="http://www.iso.org/iso/iso8601"&gt;ISO 8601 date-time format&lt;/a&gt;, when the group was created. |
| `GroupId` | `string` |  The stable and unique string identifying the group. For more information about IDs, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
| `GroupName` | `string` | The friendly name that identifies the group. |
| `Path` | `string` | The path to the group. For more information about paths, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `groups_Get` | `SELECT` | `GroupName, region` |  Returns a list of IAM users that are in the specified IAM group. You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters. |
| `groups_List` | `SELECT` | `region` | &lt;p&gt;Lists the IAM groups that have the specified path prefix.&lt;/p&gt; &lt;p&gt; You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `groups_Create` | `INSERT` | `GroupName, region` | &lt;p&gt;Creates a new group.&lt;/p&gt; &lt;p&gt; For information about the number of groups you can create, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM and STS quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `groups_Delete` | `DELETE` | `GroupName, region` | Deletes the specified IAM group. The group must not contain any users or have any attached policies. |
| `groups_Update` | `EXEC` | `GroupName, region` | &lt;p&gt;Updates the name and/or the path of the specified IAM group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; You should understand the implications of changing a group's path or name. For more information, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html"&gt;Renaming users and groups&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;note&gt; &lt;p&gt;The person making the request (the principal), must have permission to change the role group with the old name and the new name. For example, to change the group named &lt;code&gt;Managers&lt;/code&gt; to &lt;code&gt;MGRs&lt;/code&gt;, the principal must have a policy that allows them to update both groups. If the principal has permission to update the &lt;code&gt;Managers&lt;/code&gt; group, but not the &lt;code&gt;MGRs&lt;/code&gt; group, then the update fails. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html"&gt;Access management&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; |
