---
title: data_controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_controllers
  - azure_arc_data
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

Creates, updates, deletes, gets or lists a <code>data_controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_arc_data.data_controllers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The data controller properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_in_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_in_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="patch_data_controller" /> | `EXEC` | <CopyableCode code="dataControllerName, resourceGroupName, subscriptionId" /> | Updates a dataController resource |
| <CopyableCode code="put_data_controller" /> | `EXEC` | <CopyableCode code="dataControllerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or replaces a dataController resource |

## `SELECT` examples




```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.azure_arc_data.data_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```