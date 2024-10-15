---
title: location_based_performance_tiers
hide_title: false
hide_table_of_contents: false
keywords:
  - location_based_performance_tiers
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>location_based_performance_tiers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_based_performance_tiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.location_based_performance_tiers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the performance tier. |
| <CopyableCode code="maxBackupRetentionDays" /> | `integer` | Maximum Backup retention in days for the performance tier edition |
| <CopyableCode code="maxLargeStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="maxStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="minBackupRetentionDays" /> | `integer` | Minimum Backup retention in days for the performance tier edition |
| <CopyableCode code="minLargeStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="minStorageMB" /> | `integer` | Max storage allowed for a server. |
| <CopyableCode code="serviceLevelObjectives" /> | `array` | Service level objectives associated with the performance tier |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationName, subscriptionId" /> | List all the performance tiers at specified location in a given subscription. |

## `SELECT` examples

List all the performance tiers at specified location in a given subscription.


```sql
SELECT
id,
maxBackupRetentionDays,
maxLargeStorageMB,
maxStorageMB,
minBackupRetentionDays,
minLargeStorageMB,
minStorageMB,
serviceLevelObjectives
FROM azure.maria_db.location_based_performance_tiers
WHERE locationName = '{{ locationName }}'
AND subscriptionId = '{{ subscriptionId }}';
```