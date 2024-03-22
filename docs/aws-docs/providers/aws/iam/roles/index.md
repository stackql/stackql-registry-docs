---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Arn` | `string` | &lt;p&gt;The Amazon Resource Name (ARN). ARNs are unique identifiers for Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;For more information about ARNs, go to &lt;a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. &lt;/p&gt; |
| `AssumeRolePolicyDocument` | `string` | The policy that grants an entity permission to assume the role. |
| `CreateDate` | `string` | The date and time, in &lt;a href="http://www.iso.org/iso/iso8601"&gt;ISO 8601 date-time format&lt;/a&gt;, when the role was created. |
| `Description` | `string` | A description of the role that you provide. |
| `MaxSessionDuration` | `integer` | The maximum session duration (in seconds) for the specified role. Anyone who uses the CLI, or API to assume the role can specify the duration using the optional &lt;code&gt;DurationSeconds&lt;/code&gt; API parameter or &lt;code&gt;duration-seconds&lt;/code&gt; CLI parameter. |
| `Path` | `string` |  The path to the role. For more information about paths, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
| `PermissionsBoundary` | `object` | &lt;p&gt;Contains information about an attached permissions boundary.&lt;/p&gt; &lt;p&gt;An attached permissions boundary is a managed policy that has been attached to a user or role to set the permissions boundary.&lt;/p&gt; &lt;p&gt;For more information about permissions boundaries, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html"&gt;Permissions boundaries for IAM identities &lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `RoleId` | `string` |  The stable and unique string identifying the role. For more information about IDs, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.  |
| `RoleLastUsed` | `object` | &lt;p&gt;Contains information about the last time that an IAM role was used. This includes the date and time and the Region in which the role was last used. Activity is only reported for the trailing 400 days. This period can be shorter if your Region began supporting these features within the last year. The role might have been used more than 400 days ago. For more information, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html#access-advisor_tracking-period"&gt;Regions where data is tracked&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;This data type is returned as a response element in the &lt;a&gt;GetRole&lt;/a&gt; and &lt;a&gt;GetAccountAuthorizationDetails&lt;/a&gt; operations.&lt;/p&gt; |
| `RoleName` | `string` | The friendly name that identifies the role. |
| `Tags` | `array` | A list of tags that are attached to the role. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `roles_Get` | `SELECT` | `RoleName, region` | &lt;p&gt;Retrieves information about the specified role, including the role's path, GUID, ARN, and the role's trust policy that grants permission to assume the role. For more information about roles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html"&gt;Working with roles&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Policies returned by this operation are URL-encoded compliant with &lt;a href="https://tools.ietf.org/html/rfc3986"&gt;RFC 3986&lt;/a&gt;. You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the &lt;code&gt;decode&lt;/code&gt; method of the &lt;code&gt;java.net.URLDecoder&lt;/code&gt; utility class in the Java SDK. Other languages and SDKs provide similar functionality.&lt;/p&gt; &lt;/note&gt; |
| `roles_List` | `SELECT` | `region` | &lt;p&gt;Lists the IAM roles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about roles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html"&gt;Working with roles&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a role, see &lt;a&gt;GetRole&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `roles_Create` | `INSERT` | `AssumeRolePolicyDocument, RoleName, region` | Creates a new role for your Amazon Web Services account. For more information about roles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html"&gt;IAM roles&lt;/a&gt;. For information about quotas for role names and the number of roles you can create, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM and STS quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `roles_Delete` | `DELETE` | `RoleName, region` | &lt;p&gt;Deletes the specified role. The role must not have any policies attached. For more information about roles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html"&gt;Working with roles&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Make sure that you do not have any Amazon EC2 instances running with the role you are about to delete. Deleting a role or instance profile that is associated with a running instance will break any applications running on the instance.&lt;/p&gt; &lt;/important&gt; |
| `roles_Tag` | `EXEC` | `RoleName, Tags, region` | &lt;p&gt;Adds one or more tags to an IAM role. The role can be a regular role or a service-linked role. If a tag with the same key name already exists, then that tag is overwritten with the new value.&lt;/p&gt; &lt;p&gt;A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Administrative grouping and discovery&lt;/b&gt; - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name &lt;i&gt;Project&lt;/i&gt; and the value &lt;i&gt;MyImportantProject&lt;/i&gt;. Or search for all resources with the key name &lt;i&gt;Cost Center&lt;/i&gt; and the value &lt;i&gt;41200&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Access control&lt;/b&gt; - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM role that has a specified tag attached. You can also restrict access to only those resources that have a certain tag attached. For examples of policies that show how to use tags to control access, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html"&gt;Control access using IAM tags&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Cost allocation&lt;/b&gt; - Use tags to help track which individuals and teams are using which Amazon Web Services resources.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM identities&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `roles_Untag` | `EXEC` | `RoleName, TagKeys, region` | Removes the specified tags from the role. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `roles_Update` | `EXEC` | `RoleName, region` | Updates the description or maximum session duration setting of a role. |
