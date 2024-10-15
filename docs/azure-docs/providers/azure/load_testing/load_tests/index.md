---
title: load_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - load_tests
  - load_testing
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

Creates, updates, deletes, gets or lists a <code>load_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>load_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.load_testing.load_tests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_tests', value: 'view', },
        { label: 'load_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_plane_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="encryption" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="loadTestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | LoadTest resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Get a LoadTestResource |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List LoadTestResource resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List LoadTestResource resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Create a LoadTestResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Delete a LoadTestResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="loadTestName, resourceGroupName, subscriptionId" /> | Update a LoadTestResource |

## `SELECT` examples

List LoadTestResource resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_load_tests', value: 'view', },
        { label: 'load_tests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
data_plane_uri,
encryption,
identity,
loadTestName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.load_testing.vw_load_tests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.load_testing.load_tests
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>load_tests</code> resource.

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
INSERT INTO azure.load_testing.load_tests (
loadTestName,
resourceGroupName,
subscriptionId,
properties,
identity,
tags,
location
)
SELECT 
'{{ loadTestName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
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
        - name: provisioningState
          value: []
        - name: dataPlaneURI
          value: string
        - name: encryption
          value:
            - name: identity
              value:
                - name: type
                  value: []
                - name: resourceId
                  value: string
            - name: keyUrl
              value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>load_tests</code> resource.

```sql
/*+ update */
UPDATE azure.load_testing.load_tests
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
loadTestName = '{{ loadTestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>load_tests</code> resource.

```sql
/*+ delete */
DELETE FROM azure.load_testing.load_tests
WHERE loadTestName = '{{ loadTestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
