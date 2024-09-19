---
title: service_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - service_bindings
  - networkservices
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

Creates, updates, deletes, gets or lists a <code>service_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkservices.service_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the ServiceBinding resource. It matches pattern `projects/*/locations/global/serviceBindings/service_binding_name`. |
| <CopyableCode code="description" /> | `string` | Optional. A free-text description of the resource. Max length 1024 characters. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the resource was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Set of label tags associated with the ServiceBinding resource. |
| <CopyableCode code="service" /> | `string` | Required. The full Service Directory Service name of the format projects/*/locations/*/namespaces/*/services/* |
| <CopyableCode code="serviceId" /> | `string` | Output only. The unique identifier of the Service Directory Service against which the Service Binding resource is validated. This is populated when the Service Binding resource is used in another resource (like Backend Service). This is of the UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the resource was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceBindingsId" /> | Gets details of a single ServiceBinding. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceBinding in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServiceBinding in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceBindingsId" /> | Deletes a single ServiceBinding. |

## `SELECT` examples

Lists ServiceBinding in a given project and location.

```sql
SELECT
name,
description,
createTime,
labels,
service,
serviceId,
updateTime
FROM google.networkservices.service_bindings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_bindings</code> resource.

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
INSERT INTO google.networkservices.service_bindings (
locationsId,
projectsId,
name,
description,
service,
labels
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ service }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: service
      value: string
    - name: serviceId
      value: string
    - name: labels
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>service_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkservices.service_bindings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceBindingsId = '{{ serviceBindingsId }}';
```
