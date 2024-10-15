---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - web_pubsub
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the operation with format: {provider}/{resource}/{operation} |
| <CopyableCode code="display" /> | `object` | The object that describes a operation. |
| <CopyableCode code="isDataAction" /> | `boolean` | If the operation is a data action. (for data plane rbac) |
| <CopyableCode code="origin" /> | `string` | Optional. The intended executor of the operation; governs the display of the operation in the RBAC UX and the audit logs UX. |
| <CopyableCode code="properties" /> | `object` | Extra Operation properties. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists all of the available REST API operations of the Microsoft.SignalRService provider. |

## `SELECT` examples

Lists all of the available REST API operations of the Microsoft.SignalRService provider.


```sql
SELECT
name,
display,
isDataAction,
origin,
properties
FROM azure.web_pubsub.operations
;
```