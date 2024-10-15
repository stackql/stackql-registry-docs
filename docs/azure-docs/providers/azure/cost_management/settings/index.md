---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Specifies the kind of settings. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_scope" /> | `SELECT` | <CopyableCode code="scope, type" /> | Get the setting from the given scope by name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | List all cost management settings in the requested scope. |
| <CopyableCode code="delete_by_scope" /> | `DELETE` | <CopyableCode code="scope, type" /> | Delete a setting within the given scope. |

## `SELECT` examples

List all cost management settings in the requested scope.


```sql
SELECT
kind
FROM azure.cost_management.settings
WHERE scope = '{{ scope }}';
```
## `DELETE` example

Deletes the specified <code>settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cost_management.settings
WHERE scope = '{{ scope }}'
AND type = '{{ type }}';
```
