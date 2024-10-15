---
title: service_available_skus_by_resource_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - service_available_skus_by_resource_groups
  - data_box
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

Creates, updates, deletes, gets or lists a <code>service_available_skus_by_resource_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_available_skus_by_resource_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.service_available_skus_by_resource_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `boolean` | The sku is enabled or not. |
| <CopyableCode code="properties" /> | `object` | Properties of the sku. |
| <CopyableCode code="sku" /> | `object` | The Sku. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__country, data__location, data__transferType" /> | This method provides the list of available skus for the given subscription, resource group and location. |

## `SELECT` examples

This method provides the list of available skus for the given subscription, resource group and location.


```sql
SELECT
enabled,
properties,
sku
FROM azure.data_box.service_available_skus_by_resource_groups
WHERE location = '{{ location }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__country = '{{ data__country }}'
AND data__location = '{{ data__location }}'
AND data__transferType = '{{ data__transferType }}';
```