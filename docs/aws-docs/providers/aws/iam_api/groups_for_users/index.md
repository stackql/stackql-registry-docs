---
title: groups_for_users
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_for_users
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups_for_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.groups_for_users</code></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `groups_for_users_List` | `SELECT` | `UserName, region` |
