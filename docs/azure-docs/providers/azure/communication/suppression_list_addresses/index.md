---
title: suppression_list_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression_list_addresses
  - communication
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

Creates, updates, deletes, gets or lists a <code>suppression_list_addresses</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suppression_list_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.suppression_list_addresses" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_suppression_list_addresses', value: 'view', },
        { label: 'suppression_list_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="addressId" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="email" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suppressionListName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of a SuppressionListAddress resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get a SuppressionListAddress. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get all the addresses in a suppression list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Create or update a SuppressionListAddress. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="addressId, domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Operation to delete a single address from a suppression list. |

## `SELECT` examples

Get all the addresses in a suppression list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_suppression_list_addresses', value: 'view', },
        { label: 'suppression_list_addresses', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
addressId,
data_location,
domainName,
email,
emailServiceName,
first_name,
last_modified,
last_name,
notes,
resourceGroupName,
subscriptionId,
suppressionListName
FROM azure.communication.vw_suppression_list_addresses
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND suppressionListName = '{{ suppressionListName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.communication.suppression_list_addresses
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND suppressionListName = '{{ suppressionListName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>suppression_list_addresses</code> resource.

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
INSERT INTO azure.communication.suppression_list_addresses (
addressId,
domainName,
emailServiceName,
resourceGroupName,
subscriptionId,
suppressionListName,
properties
)
SELECT 
'{{ addressId }}',
'{{ domainName }}',
'{{ emailServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ suppressionListName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: email
          value: string
        - name: firstName
          value: string
        - name: lastName
          value: string
        - name: notes
          value: string
        - name: lastModified
          value: string
        - name: dataLocation
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>suppression_list_addresses</code> resource.

```sql
/*+ delete */
DELETE FROM azure.communication.suppression_list_addresses
WHERE addressId = '{{ addressId }}'
AND domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND suppressionListName = '{{ suppressionListName }}';
```
