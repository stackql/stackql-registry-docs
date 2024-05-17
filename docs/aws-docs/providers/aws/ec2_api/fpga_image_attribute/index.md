---
title: fpga_image_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - fpga_image_attribute
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fpga_image_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.fpga_image_attribute" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fpga_image_attribute_Describe" /> | `SELECT` | <CopyableCode code="Attribute, FpgaImageId, region" /> | Describes the specified attribute of the specified Amazon FPGA Image (AFI). |
| <CopyableCode code="fpga_image_attribute_Modify" /> | `EXEC` | <CopyableCode code="FpgaImageId, region" /> | Modifies the specified attribute of the specified Amazon FPGA Image (AFI). |
| <CopyableCode code="fpga_image_attribute_Reset" /> | `EXEC` | <CopyableCode code="FpgaImageId, region" /> | Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its default value. You can only reset the load permission attribute. |
