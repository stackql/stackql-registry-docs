---
title: tenancy_units_project
hide_title: false
hide_table_of_contents: false
keywords:
  - tenancy_units_project
  - serviceconsumermanagement
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

Creates, updates, deletes, gets or lists a <code>tenancy_units_project</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenancy_units_project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.serviceconsumermanagement.tenancy_units_project" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_project" /> | `INSERT` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Add a new tenant project to the tenancy unit. There can be a maximum of 1024 tenant projects in a tenancy unit. If there are previously failed `AddTenantProject` calls, you might need to call `RemoveTenantProject` first to resolve them before you can make another call to `AddTenantProject` with the same tag. Operation. |
| <CopyableCode code="delete_project" /> | `DELETE` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Deletes the specified project resource identified by a tenant resource tag. The mothod removes a project lien with a 'TenantManager' origin if that was added. It will then attempt to delete the project. If that operation fails, this method also fails. After the project has been deleted, the tenant resource state is set to DELETED. To permanently remove resource metadata, call the `RemoveTenantProject` method. New resources with the same tag can't be added if there are existing resources in a DELETED state. Operation. |
| <CopyableCode code="remove_project" /> | `DELETE` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Removes the specified project resource identified by a tenant resource tag. The method removes the project lien with 'TenantManager' origin if that was added. It then attempts to delete the project. If that operation fails, this method also fails. Calls to remove already removed or non-existent tenant project succeed. After the project has been deleted, or if was already in a DELETED state, resource metadata is permanently removed from the tenancy unit. Operation. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tenancy_units_project</code> resource.

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
INSERT INTO google.serviceconsumermanagement.tenancy_units_project (
servicesId,
servicesId1,
servicesId2,
tenancyUnitsId,
projectConfig,
tag
)
SELECT 
'{{ servicesId }}',
'{{ servicesId1 }}',
'{{ servicesId2 }}',
'{{ tenancyUnitsId }}',
'{{ projectConfig }}',
'{{ tag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: projectConfig
      value:
        - name: labels
          value: object
        - name: tenantProjectPolicy
          value:
            - name: policyBindings
              value:
                - - name: members
                    value:
                      - string
                  - name: role
                    value: string
        - name: billingConfig
          value:
            - name: billingAccount
              value: string
        - name: folder
          value: string
        - name: serviceAccountConfig
          value:
            - name: accountId
              value: string
            - name: tenantProjectRoles
              value:
                - string
        - name: services
          value:
            - string
    - name: tag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tenancy_units_project</code> resource.

```sql
/*+ delete */
DELETE FROM google.serviceconsumermanagement.tenancy_units_project
WHERE servicesId = '{{ servicesId }}'
AND servicesId1 = '{{ servicesId1 }}'
AND servicesId2 = '{{ servicesId2 }}'
AND tenancyUnitsId = '{{ tenancyUnitsId }}';
```
