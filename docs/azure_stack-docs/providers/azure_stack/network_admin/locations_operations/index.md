---
title: locations_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_operations
  - network_admin
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

Creates, updates, deletes, gets or lists a <code>locations_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.network_admin.locations_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the operation being performed on this particular object. This name should match the name that appears in RBAC or the event service. |
| <CopyableCode code="display" /> | `object` | Contains the localized display information for this particular operation / action. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location" /> | Returns the list of support REST operations. |

## `SELECT` examples

Returns the list of support REST operations.


```sql
SELECT
name,
display
FROM azure_stack.network_admin.locations_operations
WHERE location = '{{ location }}';
```