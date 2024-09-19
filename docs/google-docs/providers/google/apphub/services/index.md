---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - apphub
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apphub.services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of a Service. Format: "projects/{host-project-id}/locations/{location}/applications/{application-id}/services/{service-id}" |
| <CopyableCode code="description" /> | `string` | Optional. User-defined description of a Service. Can have a maximum length of 2048 characters. |
| <CopyableCode code="attributes" /> | `object` | Consumer provided attributes. |
| <CopyableCode code="createTime" /> | `string` | Output only. Create time. |
| <CopyableCode code="discoveredService" /> | `string` | Required. Immutable. The resource name of the original discovered service. |
| <CopyableCode code="displayName" /> | `string` | Optional. User-defined name for the Service. Can have a maximum length of 63 characters. |
| <CopyableCode code="serviceProperties" /> | `object` | Properties of an underlying cloud resource that can comprise a Service. |
| <CopyableCode code="serviceReference" /> | `object` | Reference to an underlying networking resource that can comprise a Service. |
| <CopyableCode code="state" /> | `string` | Output only. Service state. |
| <CopyableCode code="uid" /> | `string` | Output only. A universally unique identifier (UUID) for the `Service` in the UUID4 format. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Update time. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Gets a Service in an Application. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Lists Services in an Application. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="applicationsId, locationsId, projectsId" /> | Creates a Service in an Application. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Deletes a Service from an Application. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="applicationsId, locationsId, projectsId, servicesId" /> | Updates a Service in an Application. |

## `SELECT` examples

Lists Services in an Application.

```sql
SELECT
name,
description,
attributes,
createTime,
discoveredService,
displayName,
serviceProperties,
serviceReference,
state,
uid,
updateTime
FROM google.apphub.services
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>services</code> resource.

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
INSERT INTO google.apphub.services (
applicationsId,
locationsId,
projectsId,
name,
displayName,
description,
attributes,
discoveredService
)
SELECT 
'{{ applicationsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ attributes }}',
'{{ discoveredService }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
    - name: serviceReference
      value:
        - name: uri
          value: string
    - name: serviceProperties
      value:
        - name: gcpProject
          value: string
        - name: location
          value: string
        - name: zone
          value: string
    - name: attributes
      value:
        - name: criticality
          value:
            - name: type
              value: string
        - name: environment
          value:
            - name: type
              value: string
        - name: developerOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
        - name: operatorOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
        - name: businessOwners
          value:
            - - name: displayName
                value: string
              - name: email
                value: string
    - name: discoveredService
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: uid
      value: string
    - name: state
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE google.apphub.services
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
attributes = '{{ attributes }}',
discoveredService = '{{ discoveredService }}'
WHERE 
applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM google.apphub.services
WHERE applicationsId = '{{ applicationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
