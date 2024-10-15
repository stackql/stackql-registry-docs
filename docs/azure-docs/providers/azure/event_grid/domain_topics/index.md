---
title: domain_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topics
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

Creates, updates, deletes, gets or lists a <code>domain_topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domain_topics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domain_topics', value: 'view', },
        { label: 'domain_topics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainTopicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the Domain Topic. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Get properties of a domain topic. |
| <CopyableCode code="list_by_domain" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | List all the topics in a domain. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates a new domain topic with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, domainTopicName, resourceGroupName, subscriptionId" /> | Delete existing domain topic. |

## `SELECT` examples

List all the topics in a domain.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_domain_topics', value: 'view', },
        { label: 'domain_topics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
domainName,
domainTopicName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.event_grid.vw_domain_topics
WHERE domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.event_grid.domain_topics
WHERE domainName = '{{ domainName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>domain_topics</code> resource.

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
INSERT INTO azure.event_grid.domain_topics (
domainName,
domainTopicName,
resourceGroupName,
subscriptionId
)
SELECT 
'{{ domainName }}',
'{{ domainTopicName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>domain_topics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.domain_topics
WHERE domainName = '{{ domainName }}'
AND domainTopicName = '{{ domainTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
