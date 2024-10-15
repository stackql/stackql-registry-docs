---
title: outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_network_dependencies_endpoints
  - api_management
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

Creates, updates, deletes, gets or lists a <code>outbound_network_dependencies_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The type of service accessed by the Api Management Service, e.g., Azure Storage, Azure SQL Database, and Azure Active Directory. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints that the Api Management Service reaches the service at. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets the network endpoints of all outbound dependencies of a ApiManagement service. |

## `SELECT` examples

Gets the network endpoints of all outbound dependencies of a ApiManagement service.


```sql
SELECT
category,
endpoints
FROM azure.api_management.outbound_network_dependencies_endpoints
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```