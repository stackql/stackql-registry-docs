---
title: workstation_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_configs
  - workstations
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
<tr><td><b>Name</b></td><td><code>workstation_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.workstations.workstation_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Full name of this resource. |
| `degraded` | `boolean` | Output only. Whether this resource is degraded, in which case it may require user action to restore full functionality. See also the `conditions` field. |
| `readinessChecks` | `array` | Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes. |
| `runningTimeout` | `string` | Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The `idleTimeout` and `runningTimeout` parameters are independent of each other. Note that the `runningTimeout` parameter shuts down VMs after the specified time, regardless of whether or not the VMs are idle. Provide duration terminated by `s` for seconds—for example, `54000s` (15 hours). Defaults to `43200s` (12 hours). A value of `0` indicates that workstations using this configuration should never time out. If `encryption_key` is set, it must be greater than `0` and less than `86400s` (24 hours). Warning: A value of `0s` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates. |
| `deleteTime` | `string` | Output only. Time when this resource was soft-deleted. |
| `createTime` | `string` | Output only. Time when this resource was created. |
| `uid` | `string` | Output only. A system-assigned unique identifier for this resource. |
| `annotations` | `object` | Client-specified annotations. |
| `container` | `object` | A Docker container. |
| `displayName` | `string` | Human-readable name for this resource. |
| `updateTime` | `string` | Output only. Time when this resource was most recently updated. |
| `enableAuditAgent` | `boolean` | Whether to enable Linux `auditd` logging on the workstation. When enabled, a service account must also be specified that has `logging.buckets.write` permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging). |
| `persistentDirectories` | `array` | Directories to persist across workstation sessions. |
| `reconciling` | `boolean` | Output only. Indicates whether this resource is currently being updated to match its intended state. |
| `conditions` | `array` | Output only. Status conditions describing the current resource state. |
| `etag` | `string` | Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| `encryptionKey` | `object` | A customer-managed encryption key (CMEK) for the Compute Engine resources of the associated workstation configuration. Specify the name of your Cloud KMS encryption key and the default service account. We recommend that you use a separate service account and follow [Cloud KMS best practices](https://cloud.google.com/kms/docs/separation-of-duties). |
| `idleTimeout` | `string` | Number of seconds to wait before automatically stopping a workstation after it last received user traffic. A value of `0s` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `7200s` (2 hours). The default is `1200s` (20 minutes). |
| `host` | `object` | Runtime host for a workstation. |
| `labels` | `object` | Client-specified labels that are applied to the resource and that are also propagated to the underlying Compute Engine resources. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Returns the requested workstation configuration. |
| `list` | `SELECT` | `locationsId, projectsId, workstationClustersId` | Returns all workstation configurations in the specified cluster. |
| `create` | `INSERT` | `locationsId, projectsId, workstationClustersId` | Creates a new workstation configuration. |
| `delete` | `DELETE` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Deletes the specified workstation configuration. |
| `_list` | `EXEC` | `locationsId, projectsId, workstationClustersId` | Returns all workstation configurations in the specified cluster. |
| `patch` | `EXEC` | `locationsId, projectsId, workstationClustersId, workstationConfigsId` | Updates an existing workstation configuration. |
