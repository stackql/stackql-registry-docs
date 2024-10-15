---
title: network_features_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - network_features_slots
  - app_service
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

Creates, updates, deletes, gets or lists a <code>network_features_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_features_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.network_features_slots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | NetworkFeatures resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, view" /> | Description for Gets all network features used by the app (or deployment slot, if specified). |

## `SELECT` examples

Description for Gets all network features used by the app (or deployment slot, if specified).


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.network_features_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}'
AND view = '{{ view }}';
```