---
title: machine_types
hide_title: false
hide_table_of_contents: false
keywords:
  - machine_types
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
<tr><td><b>Name</b></td><td><code>machine_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.machine_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | [Output Only] Name of the resource. |
| `description` | `string` | [Output Only] An optional textual description of the resource. |
| `memoryMb` | `integer` | [Output Only] The amount of physical memory available to the instance, defined in MB. |
| `kind` | `string` | [Output Only] The type of the resource. Always compute#machineType for machine types. |
| `zone` | `string` | [Output Only] The name of the zone where the machine type resides, such as us-central1-a. |
| `scratchDisks` | `array` | [Output Only] A list of extended scratch disks assigned to the instance. |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `accelerators` | `array` | [Output Only] A list of accelerator configurations assigned to this machine type. |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `imageSpaceGb` | `integer` | [Deprecated] This property is deprecated and will never be populated with any relevant values. |
| `guestCpus` | `integer` | [Output Only] The number of virtual CPUs that are available to the instance. |
| `maximumPersistentDisksSizeGb` | `string` | [Output Only] Maximum total persistent disks size (GB) allowed. |
| `maximumPersistentDisks` | `integer` | [Output Only] Maximum persistent disks allowed. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `isSharedCpu` | `boolean` | [Output Only] Whether this machine type has a shared CPU. See Shared-core machine types for more information. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `machineTypes_aggregatedList` | `SELECT` | `project` | Retrieves an aggregated list of machine types. |
| `machineTypes_get` | `SELECT` | `machineType, project, zone` | Returns the specified machine type. Gets a list of available machine types by making a list() request. |
| `machineTypes_list` | `SELECT` | `project, zone` | Retrieves a list of machine types available to the specified project. |
