---
title: suppression_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - suppression_lists
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

Creates, updates, deletes, gets or lists a <code>suppression_lists</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suppression_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.suppression_lists" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_suppression_lists', value: 'view', },
        { label: 'suppression_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_time_stamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated_time_stamp" /> | `text` | field from the `properties` object |
| <CopyableCode code="list_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suppressionListName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of a SuppressionList resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Get a SuppressionList resource. |
| <CopyableCode code="list_by_domain" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | List all suppression lists for a domains resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Add a new SuppressionList resource under the parent Domains resource or update an existing SuppressionList resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId, suppressionListName" /> | Delete a SuppressionList. |

## `SELECT` examples

List all suppression lists for a domains resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_suppression_lists', value: 'view', },
        { label: 'suppression_lists', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
created_time_stamp,
data_location,
domainName,
emailServiceName,
last_updated_time_stamp,
list_name,
resourceGroupName,
subscriptionId,
suppressionListName
FROM azure.communication.vw_suppression_lists
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.communication.suppression_lists
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>suppression_lists</code> resource.

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
INSERT INTO azure.communication.suppression_lists (
domainName,
emailServiceName,
resourceGroupName,
subscriptionId,
suppressionListName,
properties
)
SELECT 
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
        - name: listName
          value: string
        - name: lastUpdatedTimeStamp
          value: string
        - name: createdTimeStamp
          value: string
        - name: dataLocation
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>suppression_lists</code> resource.

```sql
/*+ delete */
DELETE FROM azure.communication.suppression_lists
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND suppressionListName = '{{ suppressionListName }}';
```
