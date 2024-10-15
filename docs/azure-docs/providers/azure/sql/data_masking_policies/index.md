---
title: data_masking_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_policies
  - sql
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

Creates, updates, deletes, gets or lists a <code>data_masking_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_masking_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.data_masking_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_masking_policies', value: 'view', },
        { label: 'data_masking_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataMaskingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_masking_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="databaseName" /> | `text` | field from the `properties` object |
| <CopyableCode code="exempt_principals" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of data masking policy. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `text` | The location of the data masking policy. |
| <CopyableCode code="masking_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of data masking policy. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `string` | The location of the data masking policy. |
| <CopyableCode code="properties" /> | `object` | The properties of a database data masking policy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a database data masking policy. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a database data masking policy |

## `SELECT` examples

Gets a database data masking policy.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_masking_policies', value: 'view', },
        { label: 'data_masking_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_principals,
dataMaskingPolicyName,
data_masking_state,
databaseName,
exempt_principals,
kind,
location,
masking_level,
resourceGroupName,
serverName,
subscriptionId
FROM azure.sql.vw_data_masking_policies
WHERE dataMaskingPolicyName = '{{ dataMaskingPolicyName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.sql.data_masking_policies
WHERE dataMaskingPolicyName = '{{ dataMaskingPolicyName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_masking_policies</code> resource.

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
INSERT INTO azure.sql.data_masking_policies (
dataMaskingPolicyName,
databaseName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ dataMaskingPolicyName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
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
        - name: dataMaskingState
          value: string
        - name: exemptPrincipals
          value: string
        - name: applicationPrincipals
          value: string
        - name: maskingLevel
          value: string
    - name: location
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>
