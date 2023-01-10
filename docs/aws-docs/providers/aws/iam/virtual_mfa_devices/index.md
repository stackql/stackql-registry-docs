---
title: virtual_mfa_devices
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_mfa_devices
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
<tr><td><b>Name</b></td><td><code>virtual_mfa_devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.virtual_mfa_devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Base32StringSeed` | `string` |  The base32 seed defined as specified in &lt;a href="https://tools.ietf.org/html/rfc3548.txt"&gt;RFC3548&lt;/a&gt;. The &lt;code&gt;Base32StringSeed&lt;/code&gt; is base64-encoded.  |
| `EnableDate` | `string` | The date and time on which the virtual MFA device was enabled. |
| `QRCodePNG` | `string` |  A QR code PNG image that encodes &lt;code&gt;otpauth://totp/$virtualMFADeviceName@$AccountName?secret=$Base32String&lt;/code&gt; where &lt;code&gt;$virtualMFADeviceName&lt;/code&gt; is one of the create call arguments. &lt;code&gt;AccountName&lt;/code&gt; is the user name if set (otherwise, the account ID otherwise), and &lt;code&gt;Base32String&lt;/code&gt; is the seed in base32 format. The &lt;code&gt;Base32String&lt;/code&gt; value is base64-encoded.  |
| `SerialNumber` | `string` | The serial number associated with &lt;code&gt;VirtualMFADevice&lt;/code&gt;. |
| `Tags` | `array` | A list of tags that are attached to the virtual MFA device. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `User` | `object` | &lt;p&gt;Contains information about an IAM user entity.&lt;/p&gt; &lt;p&gt;This data type is used as a response element in the following operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;CreateUser&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetUser&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;ListUsers&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `virtual_mfa_devices_List` | `SELECT` |  | &lt;p&gt;Lists the virtual MFA devices defined in the Amazon Web Services account by assignment status. If you do not specify an assignment status, the operation returns a list of all virtual MFA devices. Assignment status can be &lt;code&gt;Assigned&lt;/code&gt;, &lt;code&gt;Unassigned&lt;/code&gt;, or &lt;code&gt;Any&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view tag information for a virtual MFA device, see &lt;a&gt;ListMFADeviceTags&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;You can paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; |
| `virtual_mfa_devices_Create` | `INSERT` | `VirtualMFADeviceName` | &lt;p&gt;Creates a new virtual MFA device for the Amazon Web Services account. After creating the virtual MFA, use &lt;a&gt;EnableMFADevice&lt;/a&gt; to attach the MFA device to an IAM user. For more information about creating and working with virtual MFA devices, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html"&gt;Using a virtual MFA device&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For information about the maximum number of MFA devices you can create, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html"&gt;IAM and STS quotas&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The seed information contained in the QR code and the Base32 string should be treated like any other secret access information. In other words, protect the seed information as you would your Amazon Web Services access keys or your passwords. After you provision your virtual device, you should ensure that the information is destroyed following secure procedures.&lt;/p&gt; &lt;/important&gt; |
| `virtual_mfa_devices_Delete` | `DELETE` | `SerialNumber` | &lt;p&gt;Deletes a virtual MFA device.&lt;/p&gt; &lt;note&gt; &lt;p&gt; You must deactivate a user's virtual MFA device before you can delete it. For information about deactivating MFA devices, see &lt;a&gt;DeactivateMFADevice&lt;/a&gt;. &lt;/p&gt; &lt;/note&gt; |
