---
title: runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - runtimes
  - notebooks
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
<tr><td><b>Name</b></td><td><code>runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.notebooks.runtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the runtime. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/runtimes/&#123;runtimeId&#125;` |
| `softwareConfig` | `object` | Specifies the selection and configuration of software inside the runtime. The properties to set on runtime. Properties keys are specified in `key:value` format, for example: * `idle_shutdown: true` * `idle_shutdown_timeout: 180` * `enable_health_monitoring: true` |
| `createTime` | `string` | Output only. Runtime creation time. |
| `updateTime` | `string` | Output only. Runtime update time. |
| `virtualMachine` | `object` | Runtime using Virtual Machine for computing. |
| `state` | `string` | Output only. Runtime state. |
| `healthState` | `string` | Output only. Runtime health_state. |
| `accessConfig` | `object` | Specifies the login configuration for Runtime |
| `metrics` | `object` | Contains runtime daemon metrics, such as OS and kernels and sessions stats. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_runtimes_get` | `SELECT` | `locationsId, projectsId, runtimesId` | Gets details of a single Runtime. The location must be a regional endpoint rather than zonal. |
| `projects_locations_runtimes_list` | `SELECT` | `locationsId, projectsId` | Lists Runtimes in a given project and location. |
| `projects_locations_runtimes_create` | `INSERT` | `locationsId, projectsId` | Creates a new Runtime in a given project and location. |
| `projects_locations_runtimes_delete` | `DELETE` | `locationsId, projectsId, runtimesId` | Deletes a single Runtime. |
| `projects_locations_runtimes_diagnose` | `EXEC` | `locationsId, projectsId, runtimesId` | Creates a Diagnostic File and runs Diagnostic Tool given a Runtime. |
| `projects_locations_runtimes_patch` | `EXEC` | `locationsId, projectsId, runtimesId` | Update Notebook Runtime configuration. |
| `projects_locations_runtimes_refreshRuntimeTokenInternal` | `EXEC` | `locationsId, projectsId, runtimesId` | Gets an access token for the consumer service account that the customer attached to the runtime. Only accessible from the tenant instance. |
| `projects_locations_runtimes_reportEvent` | `EXEC` | `locationsId, projectsId, runtimesId` | Report and process a runtime event. |
| `projects_locations_runtimes_reset` | `EXEC` | `locationsId, projectsId, runtimesId` | Resets a Managed Notebook Runtime. |
| `projects_locations_runtimes_start` | `EXEC` | `locationsId, projectsId, runtimesId` | Starts a Managed Notebook Runtime. Perform "Start" on GPU instances; "Resume" on CPU instances See: https://cloud.google.com/compute/docs/instances/stop-start-instance https://cloud.google.com/compute/docs/instances/suspend-resume-instance |
| `projects_locations_runtimes_stop` | `EXEC` | `locationsId, projectsId, runtimesId` | Stops a Managed Notebook Runtime. Perform "Stop" on GPU instances; "Suspend" on CPU instances See: https://cloud.google.com/compute/docs/instances/stop-start-instance https://cloud.google.com/compute/docs/instances/suspend-resume-instance |
| `projects_locations_runtimes_switch` | `EXEC` | `locationsId, projectsId, runtimesId` | Switch a Managed Notebook Runtime. |
| `projects_locations_runtimes_upgrade` | `EXEC` | `locationsId, projectsId, runtimesId` | Upgrades a Managed Notebook Runtime to the latest version. |
