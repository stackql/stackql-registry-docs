---
title: active_connectivity_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - active_connectivity_configurations
  - network
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

Creates, updates, deletes, gets or lists a <code>active_connectivity_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>active_connectivity_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.active_connectivity_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Connectivity configuration ID. |
| <CopyableCode code="commitTime" /> | `string` | Deployment time string. |
| <CopyableCode code="configurationGroups" /> | `array` | Effective configuration groups. |
| <CopyableCode code="properties" /> | `object` | Properties of network manager connectivity configuration |
| <CopyableCode code="region" /> | `string` | Deployment region. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkManagerName, resourceGroupName, subscriptionId" /> | Lists active connectivity configurations in a network manager. |

## `SELECT` examples

Lists active connectivity configurations in a network manager.


```sql
SELECT
id,
commitTime,
configurationGroups,
properties,
region
FROM azure.network.active_connectivity_configurations
WHERE networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```