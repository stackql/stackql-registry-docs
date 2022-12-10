---
title: volume_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_attribute
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.volume_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `autoEnableIO` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `productCodes` | `array` | A list of product codes. |
| `volumeId` | `string` | The ID of the volume. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `volume_attribute_Describe` | `SELECT` | `Attribute, VolumeId` | &lt;p&gt;Describes the specified attribute of the specified volume. You can specify only one attribute at a time.&lt;/p&gt; &lt;p&gt;For more information about EBS volumes, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumes.html"&gt;Amazon EBS volumes&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Compute Cloud User Guide&lt;/i&gt;.&lt;/p&gt; |
| `volume_attribute_Modify` | `EXEC` | `VolumeId` | &lt;p&gt;Modifies a volume attribute.&lt;/p&gt; &lt;p&gt;By default, all I/O operations for the volume are suspended when the data on the volume is determined to be potentially inconsistent, to prevent undetectable, latent data corruption. The I/O access to the volume can be resumed by first enabling I/O access and then checking the data consistency on your volume.&lt;/p&gt; &lt;p&gt;You can change the default behavior to resume I/O operations. We recommend that you change this only for boot volumes or for volumes that are stateless or disposable.&lt;/p&gt; |
