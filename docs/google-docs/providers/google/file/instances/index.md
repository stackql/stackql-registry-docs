---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - file
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.file.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the instance, in the format `projects/&#123;project&#125;/locations/&#123;location&#125;/instances/&#123;instance&#125;`. |
| <CopyableCode code="description" /> | `string` | The description of the instance (2048 characters or less). |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the instance was created. |
| <CopyableCode code="etag" /> | `string` | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. |
| <CopyableCode code="fileShares" /> | `array` | File system shares on the instance. For this version, only a single file share is supported. |
| <CopyableCode code="kmsKeyName" /> | `string` | KMS key name used for data encryption. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user provided metadata. |
| <CopyableCode code="networks" /> | `array` | VPC networks to which the instance is connected. For this version, only a single network is supported. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. The instance state. |
| <CopyableCode code="statusMessage" /> | `string` | Output only. Additional information about the instance state, if available. |
| <CopyableCode code="suspensionReasons" /> | `array` | Output only. Field indicates all the reasons the instance is in "SUSPENDED" state. |
| <CopyableCode code="tier" /> | `string` | The service tier of the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets the details of a specific instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all instances in a project for either a specified location or for all locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Deletes an instance. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists all instances in a project for either a specified location or for all locations. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Updates the settings of a specific instance. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Restores an existing instance's file share from a backup. The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| <CopyableCode code="revert" /> | `EXEC` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Revert an existing instance's file system to a specified snapshot. |
