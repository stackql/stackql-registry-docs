---
title: swift_virtual_network_slots
hide_title: false
hide_table_of_contents: false
keywords:
  - swift_virtual_network_slots
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

Creates, updates, deletes, gets or lists a <code>swift_virtual_network_slots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>swift_virtual_network_slots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.swift_virtual_network_slots" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Deletes a Swift Virtual Network connection from an app (or deployment slot). |

## `DELETE` example

Deletes the specified <code>swift_virtual_network_slots</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.swift_virtual_network_slots
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND slot = '{{ slot }}'
AND subscriptionId = '{{ subscriptionId }}';
```
