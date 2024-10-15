---
title: consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - consoles
  - serial_console
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

Creates, updates, deletes, gets or lists a <code>consoles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consoles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.serial_console.consoles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_status" /> | `SELECT` | <CopyableCode code="default, subscriptionId" /> | Gets whether or not Serial Console is disabled for a given subscription |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="default, subscriptionId" /> | Disables the Serial Console service for all VMs and VM scale sets in the provided subscription |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="default, subscriptionId" /> | Enables the Serial Console service for all VMs and VM scale sets in the provided subscription |

## `SELECT` examples

Gets whether or not Serial Console is disabled for a given subscription


```sql
SELECT
properties
FROM azure.serial_console.consoles
WHERE default = '{{ default }}'
AND subscriptionId = '{{ subscriptionId }}';
```