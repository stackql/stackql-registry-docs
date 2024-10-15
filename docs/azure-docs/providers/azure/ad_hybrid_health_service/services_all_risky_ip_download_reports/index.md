---
title: services_all_risky_ip_download_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - services_all_risky_ip_download_reports
  - ad_hybrid_health_service
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

Creates, updates, deletes, gets or lists a <code>services_all_risky_ip_download_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_all_risky_ip_download_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services_all_risky_ip_download_reports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="blobCreateDateTime" /> | `string` | Time at which the new Risky IP report was requested. |
| <CopyableCode code="jobCompletionTime" /> | `string` | Time at which the blob creation job for the new Risky IP report was completed. |
| <CopyableCode code="resultSasUri" /> | `string` | The blob uri for the report. |
| <CopyableCode code="serviceId" /> | `string` | The service id for whom the report belongs to. |
| <CopyableCode code="status" /> | `string` | Status of the Risky IP report generation. |
| <CopyableCode code="tenantId" /> | `string` | The tenant id for whom the report belongs to. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets all Risky IP report URIs for the last 7 days. |

## `SELECT` examples

Gets all Risky IP report URIs for the last 7 days.


```sql
SELECT
blobCreateDateTime,
jobCompletionTime,
resultSasUri,
serviceId,
status,
tenantId
FROM azure.ad_hybrid_health_service.services_all_risky_ip_download_reports
WHERE serviceName = '{{ serviceName }}';
```