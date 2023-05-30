---
title: policy_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_versions
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
<tr><td><b>Name</b></td><td><code>policy_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.policy_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `policy_versions_Get` | `SELECT` | `PolicyArn, VersionId, region` | &lt;p&gt;Retrieves information about the specified version of the specified managed policy, including the policy document.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Policies returned by this operation are URL-encoded compliant with &lt;a href="https://tools.ietf.org/html/rfc3986"&gt;RFC 3986&lt;/a&gt;. You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the &lt;code&gt;decode&lt;/code&gt; method of the &lt;code&gt;java.net.URLDecoder&lt;/code&gt; utility class in the Java SDK. Other languages and SDKs provide similar functionality.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To list the available versions for a policy, use &lt;a&gt;ListPolicyVersions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This operation retrieves information about managed policies. To retrieve information about an inline policy that is embedded in a user, group, or role, use &lt;a&gt;GetUserPolicy&lt;/a&gt;, &lt;a&gt;GetGroupPolicy&lt;/a&gt;, or &lt;a&gt;GetRolePolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about the types of policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about managed policy versions, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html"&gt;Versioning for managed policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `policy_versions_List` | `SELECT` | `PolicyArn, region` | &lt;p&gt;Lists information about the versions of the specified managed policy, including the version that is currently set as the policy's default version.&lt;/p&gt; &lt;p&gt;For more information about managed policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `policy_versions_Create` | `INSERT` | `PolicyArn, PolicyDocument, region` | &lt;p&gt;Creates a new version of the specified managed policy. To update a managed policy, you create a new policy version. A managed policy can have up to five versions. If the policy has five versions, you must delete an existing version using &lt;a&gt;DeletePolicyVersion&lt;/a&gt; before you create a new version.&lt;/p&gt; &lt;p&gt;Optionally, you can set the new version as the policy's default version. The default version is the version that is in effect for the IAM users, groups, and roles to which the policy is attached.&lt;/p&gt; &lt;p&gt;For more information about managed policy versions, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html"&gt;Versioning for managed policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `policy_versions_Delete` | `DELETE` | `PolicyArn, VersionId, region` | &lt;p&gt;Deletes the specified version from the specified managed policy.&lt;/p&gt; &lt;p&gt;You cannot delete the default version from a policy using this operation. To delete the default version from a policy, use &lt;a&gt;DeletePolicy&lt;/a&gt;. To find out which version of a policy is marked as the default version, use &lt;a&gt;ListPolicyVersions&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For information about versions for managed policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html"&gt;Versioning for managed policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
