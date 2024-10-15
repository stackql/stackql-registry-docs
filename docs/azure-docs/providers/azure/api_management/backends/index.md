---
title: backends
hide_title: false
hide_table_of_contents: false
keywords:
  - backends
  - api_management
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

Creates, updates, deletes, gets or lists a <code>backends</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backends</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.backends" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backends', value: 'view', },
        { label: 'backends', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="backendId" /> | `text` | field from the `properties` object |
| <CopyableCode code="circuit_breaker" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="pool" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Parameters supplied to the Create Backend operation. |
| <CopyableCode code="protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="proxy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="tls" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | field from the `properties` object |
| <CopyableCode code="url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Parameters supplied to the Create Backend operation. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the backend specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of backends in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Creates or Updates a backend. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, backendId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified backend. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, backendId, resourceGroupName, serviceName, subscriptionId" /> | Updates an existing backend. |
| <CopyableCode code="reconnect" /> | `EXEC` | <CopyableCode code="backendId, resourceGroupName, serviceName, subscriptionId" /> | Notifies the API Management gateway to create a new connection to the backend after the specified timeout. If no timeout was specified, timeout of 2 minutes is used. |

## `SELECT` examples

Lists a collection of backends in the specified service instance.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_backends', value: 'view', },
        { label: 'backends', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
backendId,
circuit_breaker,
credentials,
pool,
properties,
protocol,
proxy,
resourceGroupName,
resource_id,
serviceName,
subscriptionId,
title,
tls,
type,
url
FROM azure.api_management.vw_backends
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.backends
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backends</code> resource.

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
INSERT INTO azure.api_management.backends (
backendId,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ backendId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
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
        - name: url
          value: string
        - name: protocol
          value: string
        - name: title
          value: string
        - name: description
          value: string
        - name: resourceId
          value: string
        - name: properties
          value:
            - name: serviceFabricCluster
              value:
                - name: clientCertificateId
                  value: string
                - name: clientCertificatethumbprint
                  value: string
                - name: maxPartitionResolutionRetries
                  value: integer
                - name: managementEndpoints
                  value:
                    - string
                - name: serverCertificateThumbprints
                  value:
                    - string
                - name: serverX509Names
                  value:
                    - - name: name
                        value: string
                      - name: issuerCertificateThumbprint
                        value: string
        - name: credentials
          value:
            - name: certificateIds
              value:
                - string
            - name: certificate
              value:
                - string
            - name: query
              value: object
            - name: header
              value: object
            - name: authorization
              value:
                - name: scheme
                  value: string
                - name: parameter
                  value: string
        - name: proxy
          value:
            - name: url
              value: string
            - name: username
              value: string
            - name: password
              value: string
        - name: tls
          value:
            - name: validateCertificateChain
              value: boolean
            - name: validateCertificateName
              value: boolean
        - name: circuitBreaker
          value:
            - name: rules
              value:
                - - name: name
                    value: string
                  - name: failureCondition
                    value:
                      - name: count
                        value: integer
                      - name: percentage
                        value: integer
                      - name: interval
                        value: string
                      - name: statusCodeRanges
                        value:
                          - - name: min
                              value: integer
                            - name: max
                              value: integer
                      - name: errorReasons
                        value:
                          - string
                  - name: tripDuration
                    value: string
                  - name: acceptRetryAfter
                    value: boolean
        - name: pool
          value: string
        - name: type
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>backends</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.backends
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND backendId = '{{ backendId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>backends</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.backends
WHERE If-Match = '{{ If-Match }}'
AND backendId = '{{ backendId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
