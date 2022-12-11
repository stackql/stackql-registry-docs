---
title: fpga_image_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - fpga_image_attribute
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
<tr><td><b>Name</b></td><td><code>fpga_image_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.fpga_image_attribute</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `fpga_image_attribute_Describe` | `SELECT` | `Attribute, FpgaImageId` | Describes the specified attribute of the specified Amazon FPGA Image (AFI). |
| `fpga_image_attribute_Modify` | `EXEC` | `FpgaImageId` | Modifies the specified attribute of the specified Amazon FPGA Image (AFI). |
| `fpga_image_attribute_Reset` | `EXEC` | `FpgaImageId` | Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute. |
