---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - data_migration
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_stop_delay" /> | `text` | field from the `properties` object |
| <CopyableCode code="delete_resources_on_stop" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | HTTP strong entity tag value. Ignored if submitted |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The resource kind. Only 'vm' (the default) is supported. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | An Azure SKU instance |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_nic_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_subnet_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. Ignored if submitted |
| <CopyableCode code="kind" /> | `string` | The resource kind. Only 'vm' (the default) is supported. |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` | Properties of the Azure Database Migration Service (classic) instance |
| <CopyableCode code="sku" /> | `object` | An Azure SKU instance |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` |  |
| <CopyableCode code="type" /> | `string` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The GET method retrieves information about a service instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="groupName, subscriptionId" /> | The Services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PUT method creates a new service or updates an existing one. When a service is updated, existing child resources (i.e. tasks) are unaffected. Services currently support a single kind, "vm", which refers to a VM-based service, although other kinds may be added in the future. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). The provider will reply when successful with 200 OK or 201 Created. Long-running operations use the provisioningState property. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The DELETE method deletes a service. Any running tasks will be canceled. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). The PATCH method updates an existing service. This method can change the kind, SKU, and network of the service, but if tasks are currently running (i.e. the service is busy), this will fail with 400 Bad Request ("ServiceIsBusy"). |
| <CopyableCode code="check_children_name_availability" /> | `EXEC` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | This method checks whether a proposed nested resource name is valid and available. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | This method checks whether a proposed top-level resource name is valid and available. |
| <CopyableCode code="check_status" /> | `EXEC` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action performs a health check and returns the status of the service and virtual machine size. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action starts the service and the service can be used for data migration. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This action stops the service and the service cannot be used for data migration. The service owner won't be billed when the service is stopped. |

## `SELECT` examples

The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_services', value: 'view', },
        { label: 'services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
auto_stop_delay,
delete_resources_on_stop,
etag,
groupName,
kind,
location,
provisioning_state,
public_key,
serviceName,
sku,
subscriptionId,
system_data,
tags,
type,
virtual_nic_id,
virtual_subnet_id
FROM azure.data_migration.vw_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.data_migration.services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


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
INSERT INTO azure.data_migration.services (
groupName,
serviceName,
subscriptionId,
etag,
kind,
properties,
sku,
location,
tags
)
SELECT 
'{{ groupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ etag }}',
'{{ kind }}',
'{{ properties }}',
'{{ sku }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: publicKey
          value: string
        - name: virtualSubnetId
          value: string
        - name: virtualNicId
          value: string
        - name: autoStopDelay
          value: string
        - name: deleteResourcesOnStop
          value: boolean
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: family
          value: string
        - name: size
          value: string
        - name: capacity
          value: integer
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.data_migration.services
SET 
etag = '{{ etag }}',
kind = '{{ kind }}',
properties = '{{ properties }}',
sku = '{{ sku }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
groupName = '{{ groupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_migration.services
WHERE groupName = '{{ groupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
