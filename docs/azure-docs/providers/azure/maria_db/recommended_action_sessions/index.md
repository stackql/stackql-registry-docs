---
title: recommended_action_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_action_sessions
  - maria_db
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

Creates, updates, deletes, gets or lists a <code>recommended_action_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommended_action_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.recommended_action_sessions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="advisorName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Create recommendation action session for the advisor. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>recommended_action_sessions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.maria_db.recommended_action_sessions (
advisorName,
databaseName,
resourceGroupName,
serverName,
subscriptionId
)
SELECT 
'{{ advisorName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>
