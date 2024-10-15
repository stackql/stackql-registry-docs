---
title: email_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - email_configurations
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>email_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.email_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_configurations', value: 'view', },
        { label: 'email_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="custom_email_addresses" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="locale" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="send_to_owners" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Email configuration model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="emailConfigurationName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the alert configuration setting. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the list of alert configuration settings for the given vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="emailConfigurationName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates an alert configuration setting for the given vault. |

## `SELECT` examples

Gets the list of alert configuration settings for the given vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_configurations', value: 'view', },
        { label: 'email_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_email_addresses,
emailConfigurationName,
locale,
resourceGroupName,
send_to_owners,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_replication.vw_email_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
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
FROM azure.data_replication.email_configurations
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>email_configurations</code> resource.

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
INSERT INTO azure.data_replication.email_configurations (
emailConfigurationName,
resourceGroupName,
subscriptionId,
vaultName,
data__properties,
properties
)
SELECT 
'{{ emailConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ data__properties }}',
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
        - name: sendToOwners
          value: boolean
        - name: customEmailAddresses
          value:
            - string
        - name: locale
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>
