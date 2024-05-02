---
title: mfa_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - mfa_devices
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
<tr><td><b>Name</b></td><td><code>mfa_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.mfa_devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `EnableDate` | `string` | The date when the MFA device was enabled for the user. |
| `SerialNumber` | `string` | The serial number that uniquely identifies the MFA device. For virtual MFA devices, the serial number is the device ARN. |
| `UserName` | `string` | The user with whom the MFA device is associated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `mfa_devices_List` | `SELECT` | `region` | &lt;p&gt;Lists the MFA devices for an IAM user. If the request includes a IAM user name, then this operation lists all the MFA devices associated with the specified user. If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request for this operation.&lt;/p&gt; &lt;p&gt;You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `mfa_devices_Deactivate` | `EXEC` | `SerialNumber, UserName, region` | &lt;p&gt;Deactivates the specified MFA device and removes it from association with the user name for which it was originally enabled.&lt;/p&gt; &lt;p&gt;For more information about creating and working with virtual MFA devices, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html"&gt;Enabling a virtual multi-factor authentication (MFA) device&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `mfa_devices_Enable` | `EXEC` | `AuthenticationCode1, AuthenticationCode2, SerialNumber, UserName, region` | Enables the specified MFA device and associates it with the specified IAM user. When enabled, the MFA device is required for every subsequent login by the IAM user associated with the device. |
| `mfa_devices_Resync` | `EXEC` | `AuthenticationCode1, AuthenticationCode2, SerialNumber, UserName, region` | &lt;p&gt;Synchronizes the specified MFA device with its IAM resource object on the Amazon Web Services servers.&lt;/p&gt; &lt;p&gt;For more information about creating and working with virtual MFA devices, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html"&gt;Using a virtual MFA device&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `mfa_devices_Tag` | `EXEC` | `SerialNumber, Tags, region` | &lt;p&gt;Adds one or more tags to an IAM virtual multi-factor authentication (MFA) device. If a tag with the same key name already exists, then that tag is overwritten with the new value.&lt;/p&gt; &lt;p&gt;A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Administrative grouping and discovery&lt;/b&gt; - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name &lt;i&gt;Project&lt;/i&gt; and the value &lt;i&gt;MyImportantProject&lt;/i&gt;. Or search for all resources with the key name &lt;i&gt;Cost Center&lt;/i&gt; and the value &lt;i&gt;41200&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Access control&lt;/b&gt; - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an IAM virtual MFA device that has a specified tag attached. For examples of policies that show how to use tags to control access, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html"&gt;Control access using IAM tags&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; |
| `mfa_devices_Untag` | `EXEC` | `SerialNumber, TagKeys, region` | Removes the specified tags from the IAM virtual multi-factor authentication (MFA) device. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
