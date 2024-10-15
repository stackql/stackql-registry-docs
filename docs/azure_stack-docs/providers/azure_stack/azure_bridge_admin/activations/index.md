---
title: activations
hide_title: false
hide_table_of_contents: false
keywords:
  - activations
  - azure_bridge_admin
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

Creates, updates, deletes, gets or lists a <code>activations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>activations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_bridge_admin.activations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activations', value: 'view', },
        { label: 'activations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | URI of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="activationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="azure_registration_resource_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource |
| <CopyableCode code="marketplace_syndication_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | List of key value pairs. |
| <CopyableCode code="type" /> | `text` | Type of resource. |
| <CopyableCode code="usage_reporting_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Holds properties related to activation. |
| <CopyableCode code="tags" /> | `object` | List of key value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Returns activation name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns the list of activations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Create a new activation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="activationName, resourceGroupName, subscriptionId" /> | Delete an activation. |

## `SELECT` examples

Returns the list of activations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_activations', value: 'view', },
        { label: 'activations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
activationName,
azure_registration_resource_identifier,
display_name,
expiration,
location,
marketplace_syndication_enabled,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
usage_reporting_enabled
FROM azure_stack.azure_bridge_admin.vw_activations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.azure_bridge_admin.activations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>activations</code> resource.

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
INSERT INTO azure_stack.azure_bridge_admin.activations (
activationName,
resourceGroupName,
subscriptionId,
displayName,
azureRegistrationResourceIdentifier,
provisioningState,
expiration,
marketplaceSyndicationEnabled,
usageReportingEnabled
)
SELECT 
'{{ activationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ displayName }}',
'{{ azureRegistrationResourceIdentifier }}',
'{{ provisioningState }}',
'{{ expiration }}',
{{ marketplaceSyndicationEnabled }},
{{ usageReportingEnabled }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: displayName
      value: string
    - name: azureRegistrationResourceIdentifier
      value: string
    - name: provisioningState
      value: []
    - name: expiration
      value: string
    - name: marketplaceSyndicationEnabled
      value: boolean
    - name: usageReportingEnabled
      value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>activations</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.azure_bridge_admin.activations
WHERE activationName = '{{ activationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
