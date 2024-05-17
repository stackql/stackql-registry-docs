---
title: password_data
hide_title: false
hide_table_of_contents: false
keywords:
  - password_data
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
<tr><td><b>Name</b></td><td><code>password_data</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.password_data" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instanceId" /> | `string` | The ID of the Windows instance. |
| <CopyableCode code="passwordData" /> | `string` | The password of the instance. Returns an empty string if the password is not available. |
| <CopyableCode code="timestamp" /> | `string` | The time the data was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="password_data_Get" /> | `SELECT` | <CopyableCode code="InstanceId, region" /> |
