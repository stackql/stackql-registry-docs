---
title: partner_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_registrations
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>partner_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_registrations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_registrations', value: 'view', },
        { label: 'partner_registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="partnerRegistrationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_registration_immutable_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the partner registration. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="partnerRegistrationName, resourceGroupName, subscriptionId" /> | Gets a partner registration with the specified parameters. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner registrations under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the partner registrations under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="partnerRegistrationName, resourceGroupName, subscriptionId" /> | Creates a new partner registration with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerRegistrationName, resourceGroupName, subscriptionId" /> | Deletes a partner registration with the specified parameters. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="partnerRegistrationName, resourceGroupName, subscriptionId" /> | Updates a partner registration with the specified parameters. |

## `SELECT` examples

List all the partner registrations under an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_registrations', value: 'view', },
        { label: 'partner_registrations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
partnerRegistrationName,
partner_registration_immutable_id,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure.event_grid.vw_partner_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.event_grid.partner_registrations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_registrations</code> resource.

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
INSERT INTO azure.event_grid.partner_registrations (
partnerRegistrationName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ partnerRegistrationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: partnerRegistrationImmutableId
          value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>partner_registrations</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.partner_registrations
SET 
tags = '{{ tags }}'
WHERE 
partnerRegistrationName = '{{ partnerRegistrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>partner_registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.partner_registrations
WHERE partnerRegistrationName = '{{ partnerRegistrationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
