---
title: serving_configs_control
hide_title: false
hide_table_of_contents: false
keywords:
  - serving_configs_control
  - retail
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

Creates, updates, deletes, gets or lists a <code>serving_configs_control</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>serving_configs_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.serving_configs_control" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_serving_configs_add_control" /> | `INSERT` | <CopyableCode code="catalogsId, locationsId, projectsId, servingConfigsId" /> | Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control. |
| <CopyableCode code="projects_locations_catalogs_serving_configs_remove_control" /> | `DELETE` | <CopyableCode code="catalogsId, locationsId, projectsId, servingConfigsId" /> | Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>serving_configs_control</code> resource.

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
INSERT INTO google.retail.serving_configs_control (
catalogsId,
locationsId,
projectsId,
servingConfigsId,
controlId
)
SELECT 
'{{ catalogsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ servingConfigsId }}',
'{{ controlId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: controlId
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>serving_configs_control</code> resource.

```sql
/*+ delete */
DELETE FROM google.retail.serving_configs_control
WHERE catalogsId = '{{ catalogsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servingConfigsId = '{{ servingConfigsId }}';
```
