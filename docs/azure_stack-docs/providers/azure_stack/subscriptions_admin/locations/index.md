---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - subscriptions_admin
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Location identifier. |
| <CopyableCode code="name" /> | `string` | Location name. |
| <CopyableCode code="displayName" /> | `string` | Display name of the location. |
| <CopyableCode code="latitude" /> | `string` | Latitude of the location. |
| <CopyableCode code="longitude" /> | `string` | Longitude of the location. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Get the specified location. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get a list of all AzureStack location. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="location, subscriptionId" /> | Updates the specified location. |

## `SELECT` examples

Get a list of all AzureStack location.


```sql
SELECT
id,
name,
displayName,
latitude,
longitude
FROM azure_stack.subscriptions_admin.locations
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>locations</code> resource.

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
INSERT INTO azure_stack.subscriptions_admin.locations (
location,
subscriptionId,
displayName,
id,
latitude,
longitude,
name
)
SELECT 
'{{ location }}',
'{{ subscriptionId }}',
'{{ displayName }}',
'{{ id }}',
'{{ latitude }}',
'{{ longitude }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: id
      value: string
    - name: latitude
      value: string
    - name: longitude
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>
