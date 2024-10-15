---
title: guest_agents_by_virtual_machine_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - guest_agents_by_virtual_machine_instances
  - system_center_vm_manager
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

Creates, updates, deletes, gets or lists a <code>guest_agents_by_virtual_machine_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>guest_agents_by_virtual_machine_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.guest_agents_by_virtual_machine_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | Returns the list of GuestAgent of the given vm. |

## `SELECT` examples

Returns the list of GuestAgent of the given vm.


```sql
SELECT
properties
FROM azure.system_center_vm_manager.guest_agents_by_virtual_machine_instances
WHERE resourceUri = '{{ resourceUri }}';
```