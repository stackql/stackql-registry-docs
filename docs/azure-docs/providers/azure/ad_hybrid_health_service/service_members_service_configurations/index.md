---
title: service_members_service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_service_configurations
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

Creates, updates, deletes, gets or lists a <code>service_members_service_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_service_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_service_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="serviceAccount" /> | `string` | The service account. |
| <CopyableCode code="serviceType" /> | `integer` | The service type of the server. |
| <CopyableCode code="sqlDatabaseName" /> | `string` | The SQL database. |
| <CopyableCode code="sqlDatabaseSize" /> | `integer` | The SQL database size. |
| <CopyableCode code="sqlEdition" /> | `string` | The SQL edition |
| <CopyableCode code="sqlInstance" /> | `string` | The SQL instance details. |
| <CopyableCode code="sqlServer" /> | `string` | The SQL server information. |
| <CopyableCode code="sqlVersion" /> | `string` | The SQL version. |
| <CopyableCode code="version" /> | `string` | The version of the sync service. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the service configuration. |

## `SELECT` examples

Gets the service configuration.


```sql
SELECT
serviceAccount,
serviceType,
sqlDatabaseName,
sqlDatabaseSize,
sqlEdition,
sqlInstance,
sqlServer,
sqlVersion,
version
FROM azure.ad_hybrid_health_service.service_members_service_configurations
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```