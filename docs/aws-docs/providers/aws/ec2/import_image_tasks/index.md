---
title: import_image_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - import_image_tasks
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>import_image_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.import_image_tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | A description of the import task. |
| `status` | `string` | A brief status for the import image task. |
| `licenseSpecifications` | `array` | The ARNs of the license configurations that are associated with the import image task. |
| `tagSet` | `array` | The tags for the import image task. |
| `progress` | `string` | The percentage of progress of the import image task. |
| `platform` | `string` | The description string for the import image task. |
| `encrypted` | `boolean` | Indicates whether the image is encrypted. |
| `hypervisor` | `string` | &lt;p&gt;The target hypervisor for the import task.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;xen&lt;/code&gt; &lt;/p&gt; |
| `usageOperation` | `string` | The usage operation value. |
| `snapshotDetailSet` | `array` | Information about the snapshots. |
| `imageId` | `string` | The ID of the Amazon Machine Image (AMI) of the imported virtual machine. |
| `kmsKeyId` | `string` | The identifier for the KMS key that was used to create the encrypted image. |
| `statusMessage` | `string` | A descriptive status message for the import image task. |
| `licenseType` | `string` | The license type of the virtual machine. |
| `architecture` | `string` | &lt;p&gt;The architecture of the virtual machine.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;i386&lt;/code&gt; \| &lt;code&gt;x86_64&lt;/code&gt; \| &lt;code&gt;arm64&lt;/code&gt; &lt;/p&gt; |
| `importTaskId` | `string` | The ID of the import image task. |
| `bootMode` | `string` | The boot mode of the virtual machine. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `import_image_tasks_Describe` | `SELECT` |  |
