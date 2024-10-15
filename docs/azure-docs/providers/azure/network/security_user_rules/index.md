---
title: security_user_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_user_rules
  - network
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

Creates, updates, deletes, gets or lists a <code>security_user_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_user_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.security_user_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_user_rules', value: 'view', },
        { label: 'security_user_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination_port_ranges" /> | `text` | field from the `properties` object |
| <CopyableCode code="destinations" /> | `text` | field from the `properties` object |
| <CopyableCode code="direction" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_port_ranges" /> | `text` | field from the `properties` object |
| <CopyableCode code="sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Security rule resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId" /> | Gets a security user rule. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Lists all Security User Rules in a rule collection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId" /> | Creates or updates a security user rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, ruleName, subscriptionId" /> | Deletes a security user rule. |

## `SELECT` examples

Lists all Security User Rules in a rule collection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_security_user_rules', value: 'view', },
        { label: 'security_user_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
configurationName,
destination_port_ranges,
destinations,
direction,
etag,
networkManagerName,
protocol,
provisioning_state,
resourceGroupName,
resource_guid,
ruleCollectionName,
ruleName,
source_port_ranges,
sources,
subscriptionId,
system_data,
type
FROM azure.network.vw_security_user_rules
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.network.security_user_rules
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_user_rules</code> resource.

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
INSERT INTO azure.network.security_user_rules (
configurationName,
networkManagerName,
resourceGroupName,
ruleCollectionName,
ruleName,
subscriptionId,
properties
)
SELECT 
'{{ configurationName }}',
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ ruleCollectionName }}',
'{{ ruleName }}',
'{{ subscriptionId }}',
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
        - name: description
          value: string
        - name: protocol
          value: []
        - name: sources
          value:
            - - name: addressPrefix
                value: string
              - name: addressPrefixType
                value: string
        - name: destinations
          value:
            - - name: addressPrefix
                value: string
              - name: addressPrefixType
                value: string
        - name: sourcePortRanges
          value:
            - string
        - name: destinationPortRanges
          value:
            - string
        - name: direction
          value: []
        - name: provisioningState
          value: []
        - name: resourceGuid
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>security_user_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.security_user_rules
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND ruleName = '{{ ruleName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
