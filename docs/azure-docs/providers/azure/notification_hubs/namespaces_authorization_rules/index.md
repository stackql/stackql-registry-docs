---
title: namespaces_authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces_authorization_rules
  - notification_hubs
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

Creates, updates, deletes, gets or lists a <code>namespaces_authorization_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces_authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.namespaces_authorization_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces_authorization_rules', value: 'view', },
        { label: 'namespaces_authorization_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorizationRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="claim_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="claim_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Deprecated - only for compatibility. |
| <CopyableCode code="modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="revision" /> | `text` | field from the `properties` object |
| <CopyableCode code="rights" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Deprecated - only for compatibility. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Deprecated - only for compatibility. |
| <CopyableCode code="properties" /> | `object` | SharedAccessAuthorizationRule properties. |
| <CopyableCode code="tags" /> | `object` | Deprecated - only for compatibility. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespaces_authorization_rules', value: 'view', },
        { label: 'namespaces_authorization_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
authorizationRuleName,
claim_type,
claim_value,
created_time,
key_name,
location,
modified_time,
namespaceName,
primary_key,
resourceGroupName,
revision,
rights,
secondary_key,
subscriptionId,
tags
FROM azure.notification_hubs.vw_namespaces_authorization_rules
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.notification_hubs.namespaces_authorization_rules
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespaces_authorization_rules</code> resource.

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
INSERT INTO azure.notification_hubs.namespaces_authorization_rules (
authorizationRuleName,
namespaceName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ authorizationRuleName }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: rights
          value:
            - []
        - name: primaryKey
          value: string
        - name: secondaryKey
          value: string
        - name: keyName
          value: string
        - name: modifiedTime
          value: string
        - name: createdTime
          value: string
        - name: claimType
          value: string
        - name: claimValue
          value: string
        - name: revision
          value: integer
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>namespaces_authorization_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.notification_hubs.namespaces_authorization_rules
WHERE authorizationRuleName = '{{ authorizationRuleName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
