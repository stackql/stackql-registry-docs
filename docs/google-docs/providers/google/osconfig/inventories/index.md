---
title: inventories
hide_title: false
hide_table_of_contents: false
keywords:
  - inventories
  - osconfig
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

Creates, updates, deletes or gets an <code>inventory</code> resource or lists <code>inventories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inventories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.osconfig.inventories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The `Inventory` API resource name. Format: `projects/{project_number}/locations/{location}/instances/{instance_id}/inventory` |
| <CopyableCode code="items" /> | `object` | Inventory items related to the VM keyed by an opaque unique identifier for each inventory item. The identifier is unique to each distinct and addressable inventory item and will change, when there is a new package version. |
| <CopyableCode code="osInfo" /> | `object` | Operating system information for the VM. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp of the last reported inventory for the VM. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | List inventory data for all VM instances in the specified zone. |

## `SELECT` examples

List inventory data for all VM instances in the specified zone.

```sql
SELECT
name,
items,
osInfo,
updateTime
FROM google.osconfig.inventories
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
