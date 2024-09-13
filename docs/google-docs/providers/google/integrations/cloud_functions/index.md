---
title: cloud_functions
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_functions
  - integrations
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

Creates, updates, deletes, gets or lists a <code>cloud_functions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_functions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.cloud_functions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_cloud_functions_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a cloud function project. |
| <CopyableCode code="projects_locations_products_cloud_functions_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates a cloud function project. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_functions</code> resource.

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
INSERT INTO google.integrations.cloud_functions (
locationsId,
projectsId,
projectId,
functionRegion,
functionName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ projectId }}',
'{{ functionRegion }}',
'{{ functionName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: projectId
        value: '{{ projectId }}'
      - name: functionRegion
        value: '{{ functionRegion }}'
      - name: functionName
        value: '{{ functionName }}'

```
</TabItem>
</Tabs>
