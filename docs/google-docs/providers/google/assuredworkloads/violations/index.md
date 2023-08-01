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
| `nextPageToken` | `string` | The next page token. Returns empty if reached the last page. |
| `violations` | `array` | List of Violations under a Workload. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, organizationsId, violationsId, workloadsId` | Retrieves Assured Workload Violation based on ID. |
| `list` | `SELECT` | `locationsId, organizationsId, workloadsId` | Lists the Violations in the AssuredWorkload Environment. Callers may also choose to read across multiple Workloads as per [AIP-159](https://google.aip.dev/159) by using '-' (the hyphen or dash character) as a wildcard character instead of workload-id in the parent. Format `organizations/&#123;org_id&#125;/locations/&#123;location&#125;/workloads/-` |
| `acknowledge` | `EXEC` | `locationsId, organizationsId, violationsId, workloadsId` | Acknowledges an existing violation. By acknowledging a violation, users acknowledge the existence of a compliance violation in their workload and decide to ignore it due to a valid business justification. Acknowledgement is a permanent operation and it cannot be reverted. |
