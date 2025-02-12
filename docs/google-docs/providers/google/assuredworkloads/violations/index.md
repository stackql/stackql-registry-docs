---
title: violations
hide_title: false
hide_table_of_contents: false
keywords:
  - violations
  - assuredworkloads
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

Creates, updates, deletes, gets or lists a <code>violations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>violations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.assuredworkloads.violations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Immutable. Name of the Violation. Format: organizations/{organization}/locations/{location}/workloads/{workload_id}/violations/{violations_id} |
| <CopyableCode code="description" /> | `string` | Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value. |
| <CopyableCode code="acknowledged" /> | `boolean` | A boolean that indicates if the violation is acknowledged |
| <CopyableCode code="acknowledgementTime" /> | `string` | Optional. Timestamp when this violation was acknowledged first. Check exception_contexts to find the last time the violation was acknowledged when there are more than one violations. This field will be absent when acknowledged field is marked as false. |
| <CopyableCode code="associatedOrgPolicyViolationId" /> | `string` | Optional. Output only. Violation Id of the org-policy violation due to which the resource violation is caused. Empty for org-policy violations. |
| <CopyableCode code="auditLogLink" /> | `string` | Output only. Immutable. Audit Log Link for violated resource Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{timeRange}{folder} |
| <CopyableCode code="beginTime" /> | `string` | Output only. Time of the event which triggered the Violation. |
| <CopyableCode code="category" /> | `string` | Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc. |
| <CopyableCode code="exceptionAuditLogLink" /> | `string` | Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: https://console.cloud.google.com/logs/query;query={logName}{protoPayload.resourceName}{protoPayload.methodName}{timeRange}{organization} |
| <CopyableCode code="exceptionContexts" /> | `array` | Output only. List of all the exception detail added for the violation. |
| <CopyableCode code="nonCompliantOrgPolicy" /> | `string` | Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/{project_number}/policies/{constraint_name} folders/{folder_id}/policies/{constraint_name} organizations/{organization_id}/policies/{constraint_name} |
| <CopyableCode code="orgPolicyConstraint" /> | `string` | Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation. |
| <CopyableCode code="parentProjectNumber" /> | `string` | Optional. Output only. Parent project number where resource is present. Empty for org-policy violations. |
| <CopyableCode code="remediation" /> | `object` | Represents remediation guidance to resolve compliance violation for AssuredWorkload |
| <CopyableCode code="resolveTime" /> | `string` | Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty. |
| <CopyableCode code="resourceName" /> | `string` | Optional. Output only. Name of the resource like //storage.googleapis.com/myprojectxyz-testbucket. Empty for org-policy violations. |
| <CopyableCode code="resourceType" /> | `string` | Optional. Output only. Type of the resource like compute.googleapis.com/Disk, etc. Empty for org-policy violations. |
| <CopyableCode code="state" /> | `string` | Output only. State of the violation |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time when the Violation record was updated. |
| <CopyableCode code="violationType" /> | `string` | Output only. Type of the violation |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, violationsId, workloadsId" /> | Retrieves Assured Workload Violation based on ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId, workloadsId" /> | Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-` |
| <CopyableCode code="acknowledge" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId, violationsId, workloadsId" /> | Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted. |

## `SELECT` examples

Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/{org_id}/locations/{location}/workloads/-`

```sql
SELECT
name,
description,
acknowledged,
acknowledgementTime,
associatedOrgPolicyViolationId,
auditLogLink,
beginTime,
category,
exceptionAuditLogLink,
exceptionContexts,
nonCompliantOrgPolicy,
orgPolicyConstraint,
parentProjectNumber,
remediation,
resolveTime,
resourceName,
resourceType,
state,
updateTime,
violationType
FROM google.assuredworkloads.violations
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}';
```
