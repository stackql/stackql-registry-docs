---
title: spacecrafts_available_contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts_available_contacts
  - orbital
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

Creates, updates, deletes, gets or lists a <code>spacecrafts_available_contacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spacecrafts_available_contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.spacecrafts_available_contacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="groundStationName" /> | `string` | Name of Azure Ground Station. |
| <CopyableCode code="properties" /> | `object` | Properties of Contact resource. |
| <CopyableCode code="spacecraft" /> | `object` | The reference to the spacecraft resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId, data__contactProfile, data__endTime, data__groundStationName, data__startTime" /> | Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile. |

## `SELECT` examples

Returns list of available contacts. A contact is available if the spacecraft is visible from the ground station for more than the minimum viable contact duration provided in the contact profile.


```sql
SELECT
groundStationName,
properties,
spacecraft
FROM azure.orbital.spacecrafts_available_contacts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spacecraftName = '{{ spacecraftName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__contactProfile = '{{ data__contactProfile }}'
AND data__endTime = '{{ data__endTime }}'
AND data__groundStationName = '{{ data__groundStationName }}'
AND data__startTime = '{{ data__startTime }}';
```