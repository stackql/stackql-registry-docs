---
title: instance_uefi_data
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_uefi_data
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
<tr><td><b>Name</b></td><td><code>instance_uefi_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.instance_uefi_data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance from which to retrieve the UEFI data. |
| <CopyableCode code="uefiData" /> | `string` | Base64 representation of the non-volatile UEFI variable store. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="instance_uefi_data_Get" /> | `SELECT` | <CopyableCode code="InstanceId, region" /> |
