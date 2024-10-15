---
title: operations
hide_title: false
hide_table_of_contents: false
keywords:
  - operations
  - container_service_admin
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.container_service_admin.operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. It should match the action name that appears in RBAC / the event service. |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. |
| <CopyableCode code="isDataAction" /> | `boolean` | Indicates whether the operation is a data action |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Get the list of supported admin container service rest operations. |

## `SELECT` examples

Get the list of supported admin container service rest operations.


```sql
SELECT
name,
display,
isDataAction
FROM azure_stack.container_service_admin.operations
;
```