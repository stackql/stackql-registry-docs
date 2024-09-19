---
title: sfdc_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sfdc_instances
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

Creates, updates, deletes, gets or lists a <code>sfdc_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sfdc_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.integrations.sfdc_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name of the SFDC instance projects/{project}/locations/{location}/sfdcInstances/{sfdcInstance}. |
| <CopyableCode code="description" /> | `string` | A description of the sfdc instance. |
| <CopyableCode code="authConfigId" /> | `array` | A list of AuthConfigs that can be tried to open the channel to SFDC |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the instance is created |
| <CopyableCode code="deleteTime" /> | `string` | Output only. Time when the instance was deleted. Empty if not deleted. |
| <CopyableCode code="displayName" /> | `string` | User selected unique name/alias to easily reference an instance. |
| <CopyableCode code="serviceAuthority" /> | `string` | URL used for API calls after authentication (the login authority is configured within the referenced AuthConfig). |
| <CopyableCode code="sfdcOrgId" /> | `string` | The SFDC Org Id. This is defined in salesforce. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the instance was last updated |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_products_sfdc_instances_get" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| <CopyableCode code="projects_locations_products_sfdc_instances_list" /> | `SELECT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="projects_locations_sfdc_instances_get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Gets an sfdc instance. If the instance doesn't exist, Code.NOT_FOUND exception will be thrown. |
| <CopyableCode code="projects_locations_sfdc_instances_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only. |
| <CopyableCode code="projects_locations_products_sfdc_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, productsId, projectsId" /> | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an sfdc instance record. Store the sfdc instance in Spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_products_sfdc_instances_delete" /> | `DELETE` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Deletes an sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Deletes an sfdc instance. |
| <CopyableCode code="projects_locations_products_sfdc_instances_patch" /> | `UPDATE` | <CopyableCode code="locationsId, productsId, projectsId, sfdcInstancesId" /> | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |
| <CopyableCode code="projects_locations_sfdc_instances_patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, sfdcInstancesId" /> | Updates an sfdc instance. Updates the sfdc instance in spanner. Returns the sfdc instance. |

## `SELECT` examples

Lists all sfdc instances that match the filter. Restrict to sfdc instances belonging to the current client only.

```sql
SELECT
name,
description,
authConfigId,
createTime,
deleteTime,
displayName,
serviceAuthority,
sfdcOrgId,
updateTime
FROM google.integrations.sfdc_instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sfdc_instances</code> resource.

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
INSERT INTO google.integrations.sfdc_instances (
locationsId,
projectsId,
sfdcOrgId,
serviceAuthority,
authConfigId,
displayName,
name,
description
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ sfdcOrgId }}',
'{{ serviceAuthority }}',
'{{ authConfigId }}',
'{{ displayName }}',
'{{ name }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sfdcOrgId
      value: string
    - name: serviceAuthority
      value: string
    - name: authConfigId
      value:
        - string
    - name: deleteTime
      value: string
    - name: updateTime
      value: string
    - name: displayName
      value: string
    - name: createTime
      value: string
    - name: name
      value: string
    - name: description
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>sfdc_instances</code> resource.

```sql
/*+ update */
UPDATE google.integrations.sfdc_instances
SET 
sfdcOrgId = '{{ sfdcOrgId }}',
serviceAuthority = '{{ serviceAuthority }}',
authConfigId = '{{ authConfigId }}',
displayName = '{{ displayName }}',
name = '{{ name }}',
description = '{{ description }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sfdcInstancesId = '{{ sfdcInstancesId }}';
```

## `DELETE` example

Deletes the specified <code>sfdc_instances</code> resource.

```sql
/*+ delete */
DELETE FROM google.integrations.sfdc_instances
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND sfdcInstancesId = '{{ sfdcInstancesId }}';
```
