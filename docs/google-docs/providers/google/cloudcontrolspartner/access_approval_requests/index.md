---
title: access_approval_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - access_approval_requests
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
<tr><td><b>Name</b></td><td><code>access_approval_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.access_approval_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/&#123;organization&#125;/locations/&#123;location&#125;/customers/&#123;customer&#125;/workloads/&#123;workload&#125;/accessApprovalRequests/&#123;access_approval_request&#125;` |
| <CopyableCode code="requestTime" /> | `string` | The time at which approval was requested. |
| <CopyableCode code="requestedExpirationTime" /> | `string` | The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. |
| <CopyableCode code="requestedReason" /> | `object` | Reason for the access. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> |
