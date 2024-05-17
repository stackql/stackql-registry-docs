---
title: console_output
hide_title: false
hide_table_of_contents: false
keywords:
  - console_output
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
<tr><td><b>Name</b></td><td><code>console_output</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.console_output" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="instanceId" /> | `string` | The ID of the instance. |
| <CopyableCode code="output" /> | `string` | The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you. |
| <CopyableCode code="timestamp" /> | `string` | The time at which the output was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="console_output_Get" /> | `SELECT` | <CopyableCode code="InstanceId, region" /> |
