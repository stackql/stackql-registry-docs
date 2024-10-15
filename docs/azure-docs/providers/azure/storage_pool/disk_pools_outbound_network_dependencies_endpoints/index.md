---
title: disk_pools_outbound_network_dependencies_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_pools_outbound_network_dependencies_endpoints
  - storage_pool
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

Creates, updates, deletes, gets or lists a <code>disk_pools_outbound_network_dependencies_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disk_pools_outbound_network_dependencies_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_pool.disk_pools_outbound_network_dependencies_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="category" /> | `string` | The type of service accessed by the App Service Environment, e.g., Azure Storage, Azure SQL Database, and Azure Active Directory. |
| <CopyableCode code="endpoints" /> | `array` | The endpoints that the App Service Environment reaches the service at. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="diskPoolName, resourceGroupName, subscriptionId" /> | Gets the network endpoints of all outbound dependencies of a Disk Pool |

## `SELECT` examples

Gets the network endpoints of all outbound dependencies of a Disk Pool


```sql
SELECT
category,
endpoints
FROM azure.storage_pool.disk_pools_outbound_network_dependencies_endpoints
WHERE diskPoolName = '{{ diskPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```