---
title: workloads
hide_title: false
hide_table_of_contents: false
keywords:
  - workloads
  - apphub
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
<tr><td><b>Name</b></td><td><code>workloads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="apphub.workloads" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the Workload. Format: "projects/&#123;host-project-id&#125;/locations/&#123;location&#125;/applications/&#123;application-id&#125;/workloads/&#123;workload-id&#125;" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of a Workload. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="discoveredWorkload" /> | `string` | Required. Immutable. The resource name of the original discovered workload. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Workload. Can have a maximum length of 63 characters. |
| <CopyableCode code="state" /> | `string` | Output only. Workload state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (UUID) for the `Workload` in the UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |
| <CopyableCode code="workloadProperties" /> | `object` | Properties of an underlying compute resource represented by the Workload. |
| <CopyableCode code="workloadReference" /> | `object` | Reference of an underlying compute resource represented by the Workload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Gets a Workload in an Application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Workloads in an Application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Creates a Workload in an Application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Deletes a Workload from an Application. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Workloads in an Application. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationsId, locationsId, projectsId, workloadsId" /> | Updates a Workload in an Application. |
