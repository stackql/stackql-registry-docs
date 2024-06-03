---
title: violations
hide_title: false
hide_table_of_contents: false
keywords:
  - violations
  - cloudcontrolspartner
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
<tr><td><b>Name</b></td><td><code>violations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.violations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;/violations/&#123;violation&#125;` |
| <CopyableCode code="description" /> | `string` | Output only. Description for the Violation. e.g. OrgPolicy gcp.resourceLocations has non compliant value. |
| <CopyableCode code="beginTime" /> | `string` | Output only. Time of the event which triggered the Violation. |
| <CopyableCode code="category" /> | `string` | Output only. Category under which this violation is mapped. e.g. Location, Service Usage, Access, Encryption, etc. |
| <CopyableCode code="folderId" /> | `string` | The folder_id of the violation |
| <CopyableCode code="nonCompliantOrgPolicy" /> | `string` | Output only. Immutable. Name of the OrgPolicy which was modified with non-compliant change and resulted this violation. Format: `projects/&#123;project_number&#125;/policies/&#123;constraint_name&#125;` `folders/&#123;folder_id&#125;/policies/&#123;constraint_name&#125;` `organizations/&#123;organization_id&#125;/policies/&#123;constraint_name&#125;` |
| <CopyableCode code="remediation" /> | `object` | Represents remediation guidance to resolve compliance violation for AssuredWorkload |
| <CopyableCode code="resolveTime" /> | `string` | Output only. Time of the event which fixed the Violation. If the violation is ACTIVE this will be empty. |
| <CopyableCode code="state" /> | `string` | Output only. State of the violation |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last time when the Violation record was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, violationsId, workloadsId" /> | Gets details of a single Violation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of &#123;customer&#125; & &#123;workload&#125;. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;` |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Lists Violations for a workload Callers may also choose to read across multiple Customers or for a single customer as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of &#123;customer&#125; & &#123;workload&#125;. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;` |
