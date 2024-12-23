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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.appengine.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Output only. Relative name of the instance within the version. Example: instance-1. |
| <CopyableCode code="name" /> | `string` | Output only. Full path to the Instance resource in the API. Example: apps/myapp/services/default/versions/v1/instances/instance-1. |
| <CopyableCode code="appEngineRelease" /> | `string` | Output only. App Engine release this instance is running on. |
| <CopyableCode code="availability" /> | `string` | Output only. Availability of the instance. |
| <CopyableCode code="averageLatency" /> | `integer` | Output only. Average latency (ms) over the last minute. |
| <CopyableCode code="errors" /> | `integer` | Output only. Number of errors since this instance was started. |
| <CopyableCode code="memoryUsage" /> | `string` | Output only. Total memory in use (bytes). |
| <CopyableCode code="qps" /> | `number` | Output only. Average queries per second (QPS) over the last minute. |
| <CopyableCode code="requests" /> | `integer` | Output only. Number of requests since this instance was started. |
| <CopyableCode code="startTime" /> | `string` | Output only. Time that this instance was started.@OutputOnly |
| <CopyableCode code="vmDebugEnabled" /> | `boolean` | Output only. Whether this instance is in debug mode. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmId" /> | `string` | Output only. Virtual machine ID of this instance. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmIp" /> | `string` | Output only. The IP address of this instance. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmLiveness" /> | `string` | Output only. The liveness health check of this instance. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmName" /> | `string` | Output only. Name of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmStatus" /> | `string` | Output only. Status of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment. |
| <CopyableCode code="vmZoneName" /> | `string` | Output only. Zone where the virtual machine is located. Only applicable for instances in App Engine flexible environment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appsId, instancesId, servicesId, versionsId" /> | Gets instance information. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appsId, servicesId, versionsId" /> | Lists the instances of a version.Tip: To aggregate details about instances over time, see the Stackdriver Monitoring API (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appsId, instancesId, servicesId, versionsId" /> | Stops a running instance.The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" (standard environment (https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) | flexible environment (https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to STOPPED with the apps.services.versions.patch (https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method. |
| <CopyableCode code="debug" /> | `EXEC` | <CopyableCode code="appsId, instancesId, servicesId, versionsId" /> | Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment. |

## `SELECT` examples

Lists the instances of a version.Tip: To aggregate details about instances over time, see the Stackdriver Monitoring API (https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

```sql
SELECT
id,
name,
appEngineRelease,
availability,
averageLatency,
errors,
memoryUsage,
qps,
requests,
startTime,
vmDebugEnabled,
vmId,
vmIp,
vmLiveness,
vmName,
vmStatus,
vmZoneName
FROM google.appengine.instances
WHERE appsId = '{{ appsId }}'
AND servicesId = '{{ servicesId }}'
AND versionsId = '{{ versionsId }}';
```

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.appengine.instances
WHERE appsId = '{{ appsId }}'
AND instancesId = '{{ instancesId }}'
AND servicesId = '{{ servicesId }}'
AND versionsId = '{{ versionsId }}';
```
