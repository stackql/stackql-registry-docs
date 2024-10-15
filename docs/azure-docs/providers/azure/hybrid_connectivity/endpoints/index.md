---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Endpoint details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri" /> | Gets the endpoint to the resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List of endpoints to the target resource. |
| <CopyableCode code="list_ingress_gateway_credentials" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri" /> | Gets the ingress gateway endpoint credentials  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="endpointName, resourceUri" /> | Create or update the endpoint to the target resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, resourceUri" /> | Deletes the endpoint access to the target resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, resourceUri" /> | Update the endpoint to the target resource. |

## `SELECT` examples

List of endpoints to the target resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_endpoints', value: 'view', },
        { label: 'endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
endpointName,
provisioning_state,
resourceUri,
resource_id,
system_data,
type
FROM azure.hybrid_connectivity.vw_endpoints
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.hybrid_connectivity.endpoints
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

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
INSERT INTO azure.hybrid_connectivity.endpoints (
endpointName,
resourceUri,
systemData,
properties
)
SELECT 
'{{ endpointName }}',
'{{ resourceUri }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: type
          value: string
        - name: resourceId
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_connectivity.endpoints
SET 
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_connectivity.endpoints
WHERE endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}';
```
