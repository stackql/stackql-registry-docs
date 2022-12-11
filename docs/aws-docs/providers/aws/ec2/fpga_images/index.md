---
title: fpga_images
hide_title: false
hide_table_of_contents: false
keywords:
  - fpga_images
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
<tr><td><b>Name</b></td><td><code>fpga_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.fpga_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the AFI. |
| `description` | `string` | The description of the AFI. |
| `ownerAlias` | `string` | The alias of the AFI owner. Possible values include &lt;code&gt;self&lt;/code&gt;, &lt;code&gt;amazon&lt;/code&gt;, and &lt;code&gt;aws-marketplace&lt;/code&gt;. |
| `pciId` | `object` | Describes the data that identifies an Amazon FPGA image (AFI) on the PCI bus. |
| `updateTime` | `string` | The time of the most recent update to the AFI. |
| `ownerId` | `string` | The ID of the Amazon Web Services account that owns the AFI. |
| `public` | `boolean` | Indicates whether the AFI is public. |
| `tags` | `array` | Any tags assigned to the AFI. |
| `state` | `object` | Describes the state of the bitstream generation process for an Amazon FPGA image (AFI). |
| `dataRetentionSupport` | `boolean` | Indicates whether data retention support is enabled for the AFI. |
| `shellVersion` | `string` | The version of the Amazon Web Services Shell that was used to create the bitstream. |
| `createTime` | `string` | The date and time the AFI was created. |
| `fpgaImageId` | `string` | The FPGA image identifier (AFI ID). |
| `productCodes` | `array` | The product codes for the AFI. |
| `fpgaImageGlobalId` | `string` | The global FPGA image identifier (AGFI ID). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `fpga_images_Describe` | `SELECT` |  | Describes the Amazon FPGA Images (AFIs) available to you. These include public AFIs, private AFIs that you own, and AFIs owned by other Amazon Web Services accounts for which you have load permissions. |
| `fpga_image_Create` | `INSERT` | `InputStorageLocation` | &lt;p&gt;Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).&lt;/p&gt; &lt;p&gt;The create operation is asynchronous. To verify that the AFI is ready for use, check the output logs.&lt;/p&gt; &lt;p&gt;An AFI contains the FPGA bitstream that is ready to download to an FPGA. You can securely deploy an AFI on multiple FPGA-accelerated instances. For more information, see the &lt;a href="https://github.com/aws/aws-fpga/"&gt;Amazon Web Services FPGA Hardware Development Kit&lt;/a&gt;.&lt;/p&gt; |
| `fpga_image_Delete` | `DELETE` | `FpgaImageId` | Deletes the specified Amazon FPGA Image (AFI). |
| `fpga_image_Copy` | `EXEC` | `SourceFpgaImageId, SourceRegion` | Copies the specified Amazon FPGA Image (AFI) to the current Region. |
