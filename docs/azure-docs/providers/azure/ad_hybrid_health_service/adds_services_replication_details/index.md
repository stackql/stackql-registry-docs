---
title: adds_services_replication_details
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_replication_details
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

Creates, updates, deletes, gets or lists a <code>adds_services_replication_details</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_replication_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_replication_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domain" /> | `string` | The domain name for a given domain controller. |
| <CopyableCode code="inboundNeighborCollection" /> | `array` | List of individual domain controller neighbor's inbound replication status. |
| <CopyableCode code="lastAttemptedSync" /> | `string` | The last time when a sync was attempted for a given domain controller. |
| <CopyableCode code="lastSuccessfulSync" /> | `string` | The time when the last successful sync happened for a given domain controller. |
| <CopyableCode code="site" /> | `string` | The site name for a given domain controller. |
| <CopyableCode code="status" /> | `integer` | The health status for a domain controller. |
| <CopyableCode code="targetServer" /> | `string` | The domain controller name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |

## `SELECT` examples

Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.


```sql
SELECT
domain,
inboundNeighborCollection,
lastAttemptedSync,
lastSuccessfulSync,
site,
status,
targetServer
FROM azure.ad_hybrid_health_service.adds_services_replication_details
WHERE serviceName = '{{ serviceName }}';
```