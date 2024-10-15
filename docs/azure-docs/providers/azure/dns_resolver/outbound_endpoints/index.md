---
title: outbound_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - outbound_endpoints
  - dns_resolver
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

Creates, updates, deletes, gets or lists a <code>outbound_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outbound_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns_resolver.outbound_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outbound_endpoints', value: 'view', },
        { label: 'outbound_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dnsResolverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | ETag of the outbound endpoint. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="outboundEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | ETag of the outbound endpoint. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of an outbound endpoint for a DNS resolver. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Gets properties of an outbound endpoint for a DNS resolver. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="dnsResolverName, resourceGroupName, subscriptionId" /> | Lists outbound endpoints for a DNS resolver. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an outbound endpoint for a DNS resolver. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Deletes an outbound endpoint for a DNS resolver. WARNING: This operation cannot be undone. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dnsResolverName, outboundEndpointName, resourceGroupName, subscriptionId" /> | Updates an outbound endpoint for a DNS resolver. |

## `SELECT` examples

Lists outbound endpoints for a DNS resolver.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outbound_endpoints', value: 'view', },
        { label: 'outbound_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dnsResolverName,
etag,
location,
outboundEndpointName,
provisioning_state,
resourceGroupName,
resource_guid,
subnet,
subscriptionId,
system_data,
tags
FROM azure.dns_resolver.vw_outbound_endpoints
WHERE dnsResolverName = '{{ dnsResolverName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
systemData,
tags
FROM azure.dns_resolver.outbound_endpoints
WHERE dnsResolverName = '{{ dnsResolverName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>outbound_endpoints</code> resource.

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
INSERT INTO azure.dns_resolver.outbound_endpoints (
dnsResolverName,
outboundEndpointName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ dnsResolverName }}',
'{{ outboundEndpointName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: string
    - name: properties
      value:
        - name: subnet
          value:
            - name: id
              value: string
        - name: provisioningState
          value: []
        - name: resourceGuid
          value: []
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>outbound_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.dns_resolver.outbound_endpoints
SET 
tags = '{{ tags }}'
WHERE 
dnsResolverName = '{{ dnsResolverName }}'
AND outboundEndpointName = '{{ outboundEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>outbound_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dns_resolver.outbound_endpoints
WHERE dnsResolverName = '{{ dnsResolverName }}'
AND outboundEndpointName = '{{ outboundEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
