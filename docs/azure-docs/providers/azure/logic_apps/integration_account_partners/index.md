---
title: integration_account_partners
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_partners
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_account_partners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_partners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_account_partners" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_partners', value: 'view', },
        { label: 'integration_account_partners', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="content" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration account partner properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationAccountName, partnerName, resourceGroupName, subscriptionId" /> | Gets an integration account partner. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationAccountName, resourceGroupName, subscriptionId" /> | Gets a list of integration account partners. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="integrationAccountName, partnerName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an integration account partner. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationAccountName, partnerName, resourceGroupName, subscriptionId" /> | Deletes an integration account partner. |

## `SELECT` examples

Gets a list of integration account partners.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_account_partners', value: 'view', },
        { label: 'integration_account_partners', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
changed_time,
content,
created_time,
integrationAccountName,
location,
metadata,
partnerName,
partner_type,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_account_partners
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
FROM azure.logic_apps.integration_account_partners
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>integration_account_partners</code> resource.

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
INSERT INTO azure.logic_apps.integration_account_partners (
integrationAccountName,
partnerName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
location,
tags
)
SELECT 
'{{ integrationAccountName }}',
'{{ partnerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: partnerType
          value: []
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: metadata
          value: []
        - name: content
          value:
            - name: b2b
              value:
                - name: businessIdentities
                  value:
                    - - name: qualifier
                        value: string
                      - name: value
                        value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>integration_account_partners</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_account_partners
WHERE integrationAccountName = '{{ integrationAccountName }}'
AND partnerName = '{{ partnerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
