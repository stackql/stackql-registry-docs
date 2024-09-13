
---
title: service_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - service_connection_policies
  - networkconnectivity
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

Creates, updates, deletes or gets an <code>service_connection_policy</code> resource or lists <code>service_connection_policies</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.service_connection_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of a ServiceConnectionPolicy. Format: projects/{project}/locations/{location}/serviceConnectionPolicies/{service_connection_policy} See: https://google.aip.dev/122#fields-representing-resource-names |
| <CopyableCode code="description" /> | `string` | A description of this resource. |
| <CopyableCode code="createTime" /> | `string` | Output only. Time when the ServiceConnectionMap was created. |
| <CopyableCode code="etag" /> | `string` | Optional. The etag is computed by the server, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="infrastructure" /> | `string` | Output only. The type of underlying resources used to create the connection. |
| <CopyableCode code="labels" /> | `object` | User-defined labels. |
| <CopyableCode code="network" /> | `string` | The resource path of the consumer network. Example: - projects/{projectNumOrId}/global/networks/{resourceId}. |
| <CopyableCode code="pscConfig" /> | `object` | Configuration used for Private Service Connect connections. Used when Infrastructure is PSC. |
| <CopyableCode code="pscConnections" /> | `array` | Output only. [Output only] Information about each Private Service Connect connection. |
| <CopyableCode code="serviceClass" /> | `string` | The service class identifier for which this ServiceConnectionPolicy is for. The service class identifier is a unique, symbolic representation of a ServiceClass. It is provided by the Service Producer. Google services have a prefix of gcp or google-cloud. For example, gcp-memorystore-redis or google-cloud-sql. 3rd party services do not. For example, test-service-a3dfcx. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the ServiceConnectionMap was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, serviceConnectionPoliciesId" /> | Gets details of a single ServiceConnectionPolicy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ServiceConnectionPolicies in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ServiceConnectionPolicy in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, serviceConnectionPoliciesId" /> | Deletes a single ServiceConnectionPolicy. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, serviceConnectionPoliciesId" /> | Updates the parameters of a single ServiceConnectionPolicy. |

## `SELECT` examples

Lists ServiceConnectionPolicies in a given project and location.

```sql
SELECT
name,
description,
createTime,
etag,
infrastructure,
labels,
network,
pscConfig,
pscConnections,
serviceClass,
updateTime
FROM google.networkconnectivity.service_connection_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_connection_policies</code> resource.

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
INSERT INTO google.networkconnectivity.service_connection_policies (
locationsId,
projectsId,
name,
createTime,
updateTime,
labels,
description,
network,
serviceClass,
infrastructure,
pscConfig,
pscConnections,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ labels }}',
'{{ description }}',
'{{ network }}',
'{{ serviceClass }}',
'{{ infrastructure }}',
'{{ pscConfig }}',
'{{ pscConnections }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: labels
        value: '{{ labels }}'
      - name: description
        value: '{{ description }}'
      - name: network
        value: '{{ network }}'
      - name: serviceClass
        value: '{{ serviceClass }}'
      - name: infrastructure
        value: '{{ infrastructure }}'
      - name: pscConfig
        value: '{{ pscConfig }}'
      - name: pscConnections
        value: '{{ pscConnections }}'
      - name: etag
        value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a service_connection_policy only if the necessary resources are available.

```sql
UPDATE google.networkconnectivity.service_connection_policies
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
network = '{{ network }}',
serviceClass = '{{ serviceClass }}',
infrastructure = '{{ infrastructure }}',
pscConfig = '{{ pscConfig }}',
pscConnections = '{{ pscConnections }}',
etag = '{{ etag }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceConnectionPoliciesId = '{{ serviceConnectionPoliciesId }}';
```

## `DELETE` example

Deletes the specified service_connection_policy resource.

```sql
DELETE FROM google.networkconnectivity.service_connection_policies
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND serviceConnectionPoliciesId = '{{ serviceConnectionPoliciesId }}';
```
