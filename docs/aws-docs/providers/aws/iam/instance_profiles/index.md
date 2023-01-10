---
title: instance_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_profiles
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
<tr><td><b>Name</b></td><td><code>instance_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.instance_profiles</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_profiles_Get` | `SELECT` | `InstanceProfileName` |  Retrieves information about the specified instance profile, including the instance profile's path, GUID, ARN, and role. For more information about instance profiles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html"&gt;About instance profiles&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `instance_profiles_List` | `SELECT` |  | &lt;p&gt;Lists the instance profiles that have the specified path prefix. If there are none, the operation returns an empty list. For more information about instance profiles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html"&gt;About instance profiles&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an instance profile, see &lt;a&gt;GetInstanceProfile&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `instance_profiles_Create` | `INSERT` | `InstanceProfileName` | &lt;p&gt; Creates a new instance profile. For information about instance profiles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html"&gt;Using roles for applications on Amazon EC2&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;, and &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#ec2-instance-profile"&gt;Instance profiles&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; For information about the number of instance profiles you can create, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM object quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_profiles_Delete` | `DELETE` | `InstanceProfileName` | &lt;p&gt;Deletes the specified instance profile. The instance profile must not have an associated role.&lt;/p&gt; &lt;important&gt; &lt;p&gt;Make sure that you do not have any Amazon EC2 instances running with the instance profile you are about to delete. Deleting a role or instance profile that is associated with a running instance will break any applications running on the instance.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about instance profiles, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html"&gt;About instance profiles&lt;/a&gt;.&lt;/p&gt; |
| `instance_profiles_Tag` | `EXEC` | `InstanceProfileName, Tags` | &lt;p&gt;Adds one or more tags to an IAM instance profile. If a tag with the same key name already exists, then that tag is overwritten with the new value.&lt;/p&gt; &lt;p&gt;Each tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Administrative grouping and discovery&lt;/b&gt; - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name &lt;i&gt;Project&lt;/i&gt; and the value &lt;i&gt;MyImportantProject&lt;/i&gt;. Or search for all resources with the key name &lt;i&gt;Cost Center&lt;/i&gt; and the value &lt;i&gt;41200&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Access control&lt;/b&gt; - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM instance profile that has a specified tag attached. For examples of policies that show how to use tags to control access, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html"&gt;Control access using IAM tags&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; |
| `instance_profiles_Untag` | `EXEC` | `InstanceProfileName, TagKeys` | Removes the specified tags from the IAM instance profile. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
