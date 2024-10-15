---
title: watchers_available_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_available_providers
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

Creates, updates, deletes, gets or lists a <code>watchers_available_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_available_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_available_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="countries" /> | `array` | List of available countries. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId" /> | NOTE: This feature is currently in preview and still being tested for stability. Lists all available internet service providers for a specified Azure region. |

## `SELECT` examples

NOTE: This feature is currently in preview and still being tested for stability. Lists all available internet service providers for a specified Azure region.


```sql
SELECT
countries
FROM azure.network.watchers_available_providers
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```