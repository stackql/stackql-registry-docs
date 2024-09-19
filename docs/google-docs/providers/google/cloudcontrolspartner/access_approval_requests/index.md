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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>access_approval_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_approval_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.access_approval_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/accessApprovalRequests/{access_approval_request}` |
| <CopyableCode code="requestTime" /> | `string` | The time at which approval was requested. |
| <CopyableCode code="requestedExpirationTime" /> | `string` | The requested expiration for the approval. If the request is approved, access will be granted from the time of approval until the expiration time. |
| <CopyableCode code="requestedReason" /> | `object` | Reason for the access. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId, workloadsId" /> | Deprecated: Only returns access approval requests directly associated with an assured workload folder. |

## `SELECT` examples

Deprecated: Only returns access approval requests directly associated with an assured workload folder.

```sql
SELECT
name,
requestTime,
requestedExpirationTime,
requestedReason
FROM google.cloudcontrolspartner.access_approval_requests
WHERE customersId = '{{ customersId }}'
AND locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'
AND workloadsId = '{{ workloadsId }}';
```
