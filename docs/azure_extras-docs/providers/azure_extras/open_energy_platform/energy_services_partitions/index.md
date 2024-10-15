---
title: energy_services_partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - energy_services_partitions
  - open_energy_platform
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

Creates, updates, deletes, gets or lists a <code>energy_services_partitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>energy_services_partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.open_energy_platform.energy_services_partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataPartitionInfo" /> | `array` | List of data partitions along with their properties in a given OEP resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Method that gets called when list of partitions is requested. |

## `SELECT` examples

Method that gets called when list of partitions is requested.


```sql
SELECT
dataPartitionInfo
FROM azure_extras.open_energy_platform.energy_services_partitions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```