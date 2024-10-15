---
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
  - azure_stack
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

Creates, updates, deletes, gets or lists a <code>registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack.registrations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registrations', value: 'view', },
        { label: 'registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="billing_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="registrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Custom tags for the resource. |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="etag" /> | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties portion of the registration resource. |
| <CopyableCode code="tags" /> | `object` | Custom tags for the resource. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Returns the properties of an Azure Stack registration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroup, subscriptionId" /> | Returns a list of all registrations. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of all registrations under current subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="registrationName, resourceGroup, subscriptionId, data__location, data__properties" /> | Create or update an Azure Stack registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Delete the requested Azure Stack registration. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="registrationName, resourceGroup, subscriptionId, data__location, data__properties" /> | Patch an Azure Stack registration. |
| <CopyableCode code="enable_remote_management" /> | `EXEC` | <CopyableCode code="registrationName, resourceGroup, subscriptionId" /> | Enables remote management for device under the Azure Stack registration. |

## `SELECT` examples

Returns a list of all registrations under current subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registrations', value: 'view', },
        { label: 'registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
billing_model,
cloud_id,
etag,
location,
object_id,
registrationName,
resourceGroup,
subscriptionId,
tags,
type
FROM azure_stack.azure_stack.vw_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure_stack.azure_stack.registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registrations</code> resource.

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
INSERT INTO azure_stack.azure_stack.registrations (
registrationName,
resourceGroup,
subscriptionId,
data__location,
data__properties,
properties,
location
)
SELECT 
'{{ registrationName }}',
'{{ resourceGroup }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: registrationToken
          value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>registrations</code> resource.

```sql
/*+ update */
UPDATE azure_stack.azure_stack.registrations
SET 
properties = '{{ properties }}',
location = '{{ location }}'
WHERE 
registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__location = '{{ data__location }}'
AND data__properties = '{{ data__properties }}';
```

## `DELETE` example

Deletes the specified <code>registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_stack.registrations
WHERE registrationName = '{{ registrationName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
