---
title: vpn_connection_device_types
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connection_device_types
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
<tr><td><b>Name</b></td><td><code>vpn_connection_device_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpn_connection_device_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="platform" /> | `string` | Customer gateway device platform. |
| <CopyableCode code="software" /> | `string` | Customer gateway device software version. |
| <CopyableCode code="vendor" /> | `string` | Customer gateway device vendor. |
| <CopyableCode code="vpnConnectionDeviceTypeId" /> | `string` | Customer gateway device identifier. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="vpn_connection_device_types_Get" /> | `SELECT` | <CopyableCode code="region" /> |
