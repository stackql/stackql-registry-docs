---
title: streaming_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_endpoints
  - media_services
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

Creates, updates, deletes, gets or lists a <code>streaming_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_endpoints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_endpoints', value: 'view', },
        { label: 'streaming_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_control" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_set_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="cdn_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="cdn_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="cdn_provider" /> | `text` | field from the `properties` object |
| <CopyableCode code="created" /> | `text` | field from the `properties` object |
| <CopyableCode code="cross_site_access_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_host_names" /> | `text` | field from the `properties` object |
| <CopyableCode code="free_trial_end_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_cache_age" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_units" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The streaming endpoint current sku. |
| <CopyableCode code="streamingEndpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The streaming endpoint properties. |
| <CopyableCode code="sku" /> | `object` | The streaming endpoint current sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Gets a streaming endpoint. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the streaming endpoints in the account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Creates a streaming endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Deletes a streaming endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Updates a existing streaming endpoint. |
| <CopyableCode code="async_operation" /> | `EXEC` | <CopyableCode code="accountName, operationId, resourceGroupName, subscriptionId" /> | Get a streaming endpoint operation status. |
| <CopyableCode code="operation_location" /> | `EXEC` | <CopyableCode code="accountName, operationId, resourceGroupName, streamingEndpointName, subscriptionId" /> | Get a streaming endpoint operation status. |
| <CopyableCode code="scale" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Scales an existing streaming endpoint. |
| <CopyableCode code="skus" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | List streaming endpoint supported skus. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Starts an existing streaming endpoint. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, streamingEndpointName, subscriptionId" /> | Stops an existing streaming endpoint. |

## `SELECT` examples

Lists the streaming endpoints in the account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_streaming_endpoints', value: 'view', },
        { label: 'streaming_endpoints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
access_control,
accountName,
availability_set_name,
cdn_enabled,
cdn_profile,
cdn_provider,
created,
cross_site_access_policies,
custom_host_names,
free_trial_end_time,
host_name,
last_modified,
location,
max_cache_age,
provisioning_state,
resourceGroupName,
resource_state,
scale_units,
sku,
streamingEndpointName,
subscriptionId,
system_data,
tags
FROM azure.media_services.vw_streaming_endpoints
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
systemData,
tags
FROM azure.media_services.streaming_endpoints
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>streaming_endpoints</code> resource.

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
INSERT INTO azure.media_services.streaming_endpoints (
accountName,
resourceGroupName,
streamingEndpointName,
subscriptionId,
properties,
sku,
tags,
location
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ streamingEndpointName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}',
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
        - name: scaleUnits
          value: integer
        - name: availabilitySetName
          value: string
        - name: accessControl
          value:
            - name: akamai
              value:
                - name: akamaiSignatureHeaderAuthenticationKeyList
                  value:
                    - - name: identifier
                        value: string
                      - name: base64Key
                        value: string
                      - name: expiration
                        value: string
            - name: ip
              value:
                - name: allow
                  value:
                    - - name: name
                        value: string
                      - name: address
                        value: string
                      - name: subnetPrefixLength
                        value: integer
        - name: maxCacheAge
          value: integer
        - name: customHostNames
          value:
            - string
        - name: hostName
          value: string
        - name: cdnEnabled
          value: boolean
        - name: cdnProvider
          value: string
        - name: cdnProfile
          value: string
        - name: provisioningState
          value: string
        - name: resourceState
          value: string
        - name: crossSiteAccessPolicies
          value:
            - name: clientAccessPolicy
              value: string
            - name: crossDomainPolicy
              value: string
        - name: freeTrialEndTime
          value: string
        - name: created
          value: string
        - name: lastModified
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
    - name: sku
      value:
        - name: name
          value: string
        - name: capacity
          value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>streaming_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.media_services.streaming_endpoints
SET 
properties = '{{ properties }}',
sku = '{{ sku }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingEndpointName = '{{ streamingEndpointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>streaming_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.media_services.streaming_endpoints
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingEndpointName = '{{ streamingEndpointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
