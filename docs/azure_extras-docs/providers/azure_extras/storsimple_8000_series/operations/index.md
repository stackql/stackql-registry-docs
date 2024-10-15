---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on a particular object. Name format: "{resourceProviderNamespace}/{resourceType}/{read|write|delete|action}". Eg. Microsoft.StorSimple/managers/devices/volumeContainers/read, Microsoft.StorSimple/managers/devices/alerts/clearAlerts/action |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation/action. These value will be used by several clients for (a) custom role definitions for RBAC, (b) complex query filters for the event service and (c) audit history/records for management operations. |
| <CopyableCode code="origin" /> | `string` | The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. Default value is "user,system" |
| <CopyableCode code="properties" /> | `object` | Represents properties of AvailableProviderOperation |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available REST API operations of the Microsoft.StorSimple provider |

## `SELECT` examples

Lists all of the available REST API operations of the Microsoft.StorSimple provider


```sql
SELECT
name,
display,
origin,
properties
FROM azure_extras.storsimple_8000_series.operations
;
```