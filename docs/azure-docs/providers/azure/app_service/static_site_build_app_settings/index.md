---
title: static_site_build_app_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - static_site_build_app_settings
  - app_service
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

Creates, updates, deletes, gets or lists a <code>static_site_build_app_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>static_site_build_app_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.static_site_build_app_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | Settings. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Description for Gets the application settings of a static site build. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Description for Creates or updates the app settings of a static site build. |

## `SELECT` examples

Description for Gets the application settings of a static site build.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.static_site_build_app_settings
WHERE environmentName = '{{ environmentName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>static_site_build_app_settings</code> resource.

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
INSERT INTO azure.app_service.static_site_build_app_settings (
environmentName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ environmentName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value: object

```
</TabItem>
</Tabs>
