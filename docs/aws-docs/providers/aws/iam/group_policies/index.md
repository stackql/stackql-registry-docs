---
title: group_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - group_policies
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
<tr><td><b>Name</b></td><td><code>group_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.group_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `PolicyDocument` | `string` | &lt;p&gt;The policy document.&lt;/p&gt; &lt;p&gt;IAM stores policies in JSON format. However, resources that were created using CloudFormation templates can be formatted in YAML. CloudFormation always converts a YAML policy to JSON format before submitting it to IAM.&lt;/p&gt; |
| `PolicyName` | `string` | The name of the policy. |
| `GroupName` | `string` | The group the policy is associated with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `group_policies_Get` | `SELECT` | `GroupName, PolicyName` | &lt;p&gt;Retrieves the specified inline policy document that is embedded in the specified IAM group.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Policies returned by this operation are URL-encoded compliant with &lt;a href="https://tools.ietf.org/html/rfc3986"&gt;RFC 3986&lt;/a&gt;. You can use a URL decoding method to convert the policy back to plain JSON text. For example, if you use Java, you can use the &lt;code&gt;decode&lt;/code&gt; method of the &lt;code&gt;java.net.URLDecoder&lt;/code&gt; utility class in the Java SDK. Other languages and SDKs provide similar functionality.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;An IAM group can also have managed policies attached to it. To retrieve a managed policy document that is attached to a group, use &lt;a&gt;GetPolicy&lt;/a&gt; to determine the policy's default version, then use &lt;a&gt;GetPolicyVersion&lt;/a&gt; to retrieve the policy document.&lt;/p&gt; &lt;p&gt;For more information about policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `group_policies_List` | `SELECT` | `GroupName` | &lt;p&gt;Lists the names of the inline policies that are embedded in the specified IAM group.&lt;/p&gt; &lt;p&gt;An IAM group can also have managed policies attached to it. To list the managed policies that are attached to a group, use &lt;a&gt;ListAttachedGroupPolicies&lt;/a&gt;. For more information about policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters. If there are no inline policies embedded with the specified group, the operation returns an empty list.&lt;/p&gt; |
| `group_policies_Delete` | `DELETE` | `GroupName, PolicyName` | &lt;p&gt;Deletes the specified inline policy that is embedded in the specified IAM group.&lt;/p&gt; &lt;p&gt;A group can also have managed policies attached to it. To detach a managed policy from a group, use &lt;a&gt;DetachGroupPolicy&lt;/a&gt;. For more information about policies, refer to &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `group_policies_Attach` | `EXEC` | `GroupName, PolicyArn` | &lt;p&gt;Attaches the specified managed policy to the specified IAM group.&lt;/p&gt; &lt;p&gt;You use this operation to attach a managed policy to a group. To embed an inline policy in a group, use &lt;a&gt;PutGroupPolicy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;As a best practice, you can validate your IAM policies. To learn more, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_policy-validator.html"&gt;Validating IAM policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `group_policies_Detach` | `EXEC` | `GroupName, PolicyArn` | &lt;p&gt;Removes the specified managed policy from the specified IAM group.&lt;/p&gt; &lt;p&gt;A group can also have inline policies embedded with it. To delete an inline policy, use &lt;a&gt;DeleteGroupPolicy&lt;/a&gt;. For information about policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `group_policies_Put` | `EXEC` | `GroupName, PolicyDocument, PolicyName` | &lt;p&gt;Adds or updates an inline policy document that is embedded in the specified IAM group.&lt;/p&gt; &lt;p&gt;A user can also have managed policies attached to it. To attach a managed policy to a group, use &lt;a&gt;AttachGroupPolicy&lt;/a&gt;. To create a new managed policy, use &lt;a&gt;CreatePolicy&lt;/a&gt;. For information about policies, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html"&gt;Managed policies and inline policies&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For information about the maximum number of inline policies that you can embed in a group, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM and STS quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Because policy documents can be large, you should use POST rather than GET when calling &lt;code&gt;PutGroupPolicy&lt;/code&gt;. For general information about using the Query API with IAM, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html"&gt;Making query requests&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; |
