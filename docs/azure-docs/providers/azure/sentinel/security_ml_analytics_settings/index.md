---
title: security_ml_analytics_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_ml_analytics_settings
  - sentinel
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

Creates, updates, deletes, gets or lists a <code>security_ml_analytics_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_ml_analytics_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.security_ml_analytics_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of security ML analytics settings |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName" /> | Gets the Security ML Analytics Settings. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all Security ML Analytics Settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName, data__kind" /> | Creates or updates the Security ML Analytics Settings. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName" /> | Delete the Security ML Analytics Settings. |

## `SELECT` examples

Gets all Security ML Analytics Settings.


```sql
SELECT
etag,
kind
FROM azure.sentinel.security_ml_analytics_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_ml_analytics_settings</code> resource.

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
INSERT INTO azure.sentinel.security_ml_analytics_settings (
resourceGroupName,
settingsResourceName,
subscriptionId,
workspaceName,
data__kind,
etag,
kind
)
SELECT 
'{{ resourceGroupName }}',
'{{ settingsResourceName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__kind }}',
'{{ etag }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: kind
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>security_ml_analytics_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sentinel.security_ml_analytics_settings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND settingsResourceName = '{{ settingsResourceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
