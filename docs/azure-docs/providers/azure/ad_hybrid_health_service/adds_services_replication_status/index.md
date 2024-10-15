---
title: adds_services_replication_status
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_replication_status
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

Creates, updates, deletes, gets or lists a <code>adds_services_replication_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_replication_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_replication_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="errorDcCount" /> | `integer` | The total number of domain controllers with error in a given forest. |
| <CopyableCode code="forestName" /> | `string` | The forest name. |
| <CopyableCode code="totalDcCount" /> | `integer` | The total number of domain controllers for a given forest. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets Replication status for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |

## `SELECT` examples

Gets Replication status for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.


```sql
SELECT
errorDcCount,
forestName,
totalDcCount
FROM azure.ad_hybrid_health_service.adds_services_replication_status
WHERE serviceName = '{{ serviceName }}';
```