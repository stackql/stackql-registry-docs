---
title: tenancy_units
hide_title: false
hide_table_of_contents: false
keywords:
  - tenancy_units
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

Creates, updates, deletes, gets or lists a <code>tenancy_units</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenancy_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.serviceconsumermanagement.tenancy_units" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Globally unique identifier of this tenancy unit "services/{service}/{collection id}/{resource id}/tenancyUnits/{unit}" |
| <CopyableCode code="consumer" /> | `string` | Output only. @OutputOnly Cloud resource name of the consumer of this service. For example 'projects/123456'. |
| <CopyableCode code="createTime" /> | `string` | Output only. @OutputOnly The time this tenancy unit was created. |
| <CopyableCode code="service" /> | `string` | Output only. Google Cloud API name of the managed service owning this tenancy unit. For example 'serviceconsumermanagement.googleapis.com'. |
| <CopyableCode code="tenantResources" /> | `array` | Resources constituting the tenancy unit. There can be at most 512 tenant resources in a tenancy unit. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="servicesId, servicesId1, servicesId2" /> | Find the tenancy unit for a managed service and service consumer. This method shouldn't be used in a service producer's runtime path, for example to find the tenant project number when creating VMs. Service producers must persist the tenant project's information after the project is created. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="servicesId, servicesId1, servicesId2" /> | Creates a tenancy unit with no tenant resources. If tenancy unit already exists, it will be returned, however, in this case, returned TenancyUnit does not have tenant_resources field set and ListTenancyUnits has to be used to get a complete TenancyUnit with all fields populated. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Delete a tenancy unit. Before you delete the tenancy unit, there should be no tenant resources in it that aren't in a DELETED state. Operation. |
| <CopyableCode code="apply_project_config" /> | `EXEC` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Apply a configuration to an existing tenant project. This project must exist in an active state and have the original owner account. The caller must have permission to add a project to the given tenancy unit. The configuration is applied, but any existing settings on the project aren't modified. Specified policy bindings are applied. Existing bindings aren't modified. Specified services are activated. No service is deactivated. If specified, new billing configuration is applied. Omit a billing configuration to keep the existing one. A service account in the project is created if previously non existed. Specified labels will be appended to tenant project, note that the value of existing label key will be updated if the same label key is requested. The specified folder is ignored, as moving a tenant project to a different folder isn't supported. The operation fails if any of the steps fail, but no rollback of already applied configuration changes is attempted. Operation. |
| <CopyableCode code="attach_project" /> | `EXEC` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Attach an existing project to the tenancy unit as a new tenant resource. The project could either be the tenant project reserved by calling `AddTenantProject` under a tenancy unit of a service producer's project of a managed service, or from a separate project. The caller is checked against a set of permissions as if calling `AddTenantProject` on the same service consumer. To trigger the attachment, the targeted tenant project must be in a folder. Make sure the ServiceConsumerManagement service account is the owner of that project. These two requirements are already met if the project is reserved by calling `AddTenantProject`. Operation. |
| <CopyableCode code="undelete_project" /> | `EXEC` | <CopyableCode code="servicesId, servicesId1, servicesId2, tenancyUnitsId" /> | Attempts to undelete a previously deleted tenant project. The project must be in a DELETED state. There are no guarantees that an undeleted project will be in a fully restored and functional state. Call the `ApplyTenantProjectConfig` method to update its configuration and then validate all managed service resources. Operation. |

## `SELECT` examples

Find the tenancy unit for a managed service and service consumer. This method shouldn't be used in a service producer's runtime path, for example to find the tenant project number when creating VMs. Service producers must persist the tenant project's information after the project is created.

```sql
SELECT
name,
consumer,
createTime,
service,
tenantResources
FROM google.serviceconsumermanagement.tenancy_units
WHERE servicesId = '{{ servicesId }}'
AND servicesId1 = '{{ servicesId1 }}'
AND servicesId2 = '{{ servicesId2 }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tenancy_units</code> resource.

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
INSERT INTO google.serviceconsumermanagement.tenancy_units (
servicesId,
servicesId1,
servicesId2,
tenancyUnitId
)
SELECT 
'{{ servicesId }}',
'{{ servicesId1 }}',
'{{ servicesId2 }}',
'{{ tenancyUnitId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tenancyUnitId
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tenancy_units</code> resource.

```sql
/*+ delete */
DELETE FROM google.serviceconsumermanagement.tenancy_units
WHERE servicesId = '{{ servicesId }}'
AND servicesId1 = '{{ servicesId1 }}'
AND servicesId2 = '{{ servicesId2 }}'
AND tenancyUnitsId = '{{ tenancyUnitsId }}';
```
