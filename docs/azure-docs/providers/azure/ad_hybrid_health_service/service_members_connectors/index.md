---
title: service_members_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members_connectors
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

Creates, updates, deletes, gets or lists a <code>service_members_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members_connectors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The connector Id. |
| <CopyableCode code="name" /> | `string` | The connector name. |
| <CopyableCode code="description" /> | `string` | The connector description. |
| <CopyableCode code="attributesIncluded" /> | `array` | The attribute inclusion list of the connector. |
| <CopyableCode code="classesIncluded" /> | `array` | The class inclusion list of the connector. |
| <CopyableCode code="connectorId" /> | `string` | The connector Id. |
| <CopyableCode code="partitions" /> | `array` | The partitions of the connector. |
| <CopyableCode code="passwordHashSyncConfiguration" /> | `object` | The password hash synchronization configuration of the connector. |
| <CopyableCode code="passwordManagementSettings" /> | `object` | The password management settings of the connector. |
| <CopyableCode code="runProfiles" /> | `array` | The run profiles of the connector. |
| <CopyableCode code="schemaXml" /> | `string` | The schema xml for the connector. |
| <CopyableCode code="timeCreated" /> | `string` | The date and time when this connector was created. |
| <CopyableCode code="timeLastModified" /> | `string` | The date and time when this connector was last modified. |
| <CopyableCode code="type" /> | `string` | The connector type. |
| <CopyableCode code="version" /> | `integer` | The connector version |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the connector details for a service. |

## `SELECT` examples

Gets the connector details for a service.


```sql
SELECT
id,
name,
description,
attributesIncluded,
classesIncluded,
connectorId,
partitions,
passwordHashSyncConfiguration,
passwordManagementSettings,
runProfiles,
schemaXml,
timeCreated,
timeLastModified,
type,
version
FROM azure.ad_hybrid_health_service.service_members_connectors
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```