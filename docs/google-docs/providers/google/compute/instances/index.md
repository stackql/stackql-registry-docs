---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - compute
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
<tr><td><b>Id</b></td><td><code>google.compute.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `lastStartTimestamp` | `string` | [Output Only] Last start timestamp in RFC3339 text format. |
| `resourcePolicies` | `array` | Resource policies applied to this instance. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#instance for instances. |
| `canIpForward` | `boolean` | Allows this instance to send and receive packets with non-matching destination or source IPs. This is required if you plan to use this instance to forward routes. For more information, see Enabling IP Forwarding . |
| `confidentialInstanceConfig` | `object` | A set of Confidential Instance options. |
| `shieldedInstanceConfig` | `object` | A set of Shielded Instance options. |
| `displayDevice` | `object` | A set of Display Device options |
| `startRestricted` | `boolean` | [Output Only] Whether a VM has been restricted for start because Compute Engine has detected suspicious activity. |
| `hostname` | `string` | Specifies the hostname of the instance. The specified hostname must be RFC1035 compliant. If hostname is not specified, the default hostname is [INSTANCE_NAME].c.[PROJECT_ID].internal when using the global DNS, and [INSTANCE_NAME].[ZONE].c.[PROJECT_ID].internal when using zonal DNS. |
| `deletionProtection` | `boolean` | Whether the resource should be protected against deletion. |
| `params` | `object` | Additional instance params. |
| `advancedMachineFeatures` | `object` | Specifies options for controlling advanced machine features. Options that would traditionally be configured in a BIOS belong here. Features that require operating system support may have corresponding entries in the GuestOsFeatures of an Image (e.g., whether or not the OS in the Image supports nested virtualization being enabled or disabled). |
| `scheduling` | `object` | Sets the scheduling options for an Instance. NextID: 21 |
| `machineType` | `string` | Full or partial URL of the machine type resource to use for this instance, in the format: zones/zone/machineTypes/machine-type. This is provided by the client when the instance is created. For example, the following is a valid partial url to a predefined machine type: zones/us-central1-f/machineTypes/n1-standard-1 To create a custom machine type, provide a URL to a machine type in the following format, where CPUS is 1 or an even number up to 32 (2, 4, 6, ... 24, etc), and MEMORY is the total memory for this instance. Memory must be a multiple of 256 MB and must be supplied in MB (e.g. 5 GB of memory is 5120 MB): zones/zone/machineTypes/custom-CPUS-MEMORY For example: zones/us-central1-f/machineTypes/custom-4-5120 For a full list of restrictions, read the Specifications for custom machine types. |
| `disks` | `array` | Array of disks associated with this instance. Persistent disks must be created before you can assign them. |
| `keyRevocationActionType` | `string` | KeyRevocationActionType of the instance. Supported options are "STOP" and "NONE". The default value is "NONE" if it is not specified. |
| `zone` | `string` | [Output Only] URL of the zone where the instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `networkPerformanceConfig` | `object` |  |
| `metadata` | `object` | A metadata key/value entry. |
| `sourceMachineImageEncryptionKey` | `object` |  |
| `selfLink` | `string` | [Output Only] Server-defined URL for this resource. |
| `lastStopTimestamp` | `string` | [Output Only] Last stop timestamp in RFC3339 text format. |
| `reservationAffinity` | `object` | Specifies the reservations that this instance can consume from. |
| `minCpuPlatform` | `string` | Specifies a minimum CPU platform for the VM instance. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: "Intel Haswell" or minCpuPlatform: "Intel Sandy Bridge". |
| `tags` | `object` | A set of instance tags. |
| `sourceMachineImage` | `string` | Source machine image |
| `lastSuspendedTimestamp` | `string` | [Output Only] Last suspended timestamp in RFC3339 text format. |
| `serviceAccounts` | `array` | A list of service accounts, with their specified scopes, authorized for this instance. Only one service account per VM instance is supported. Service accounts generate access tokens that can be accessed through the metadata server and used to authenticate applications on the instance. See Service Accounts for more information. |
| `statusMessage` | `string` | [Output Only] An optional, human-readable explanation of the status. |
| `status` | `string` | [Output Only] The status of the instance. One of the following values: PROVISIONING, STAGING, RUNNING, STOPPING, SUSPENDING, SUSPENDED, REPAIRING, and TERMINATED. For more information about the status of the instance, see Instance life cycle. |
| `shieldedInstanceIntegrityPolicy` | `object` | The policy describes the baseline against which Instance boot integrity is measured. |
| `labelFingerprint` | `string` | A fingerprint for this request, which is essentially a hash of the label's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels. To see the latest fingerprint, make get() request to the instance. |
| `labels` | `object` | Labels to apply to this instance. These can be later modified by the setLabels method. |
| `privateIpv6GoogleAccess` | `string` | The private IPv6 google access type for the VM. If not specified, use INHERIT_FROM_SUBNETWORK as default. |
| `networkInterfaces` | `array` | An array of network configurations for this instance. These specify how interfaces are configured to interact with other network services, such as connecting to the internet. Multiple interfaces are supported per instance. |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `guestAccelerators` | `array` | A list of the type and count of accelerator cards attached to the instance. |
| `cpuPlatform` | `string` | [Output Only] The CPU platform used by this instance. |
| `fingerprint` | `string` | Specifies a fingerprint for this resource, which is essentially a hash of the instance's contents and used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update the instance. You must always provide an up-to-date fingerprint hash in order to update the instance. To see the latest fingerprint, make get() request to the instance. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of all of the instances in your project across all regions and zones. The performance of this method degrades when a filter is specified on a project that has a very large number of instances. |
| `get` | `SELECT` | `instance, project, zone` | Returns the specified Instance resource. Gets a list of available instances by making a list() request. |
| `list` | `SELECT` | `project, zone` | Retrieves the list of instances contained within the specified zone. |
| `insert` | `INSERT` | `project, zone` | Creates an instance resource in the specified project using the data included in the request. |
| `delete` | `DELETE` | `instance, project, zone` | Deletes the specified Instance resource. For more information, see Deleting an instance. |
| `attachDisk` | `EXEC` | `instance, project, zone` | Attaches an existing Disk resource to an instance. You must first create the disk before you can attach it. It is not possible to create and attach a disk at the same time. For more information, read Adding a persistent disk to your instance. |
| `detachDisk` | `EXEC` | `deviceName, instance, project, zone` | Detaches a disk from an instance. |
| `reset` | `EXEC` | `instance, project, zone` | Performs a reset on the instance. This is a hard reset. The VM does not do a graceful shutdown. For more information, see Resetting an instance. |
| `resume` | `EXEC` | `instance, project, zone` | Resumes an instance that was suspended using the instances().suspend method. |
| `sendDiagnosticInterrupt` | `EXEC` | `instance, project, zone` | Sends diagnostic interrupt to the instance. |
| `setDeletionProtection` | `EXEC` | `project, resource, zone` | Sets deletion protection on the instance. |
| `setDiskAutoDelete` | `EXEC` | `autoDelete, deviceName, instance, project, zone` | Sets the auto-delete flag for a disk attached to an instance. |
| `setLabels` | `EXEC` | `instance, project, zone` | Sets labels on an instance. To learn more about labels, read the Labeling Resources documentation. |
| `setMachineResources` | `EXEC` | `instance, project, zone` | Changes the number and/or type of accelerator for a stopped instance to the values specified in the request. |
| `setMachineType` | `EXEC` | `instance, project, zone` | Changes the machine type for a stopped instance to the machine type specified in the request. |
| `setMetadata` | `EXEC` | `instance, project, zone` | Sets metadata for the specified instance to the data included in the request. |
| `setMinCpuPlatform` | `EXEC` | `instance, project, zone` | Changes the minimum CPU platform that this instance should use. This method can only be called on a stopped instance. For more information, read Specifying a Minimum CPU Platform. |
| `setScheduling` | `EXEC` | `instance, project, zone` | Sets an instance's scheduling options. You can only call this method on a stopped instance, that is, a VM instance that is in a `TERMINATED` state. See Instance Life Cycle for more information on the possible instance states. For more information about setting scheduling options for a VM, see Set VM host maintenance policy. |
| `setServiceAccount` | `EXEC` | `instance, project, zone` | Sets the service account on the instance. For more information, read Changing the service account and access scopes for an instance. |
| `setShieldedInstanceIntegrityPolicy` | `EXEC` | `instance, project, zone` | Sets the Shielded Instance integrity policy for an instance. You can only use this method on a running instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `setTags` | `EXEC` | `instance, project, zone` | Sets network tags for the specified instance to the data included in the request. |
| `simulateMaintenanceEvent` | `EXEC` | `instance, project, zone` | Simulates a host maintenance event on a VM. For more information, see Simulate a host maintenance event. |
| `start` | `EXEC` | `instance, project, zone` | Starts an instance that was stopped using the instances().stop method. For more information, see Restart an instance. |
| `startWithEncryptionKey` | `EXEC` | `instance, project, zone` | Starts an instance that was stopped using the instances().stop method. For more information, see Restart an instance. |
| `stop` | `EXEC` | `instance, project, zone` | Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges while they are stopped. However, resources that the VM is using, such as persistent disks and static IP addresses, will continue to be charged until they are deleted. For more information, see Stopping an instance. |
| `suspend` | `EXEC` | `instance, project, zone` | This method suspends a running instance, saving its state to persistent storage, and allows you to resume the instance at a later time. Suspended instances have no compute costs (cores or RAM), and incur only storage charges for the saved VM memory and localSSD data. Any charged resources the virtual machine was using, such as persistent disks and static IP addresses, will continue to be charged while the instance is suspended. For more information, see Suspending and resuming an instance. |
| `update` | `EXEC` | `instance, project, zone` | Updates an instance only if the necessary resources are available. This method can update only a specific set of instance properties. See Updating a running instance for a list of updatable instance properties. |
| `updateAccessConfig` | `EXEC` | `instance, networkInterface, project, zone` | Updates the specified access config from an instance's network interface with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `updateDisplayDevice` | `EXEC` | `instance, project, zone` | Updates the Display config for a VM instance. You can only use this method on a stopped VM instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
| `updateNetworkInterface` | `EXEC` | `instance, networkInterface, project, zone` | Updates an instance's network interface. This method can only update an interface's alias IP range and attached network. See Modifying alias IP ranges for an existing instance for instructions on changing alias IP ranges. See Migrating a VM between networks for instructions on migrating an interface. This method follows PATCH semantics. |
| `updateShieldedInstanceConfig` | `EXEC` | `instance, project, zone` | Updates the Shielded Instance config for an instance. You can only use this method on a stopped instance. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |
