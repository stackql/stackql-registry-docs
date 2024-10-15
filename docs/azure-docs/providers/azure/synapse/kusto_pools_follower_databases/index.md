---
title: kusto_pools_follower_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pools_follower_databases
  - synapse
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

Creates, updates, deletes, gets or lists a <code>kusto_pools_follower_databases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kusto_pools_follower_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.kusto_pools_follower_databases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="attachedDatabaseConfigurationName" /> | `string` | Resource name of the attached database configuration in the follower cluster. |
| <CopyableCode code="clusterResourceId" /> | `string` | Resource id of the cluster that follows a database owned by this cluster. |
| <CopyableCode code="databaseName" /> | `string` | The database name owned by this cluster that was followed. * in case following all databases. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="kustoPoolName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool. |

## `SELECT` examples

Returns a list of databases that are owned by this Kusto Pool and were followed by another Kusto Pool.


```sql
SELECT
attachedDatabaseConfigurationName,
clusterResourceId,
databaseName
FROM azure.synapse.kusto_pools_follower_databases
WHERE kustoPoolName = '{{ kustoPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```