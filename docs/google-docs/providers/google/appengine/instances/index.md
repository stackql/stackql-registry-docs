---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - appengine
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
<tr><td><b>Id</b></td><td><code>google.appengine.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. Relative name of the instance within the version. Example: instance-1. |
| `name` | `string` | Output only. Full path to the Instance resource in the API. Example: apps/myapp/services/default/versions/v1/instances/instance-1. |
| `vmLiveness` | `string` | Output only. The liveness health check of this instance. Only applicable for instances in App Engine flexible environment. |
| `vmIp` | `string` | Output only. The IP address of this instance. Only applicable for instances in App Engine flexible environment. |
| `errors` | `integer` | Output only. Number of errors since this instance was started. |
| `vmStatus` | `string` | Output only. Status of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. |
| `requests` | `integer` | Output only. Number of requests since this instance was started. |
| `startTime` | `string` | Output only. Time that this instance was started.@OutputOnly |
| `vmName` | `string` | Output only. Name of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. |
| `vmZoneName` | `string` | Output only. Zone where the virtual machine is located. Only applicable for instances in App Engine flexible environment. |
| `averageLatency` | `integer` | Output only. Average latency (ms) over the last minute. |
| `qps` | `number` | Output only. Average queries per second (QPS) over the last minute. |
| `availability` | `string` | Output only. Availability of the instance. |
| `vmDebugEnabled` | `boolean` | Output only. Whether this instance is in debug mode. Only applicable for instances in App Engine flexible environment. |
| `appEngineRelease` | `string` | Output only. App Engine release this instance is running on. |
| `vmId` | `string` | Output only. Virtual machine ID of this instance. Only applicable for instances in App Engine flexible environment. |
| `memoryUsage` | `string` | Output only. Total memory in use (bytes). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `apps_services_versions_instances_get` | `SELECT` | `appsId, instancesId, servicesId, versionsId` | Gets instance information. |
| `apps_services_versions_instances_list` | `SELECT` | `appsId, servicesId, versionsId` | Lists the instances of a version.Tip: To aggregate details about instances over time, see the Stackdriver Monitoring API (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). |
| `apps_services_versions_instances_delete` | `DELETE` | `appsId, instancesId, servicesId, versionsId` | Stops a running instance.The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" (standard environment (https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) \| flexible environment (https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to STOPPED with the apps.services.versions.patch (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method. |
| `apps_services_versions_instances_debug` | `EXEC` | `appsId, instancesId, servicesId, versionsId` | Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment. |
