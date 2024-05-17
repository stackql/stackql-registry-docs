---
title: aggregate_id_format
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregate_id_format
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
<tr><td><b>Name</b></td><td><code>aggregate_id_format</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.aggregate_id_format" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="deadline" /> | `string` | The date in UTC at which you are permanently switched over to using longer IDs. If a deadline is not yet available for this resource type, this field is not returned. |
| <CopyableCode code="resource" /> | `string` | The type of resource. |
| <CopyableCode code="useLongIds" /> | `boolean` | Indicates whether longer IDs (17-character IDs) are enabled for the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="aggregate_id_format_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
