---
title: workstation_configs_usable
hide_title: false
hide_table_of_contents: false
keywords:
  - workstation_configs_usable
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workstation_configs_usable</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workstations.workstation_configs_usable" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Full name of this workstation configuration. |
| <CopyableCode code="annotations" /> | `object` | Optional. Client-specified annotations. |
| <CopyableCode code="conditions" /> | `array` | Output only. Status conditions describing the current resource state. |
| <CopyableCode code="container" /> | `object` | A Docker container. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when this workstation configuration was created. |
| <CopyableCode code="degraded" /> | `boolean` | Output only. Whether this resource is degraded, in which case it may require user action to restore full functionality. See also the conditions field. |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when this workstation configuration was soft-deleted. |
| <CopyableCode code="disableTcpConnections" /> | `boolean` | Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections through a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain TCP connections, such as SSH. When enabled, all communication must occur over HTTPS or WSS. |
| <CopyableCode code="displayName" /> | `string` | Optional. Human-readable name for this workstation configuration. |
| <CopyableCode code="enableAuditAgent" /> | `boolean` | Optional. Whether to enable Linux `auditd` logging on the workstation. When enabled, a service account must also be specified that has `logging.buckets.write` permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging). |
| <CopyableCode code="encryptionKey" /> | `object` | A customer-managed encryption key (CMEK) for the Compute Engine resources of the associated workstation configuration. Specify the name of your Cloud KMS encryption key and the default service account. We recommend that you use a separate service account and follow [Cloud KMS best practices](https://cloud.google.com/kms/docs/separation-of-duties). |
| <CopyableCode code="ephemeralDirectories" /> | `array` | Optional. Ephemeral directories which won't persist across workstation sessions. |
| <CopyableCode code="etag" /> | `string` | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |
| <CopyableCode code="host" /> | `object` | Runtime host for a workstation. |
| <CopyableCode code="idleTimeout" /> | `string` | Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic. A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by `s` for seconds—for example, `"7200s"` (2 hours). The default is `"1200s"` (20 minutes). |
| <CopyableCode code="labels" /> | `object` | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources. |
| <CopyableCode code="persistentDirectories" /> | `array` | Optional. Directories to persist across workstation sessions. |
| <CopyableCode code="readinessChecks" /> | `array` | Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes. |
| <CopyableCode code="reconciling" /> | `boolean` | Output only. Indicates whether this workstation configuration is currently being updated to match its intended state. |
| <CopyableCode code="replicaZones" /> | `array` | Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster's region must be specified—for example, `['us-central1-a', 'us-central1-f']`. If this field is empty, two default zones within the region are used. Immutable after the workstation configuration is created. |
| <CopyableCode code="runningTimeout" /> | `string` | Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle. Provide duration terminated by `s` for seconds—for example, `"54000s"` (15 hours). Defaults to `"43200s"` (12 hours). A value of `"0s"` indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than `"0s"` and less than `"86400s"` (24 hours). Warning: A value of `"0s"` indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates. |
| <CopyableCode code="uid" /> | `string` | Output only. A system-assigned unique identifier for this workstation configuration. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when this workstation configuration was most recently updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_usable" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> |
| <CopyableCode code="_list_usable" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, workstationClustersId" /> |
