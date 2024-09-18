---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
  - apigeeregistry
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

Creates, updates, deletes, gets or lists a <code>instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Format: `projects/*/locations/*/instance`. Currently only `locations/global` is supported. |
| <CopyableCode code="build" /> | `object` | Build information of the Instance if it's in `ACTIVE` state. |
| <CopyableCode code="config" /> | `object` | Available configurations to provision an Instance. |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation timestamp. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the Instance. |
| <CopyableCode code="stateMessage" /> | `string` | Output only. Extra information of Instance.State if the state is `FAILED`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update timestamp. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_instances_get" /> | `SELECT` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Gets details of a single Instance. |
| <CopyableCode code="projects_locations_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Provisions instance resources for the Registry. |
| <CopyableCode code="projects_locations_instances_delete" /> | `DELETE` | <CopyableCode code="instancesId, locationsId, projectsId" /> | Deletes the Registry instance. |

## `SELECT` examples

Gets details of a single Instance.

```sql
SELECT
name,
build,
config,
createTime,
state,
stateMessage,
updateTime
FROM google.apigeeregistry.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instances</code> resource.

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
INSERT INTO google.apigeeregistry.instances (
locationsId,
projectsId,
name,
config
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ config }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
state: string
stateMessage: string
config:
  location: string
  cmekKeyName: string
build:
  repo: string
  commitId: string
  commitTime: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.instances
WHERE instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
