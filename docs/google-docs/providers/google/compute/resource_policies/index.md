---
title: resource_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_policies
  - compute
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
<tr><td><b>Name</b></td><td><code>resource_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.resource_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` |  |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="diskConsistencyGroupPolicy" /> | `object` | Resource policy for disk consistency groups. |
| <CopyableCode code="groupPlacementPolicy" /> | `object` | A GroupPlacementPolicy specifies resource placement configuration. It specifies the failure bucket separation as well as network locality |
| <CopyableCode code="instanceSchedulePolicy" /> | `object` | An InstanceSchedulePolicy specifies when and how frequent certain operations are performed on the instance. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#resource_policies for resource policies. |
| <CopyableCode code="region" /> | `string` |  |
| <CopyableCode code="resourceStatus" /> | `object` | Contains output only fields. Use this sub-message for all output fields set on ResourcePolicy. The internal structure of this "status" field should mimic the structure of ResourcePolicy proto specification. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| <CopyableCode code="snapshotSchedulePolicy" /> | `object` | A snapshot schedule policy specifies when and how frequently snapshots are to be created for the target disk. Also specifies how many and how long these scheduled snapshots should be retained. |
| <CopyableCode code="status" /> | `string` | [Output Only] The status of resource policy creation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="aggregated_list" /> | `SELECT` | <CopyableCode code="project" /> | Retrieves an aggregated list of resource policies. |
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="project, region, resourcePolicy" /> | Retrieves all information of the specified resource policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | A list all the resource policies that have been configured for the specified project in specified region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a new resource policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="project, region, resourcePolicy" /> | Deletes the specified resource policy. |
| <CopyableCode code="_aggregated_list" /> | `EXEC` | <CopyableCode code="project" /> | Retrieves an aggregated list of resource policies. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="project, region, resourcePolicy" /> | Modify the specified resource policy. |
