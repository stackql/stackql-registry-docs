---
title: report
hide_title: false
hide_table_of_contents: false
keywords:
  - report
  - osconfig
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

Creates, updates, deletes, gets or lists a <code>report</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.report" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The `OSPolicyAssignmentReport` API resource name. Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/osPolicyAssignments/{os_policy_assignment_id}/report` |
| <CopyableCode code="instance" /> | `string` | The Compute Engine VM instance name. |
| <CopyableCode code="lastRunId" /> | `string` | Unique identifier of the last attempted run to apply the OS policies associated with this assignment on the VM. This ID is logged by the OS Config agent while applying the OS policies associated with this assignment on the VM. NOTE: If the service is unable to successfully connect to the agent for this run, then this id will not be available in the agent logs. |
| <CopyableCode code="osPolicyAssignment" /> | `string` | Reference to the `OSPolicyAssignment` API resource that the `OSPolicy` belongs to. Format: `projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}` |
| <CopyableCode code="osPolicyCompliances" /> | `array` | Compliance data for each `OSPolicy` that is applied to the VM. |
| <CopyableCode code="updateTime" /> | `string` | Timestamp for when the report was last generated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, osPolicyAssignmentsId, projectsId" /> | Get the OS policy assignment report for the specified Compute Engine VM instance. |

## `SELECT` examples

Get the OS policy assignment report for the specified Compute Engine VM instance.

```sql
SELECT
name,
instance,
lastRunId,
osPolicyAssignment,
osPolicyCompliances,
updateTime
FROM google.osconfig.report
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND osPolicyAssignmentsId = '{{ osPolicyAssignmentsId }}'
AND projectsId = '{{ projectsId }}';
```
