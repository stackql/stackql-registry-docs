---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - notebooks
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.notebooks.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The name of this notebook instance. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` |
| `acceleratorConfig` | `object` | Definition of a hardware accelerator. Note that not all combinations of `type` and `core_count` are valid. Check [GPUs on Compute Engine](/compute/docs/gpus/#gpus-list) to find a valid combination. TPUs are not supported. |
| `kmsKey` | `string` | Input only. The KMS key used to encrypt the disks, only applicable if disk_encryption is CMEK. Format: `projects/{project_id}/locations/{location}/keyRings/{key_ring_id}/cryptoKeys/{key_id}` Learn more about [using your own encryption keys](/kms/docs/quickstart). |
| `reservationAffinity` | `object` | Reservation Affinity for consuming Zonal reservation. |
| `vmImage` | `object` | Definition of a custom Compute Engine virtual machine image for starting a notebook instance with the environment installed directly on the VM. |
| `labels` | `object` | Labels to apply to this instance. These can be later modified by the setLabels method. |
| `creator` | `string` | Output only. Email address of entity that sent original CreateInstance request. |
| `noPublicIp` | `boolean` | If true, no public IP will be assigned to this instance. |
| `customGpuDriverPath` | `string` | Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers. |
| `proxyUri` | `string` | Output only. The proxy endpoint that is used to access the Jupyter notebook. |
| `instanceOwners` | `array` | Input only. The owner of this instance after creation. Format: `alias@example.com` Currently supports one owner only. If not specified, all of the service account users of your VM instance's service account can use the instance. |
| `serviceAccountScopes` | `array` | Optional. The URIs of service account scopes to be included in Compute Engine instances. If not specified, the following [scopes](https://cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) are defined: - https://www.googleapis.com/auth/cloud-platform - https://www.googleapis.com/auth/userinfo.email If not using default scopes, you need at least: https://www.googleapis.com/auth/compute |
| `canIpForward` | `boolean` | Optional. Flag to enable ip forwarding or not, default false/off. https://cloud.google.com/vpc/docs/using-routes#canipforward |
| `installGpuDriver` | `boolean` | Whether the end user authorizes Google Cloud to install GPU driver on this instance. If this field is empty or set to false, the GPU driver won't be installed. Only applicable to instances with GPUs. |
| `createTime` | `string` | Output only. Instance creation time. |
| `nicType` | `string` | Optional. The type of vNIC to be used on this interface. This may be gVNIC or VirtioNet. |
| `diskEncryption` | `string` | Input only. Disk encryption method used on the boot and data disks, defaults to GMEK. |
| `shieldedInstanceConfig` | `object` | A set of Shielded Instance options. Check [Images using supported Shielded VM features] Not all combinations are valid. |
| `bootDiskSizeGb` | `string` | Input only. The size of the boot disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). The minimum recommended value is 100 GB. If not specified, this defaults to 100. |
| `bootDiskType` | `string` | Input only. The type of the boot disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). |
| `disks` | `array` | Output only. Attached disks to notebook instance. |
| `metadata` | `object` | Custom metadata to apply to this instance. |
| `network` | `string` | The name of the VPC that this instance is in. Format: `projects/{project_id}/global/networks/{network_id}` |
| `state` | `string` | Output only. The state of this instance. |
| `postStartupScript` | `string` | Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`). |
| `dataDiskType` | `string` | Input only. The type of the data disk attached to this instance, defaults to standard persistent disk (`PD_STANDARD`). |
| `tags` | `array` | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/compute/docs/label-or-tag-resources#tags)). |
| `noProxyAccess` | `boolean` | If true, the notebook instance will not register with the proxy. |
| `noRemoveDataDisk` | `boolean` | Input only. If true, the data disk will not be auto deleted when deleting the instance. |
| `containerImage` | `object` | Definition of a container image for starting a notebook instance with the environment installed in a container. |
| `updateTime` | `string` | Output only. Instance update time. |
| `dataDiskSizeGb` | `string` | Input only. The size of the data disk in GB attached to this instance, up to a maximum of 64000 GB (64 TB). You can choose the size of the data disk based on how big your notebooks and data are. If not specified, this defaults to 100. |
| `upgradeHistory` | `array` | The upgrade history of this instance. |
| `subnet` | `string` | The name of the subnet that this instance is in. Format: `projects/{project_id}/regions/{region}/subnetworks/{subnetwork_id}` |
| `serviceAccount` | `string` | The service account on this instance, giving access to other Google Cloud services. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. |
| `machineType` | `string` | Required. The [Compute Engine machine type](/compute/docs/machine-types) of this instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `instancesId, locationsId, projectsId` | Gets details of a single Instance. |
| `projects_locations_instances_list` | `SELECT` | `locationsId, projectsId` | Lists instances in a given project and location. |
| `projects_locations_instances_create` | `INSERT` | `locationsId, projectsId` | Creates a new Instance in a given project and location. |
| `projects_locations_instances_delete` | `DELETE` | `instancesId, locationsId, projectsId` | Deletes a single Instance. |
| `projects_locations_instances_isUpgradeable` | `EXEC` | `instancesId, locationsId, projectsId` | Check if a notebook instance is upgradable. |
| `projects_locations_instances_register` | `EXEC` | `locationsId, projectsId` | Registers an existing legacy notebook instance to the Notebooks API server. Legacy instances are instances created with the legacy Compute Engine calls. They are not manageable by the Notebooks API out of the box. This call makes these instances manageable by the Notebooks API. |
| `projects_locations_instances_report` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly. |
| `projects_locations_instances_reset` | `EXEC` | `instancesId, locationsId, projectsId` | Resets a notebook instance. |
| `projects_locations_instances_rollback` | `EXEC` | `instancesId, locationsId, projectsId` | Rollbacks a notebook instance to the previous version. |
| `projects_locations_instances_setAccelerator` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the guest accelerators of a single Instance. |
| `projects_locations_instances_setLabels` | `EXEC` | `instancesId, locationsId, projectsId` | Replaces all the labels of an Instance. |
| `projects_locations_instances_setMachineType` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the machine type of a single Instance. |
| `projects_locations_instances_start` | `EXEC` | `instancesId, locationsId, projectsId` | Starts a notebook instance. |
| `projects_locations_instances_stop` | `EXEC` | `instancesId, locationsId, projectsId` | Stops a notebook instance. |
| `projects_locations_instances_updateConfig` | `EXEC` | `instancesId, locationsId, projectsId` | Update Notebook Instance configurations. |
| `projects_locations_instances_updateMetadataItems` | `EXEC` | `instancesId, locationsId, projectsId` | Add/update metadata items for an instance. |
| `projects_locations_instances_updateShieldedInstanceConfig` | `EXEC` | `instancesId, locationsId, projectsId` | Updates the Shielded instance configuration of a single Instance. |
| `projects_locations_instances_upgrade` | `EXEC` | `instancesId, locationsId, projectsId` | Upgrades a notebook instance to the latest version. |
| `projects_locations_instances_upgradeInternal` | `EXEC` | `instancesId, locationsId, projectsId` | Allows notebook instances to call this endpoint to upgrade themselves. Do not use this method directly. |
