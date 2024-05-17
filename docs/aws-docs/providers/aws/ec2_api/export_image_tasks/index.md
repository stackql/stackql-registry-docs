---
title: export_image_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - export_image_tasks
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
<tr><td><b>Name</b></td><td><code>export_image_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.export_image_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description of the image being exported. |
| <CopyableCode code="exportImageTaskId" /> | `string` | The ID of the export image task. |
| <CopyableCode code="imageId" /> | `string` | The ID of the image. |
| <CopyableCode code="progress" /> | `string` | The percent complete of the export image task. |
| <CopyableCode code="s3ExportLocation" /> | `object` | Describes the destination for an export image task. |
| <CopyableCode code="status" /> | `string` | The status of the export image task. The possible values are &lt;code&gt;active&lt;/code&gt;, &lt;code&gt;completed&lt;/code&gt;, &lt;code&gt;deleting&lt;/code&gt;, and &lt;code&gt;deleted&lt;/code&gt;. |
| <CopyableCode code="statusMessage" /> | `string` | The status message for the export image task. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the export image task. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="export_image_tasks_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
