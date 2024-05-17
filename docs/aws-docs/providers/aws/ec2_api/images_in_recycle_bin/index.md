---
title: images_in_recycle_bin
hide_title: false
hide_table_of_contents: false
keywords:
  - images_in_recycle_bin
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
<tr><td><b>Name</b></td><td><code>images_in_recycle_bin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.images_in_recycle_bin" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the AMI. |
| <CopyableCode code="description" /> | `string` | The description of the AMI. |
| <CopyableCode code="imageId" /> | `string` | The ID of the AMI. |
| <CopyableCode code="recycleBinEnterTime" /> | `string` | The date and time when the AMI entered the Recycle Bin. |
| <CopyableCode code="recycleBinExitTime" /> | `string` | The date and time when the AMI is to be permanently deleted from the Recycle Bin. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="images_in_recycle_bin_List" /> | `SELECT` | <CopyableCode code="region" /> |
