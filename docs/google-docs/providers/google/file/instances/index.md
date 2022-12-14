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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.file.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the instance, in the format `projects/&#123;project&#125;/locations/&#123;location&#125;/instances/&#123;instance&#125;`. |
| `description` | `string` | The description of the instance (2048 characters or less). |
| `kmsKeyName` | `string` | KMS key name used for data encryption. |
| `etag` | `string` | Server-specified ETag for the instance resource to prevent simultaneous updates from overwriting each other. |
| `fileShares` | `array` | File system shares on the instance. For this version, only a single file share is supported. |
| `suspensionReasons` | `array` | Output only. Field indicates all the reasons the instance is in "SUSPENDED" state. |
| `labels` | `object` | Resource labels to represent user provided metadata. |
| `networks` | `array` | VPC networks to which the instance is connected. For this version, only a single network is supported. |
| `createTime` | `string` | Output only. The time when the instance was created. |
| `state` | `string` | Output only. The instance state. |
| `satisfiesPzs` | `boolean` | Output only. Reserved for future use. |
| `tier` | `string` | The service tier of the instance. |
| `statusMessage` | `string` | Output only. Additional information about the instance state, if available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets the details of a specific instance. |
| `projects_locations_instances_list` | `SELECT` | `locationsId, projectsId` | Lists all instances in a project for either a specified location or for all locations. |
| `projects_locations_instances_create` | `INSERT` | `locationsId, projectsId` | Creates an instance. When creating from a backup, the capacity of the new instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
| `projects_locations_instances_delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes an instance. |
| `projects_locations_instances_patch` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the settings of a specific instance. |
| `projects_locations_instances_restore` | `EXEC` | `instancesId, locationsId, projectsId` | Restores an existing instance's file share from a backup. The capacity of the instance needs to be equal to or larger than the capacity of the backup (and also equal to or larger than the minimum capacity of the tier). |
