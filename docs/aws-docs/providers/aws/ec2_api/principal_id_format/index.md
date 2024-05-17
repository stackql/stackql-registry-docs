---
title: principal_id_format
hide_title: false
hide_table_of_contents: false
keywords:
  - principal_id_format
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
<tr><td><b>Name</b></td><td><code>principal_id_format</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.principal_id_format" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="arn" /> | `string` | PrincipalIdFormatARN description |
| <CopyableCode code="statusSet" /> | `array` | PrincipalIdFormatStatuses description |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="principal_id_format_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
