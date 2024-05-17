---
title: import_image_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - import_image_tasks
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
<tr><td><b>Name</b></td><td><code>import_image_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.import_image_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | A description of the import task. |
| <CopyableCode code="architecture" /> | `string` | &lt;p&gt;The architecture of the virtual machine.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;i386&lt;/code&gt; \| &lt;code&gt;x86_64&lt;/code&gt; \| &lt;code&gt;arm64&lt;/code&gt; &lt;/p&gt; |
| <CopyableCode code="bootMode" /> | `string` | The boot mode of the virtual machine. |
| <CopyableCode code="encrypted" /> | `boolean` | Indicates whether the image is encrypted. |
| <CopyableCode code="hypervisor" /> | `string` | &lt;p&gt;The target hypervisor for the import task.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;xen&lt;/code&gt; &lt;/p&gt; |
| <CopyableCode code="imageId" /> | `string` | The ID of the Amazon Machine Image (AMI) of the imported virtual machine. |
| <CopyableCode code="importTaskId" /> | `string` | The ID of the import image task. |
| <CopyableCode code="kmsKeyId" /> | `string` | The identifier for the KMS key that was used to create the encrypted image. |
| <CopyableCode code="licenseSpecifications" /> | `array` | The ARNs of the license configurations that are associated with the import image task. |
| <CopyableCode code="licenseType" /> | `string` | The license type of the virtual machine. |
| <CopyableCode code="platform" /> | `string` | The description string for the import image task. |
| <CopyableCode code="progress" /> | `string` | The percentage of progress of the import image task. |
| <CopyableCode code="snapshotDetailSet" /> | `array` | Information about the snapshots. |
| <CopyableCode code="status" /> | `string` | A brief status for the import image task. |
| <CopyableCode code="statusMessage" /> | `string` | A descriptive status message for the import image task. |
| <CopyableCode code="tagSet" /> | `array` | The tags for the import image task. |
| <CopyableCode code="usageOperation" /> | `string` | The usage operation value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="import_image_tasks_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
