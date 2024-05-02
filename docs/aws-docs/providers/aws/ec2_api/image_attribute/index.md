---
title: image_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - image_attribute
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>image_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.image_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `object` | Describes a value for a resource attribute that is a String. |
| `blockDeviceMapping` | `array` | The block device mapping entries. |
| `bootMode` | `object` | Describes a value for a resource attribute that is a String. |
| `imageId` | `string` | The ID of the AMI. |
| `kernel` | `object` | Describes a value for a resource attribute that is a String. |
| `lastLaunchedTime` | `object` | Describes a value for a resource attribute that is a String. |
| `launchPermission` | `array` | The launch permissions. |
| `productCodes` | `array` | The product codes. |
| `ramdisk` | `object` | Describes a value for a resource attribute that is a String. |
| `sriovNetSupport` | `object` | Describes a value for a resource attribute that is a String. |
| `tpmSupport` | `object` | Describes a value for a resource attribute that is a String. |
| `uefiData` | `object` | Describes a value for a resource attribute that is a String. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `image_attribute_Describe` | `SELECT` | `Attribute, ImageId, region` | Describes the specified attribute of the specified AMI. You can specify only one attribute at a time. |
| `image_attribute_Modify` | `EXEC` | `ImageId, region` | &lt;p&gt;Modifies the specified attribute of the specified AMI. You can specify only one attribute at a time. You can use the &lt;code&gt;Attribute&lt;/code&gt; parameter to specify the attribute or one of the following parameters: &lt;code&gt;Description&lt;/code&gt; or &lt;code&gt;LaunchPermission&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;Images with an Amazon Web Services Marketplace product code cannot be made public.&lt;/p&gt; &lt;p&gt;To enable the SriovNetSupport enhanced networking attribute of an image, enable SriovNetSupport on an instance and create an AMI from the instance.&lt;/p&gt; |
| `image_attribute_Reset` | `EXEC` | `Attribute, ImageId, region` | Resets an attribute of an AMI to its default value. |
