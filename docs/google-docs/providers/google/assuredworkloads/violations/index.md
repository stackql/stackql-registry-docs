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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>violations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.assuredworkloads.violations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Immutable. Name of the Violation. Format: organizations/&#123;organization&#125;/locations/&#123;location&#125;/workloads/&#123;workload_id&#125;/violations/&#123;violations_id&#125; |
| `description` | `string` | Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value. |
| `acknowledgementTime` | `string` | Optional. Timestamp when this violation was acknowledged last. This will be absent when acknowledged field is marked as false. |
| `orgPolicyConstraint` | `string` | Output only. Immutable. The org-policy-constraint that was incorrectly changed, which resulted in this violation. |
| `resolveTime` | `string` | Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty. |
| `updateTime` | `string` | Output only. The last time when the Violation record was updated. |
| `exceptionAuditLogLink` | `string` | Output only. Immutable. Audit Log link to find business justification provided for violation exception. Format: https://console.cloud.google.com/logs/query;query=&#123;logName&#125;&#123;protoPayload.resourceName&#125;&#123;protoPayload.methodName&#125;&#123;timeRange&#125;&#123;organization&#125; |
| `auditLogLink` | `string` | Output only. Immutable. Audit Log Link for violated resource Format: https://console.cloud.google.com/logs/query;query=&#123;logName&#125;&#123;protoPayload.resourceName&#125;&#123;timeRange&#125;&#123;folder&#125; |
| `acknowledged` | `boolean` | A boolean that indicates if the violation is acknowledged |
| `nonCompliantOrgPolicy` | `string` | Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: projects/&#123;project_number&#125;/policies/&#123;constraint_name&#125; folders/&#123;folder_id&#125;/policies/&#123;constraint_name&#125; organizations/&#123;organization_id&#125;/policies/&#123;constraint_name&#125; |
| `beginTime` | `string` | Output only. Time of the event which triggered the Violation. |
| `state` | `string` | Output only. State of the violation |
| `category` | `string` | Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc. |
| `remediation` | `object` | Represents remediation guidance to resolve compliance violation for AssuredWorkload |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_workloads_violations_get` | `SELECT` | `locationsId, organizationsId, violationsId, workloadsId` | Retrieves Assured Workload Violation based on ID. |
| `organizations_locations_workloads_violations_list` | `SELECT` | `locationsId, organizationsId, workloadsId` | Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/&#123;org_id&#125;/locations/&#123;location&#125;/workloads/-` |
| `organizations_locations_workloads_violations_acknowledge` | `EXEC` | `locationsId, organizationsId, violationsId, workloadsId` | Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted. |
