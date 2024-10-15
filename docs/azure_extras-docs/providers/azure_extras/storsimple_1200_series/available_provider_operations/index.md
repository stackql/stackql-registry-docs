---
title: available_provider_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - available_provider_operations
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>available_provider_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_provider_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.available_provider_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the operation being performed on this particular object
Return value format: "{resourceProviderNamespace}/{resourceType}/{read|write|deletion|action}"
Eg: Microsoft.StorSimple/managers/devices/fileServers/read
    Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. 
These value will be used by several clients for 
(1) custom role definitions for RBAC; 
(2) complex query filters for the event service; and (3) audit history / records for management operations. |
| <CopyableCode code="origin" /> | `string` | Gets or sets Origin
The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX.
Default value is “user,system” |
| <CopyableCode code="properties" /> | `object` | Class represents Properties in AvailableProviderOperations |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | List of AvailableProviderOperations |

## `SELECT` examples

List of AvailableProviderOperations


```sql
SELECT
name,
display,
origin,
properties
FROM azure_extras.storsimple_1200_series.available_provider_operations
;
```