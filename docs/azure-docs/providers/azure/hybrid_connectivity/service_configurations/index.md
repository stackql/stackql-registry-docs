---
title: service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_configurations
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

Creates, updates, deletes, gets or lists a <code>service_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.service_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_configurations', value: 'view', },
        { label: 'service_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Service configuration details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Gets the details about the service to the resource. |
| <CopyableCode code="list_by_endpoint_resource" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri" /> | API to enumerate registered services in service configurations under a Endpoint Resource |
| <CopyableCode code="create_orupdate" /> | `INSERT` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Create or update a service in serviceConfiguration for the endpoint resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Deletes the service details to the target resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, resourceUri, serviceConfigurationName" /> | Update the service details in the service configurations of the target resource. |

## `SELECT` examples

API to enumerate registered services in service configurations under a Endpoint Resource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_service_configurations', value: 'view', },
        { label: 'service_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
endpointName,
port,
provisioning_state,
resourceUri,
resource_id,
serviceConfigurationName,
service_name,
system_data
FROM azure.hybrid_connectivity.vw_service_configurations
WHERE endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.hybrid_connectivity.service_configurations
WHERE endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_configurations</code> resource.

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
INSERT INTO azure.hybrid_connectivity.service_configurations (
endpointName,
resourceUri,
serviceConfigurationName,
systemData,
properties
)
SELECT 
'{{ endpointName }}',
'{{ resourceUri }}',
'{{ serviceConfigurationName }}',
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
        - name: serviceName
          value: string
        - name: resourceId
          value: string
        - name: port
          value: integer
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_connectivity.service_configurations
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}'
AND serviceConfigurationName = '{{ serviceConfigurationName }}';
```

## `DELETE` example

Deletes the specified <code>service_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_connectivity.service_configurations
WHERE endpointName = '{{ endpointName }}'
AND resourceUri = '{{ resourceUri }}'
AND serviceConfigurationName = '{{ serviceConfigurationName }}';
```
