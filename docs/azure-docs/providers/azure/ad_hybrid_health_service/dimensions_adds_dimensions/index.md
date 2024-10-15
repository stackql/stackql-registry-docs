---
title: dimensions_adds_dimensions
hide_title: false
hide_table_of_contents: false
keywords:
  - dimensions_adds_dimensions
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

Creates, updates, deletes, gets or lists a <code>dimensions_adds_dimensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dimensions_adds_dimensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.dimensions_adds_dimensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeAlerts" /> | `integer` | The count of alerts that are currently active for the service. |
| <CopyableCode code="additionalInformation" /> | `string` | The additional information related to the service. |
| <CopyableCode code="displayName" /> | `string` | The display name of the service. |
| <CopyableCode code="health" /> | `string` | The health status for the domain controller. |
| <CopyableCode code="lastUpdated" /> | `string` | The date or time , in UTC, when the service properties were last updated. |
| <CopyableCode code="resolvedAlerts" /> | `integer` | The total count of alerts that has been resolved for the service. |
| <CopyableCode code="signature" /> | `string` | The signature of the service. |
| <CopyableCode code="simpleProperties" /> | `object` | List of service specific configuration properties. |
| <CopyableCode code="type" /> | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dimension, serviceName" /> | Gets the dimensions for a given dimension type in a server. |

## `SELECT` examples

Gets the dimensions for a given dimension type in a server.


```sql
SELECT
activeAlerts,
additionalInformation,
displayName,
health,
lastUpdated,
resolvedAlerts,
signature,
simpleProperties,
type
FROM azure.ad_hybrid_health_service.dimensions_adds_dimensions
WHERE dimension = '{{ dimension }}'
AND serviceName = '{{ serviceName }}';
```