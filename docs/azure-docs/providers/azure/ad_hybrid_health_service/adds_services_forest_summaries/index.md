---
title: adds_services_forest_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_forest_summaries
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

Creates, updates, deletes, gets or lists a <code>adds_services_forest_summaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_forest_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_forest_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domainCount" /> | `integer` | The domain count. |
| <CopyableCode code="domains" /> | `array` | The list of domain controller names. |
| <CopyableCode code="forestName" /> | `string` | The forest name. |
| <CopyableCode code="monitoredDcCount" /> | `integer` | The number of domain controllers that are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="siteCount" /> | `integer` | The site count. |
| <CopyableCode code="sites" /> | `array` | The list of site names. |
| <CopyableCode code="totalDcCount" /> | `integer` | The total domain controllers. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |

## `SELECT` examples

Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.


```sql
SELECT
domainCount,
domains,
forestName,
monitoredDcCount,
siteCount,
sites,
totalDcCount
FROM azure.ad_hybrid_health_service.adds_services_forest_summaries
WHERE serviceName = '{{ serviceName }}';
```