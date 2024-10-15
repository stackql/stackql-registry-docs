---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
  - cdn
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.endpoints" /></td></tr>
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
| <CopyableCode code="content_types_to_compress" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_domains" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_origin_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="geo_filters" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_compression_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_http_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_https_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="optimization_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_host_header" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="origins" /> | `text` | field from the `properties` object |
| <CopyableCode code="probe_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="query_string_caching_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="url_signing_keys" /> | `text` | field from the `properties` object |
| <CopyableCode code="web_application_firewall_policy_link" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties required to create an endpoint. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="list_by_profile" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Lists existing CDN endpoints. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation. |
| <CopyableCode code="load_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Pre-loads a content to CDN. Available for Verizon Profiles. |
| <CopyableCode code="purge_content" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths" /> | Removes a content from CDN. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Starts an existing CDN endpoint that is on a stopped state. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Stops an existing running CDN endpoint. |
| <CopyableCode code="validate_custom_domain" /> | `EXEC` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId, data__hostName" /> | Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS. |

## `SELECT` examples

Lists existing CDN endpoints.

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
content_types_to_compress,
custom_domains,
default_origin_group,
delivery_policy,
endpointName,
geo_filters,
host_name,
is_compression_enabled,
is_http_allowed,
is_https_allowed,
location,
optimization_type,
origin_groups,
origin_host_header,
origin_path,
origins,
probe_path,
profileName,
provisioning_state,
query_string_caching_behavior,
resourceGroupName,
resource_state,
subscriptionId,
tags,
url_signing_keys,
web_application_firewall_policy_link
FROM azure.cdn.vw_endpoints
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.cdn.endpoints
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.cdn.endpoints (
endpointName,
profileName,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ endpointName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: originPath
          value: string
        - name: contentTypesToCompress
          value:
            - string
        - name: originHostHeader
          value: string
        - name: isCompressionEnabled
          value: boolean
        - name: isHttpAllowed
          value: boolean
        - name: isHttpsAllowed
          value: boolean
        - name: queryStringCachingBehavior
          value: []
        - name: optimizationType
          value: []
        - name: probePath
          value: string
        - name: geoFilters
          value:
            - - name: relativePath
                value: string
              - name: action
                value: string
              - name: countryCodes
                value:
                  - string
        - name: defaultOriginGroup
          value:
            - name: id
              value: string
        - name: urlSigningKeys
          value:
            - - name: keyId
                value: string
              - name: keySourceParameters
                value:
                  - name: typeName
                    value: string
                  - name: subscriptionId
                    value: string
                  - name: resourceGroupName
                    value: string
                  - name: vaultName
                    value: string
                  - name: secretName
                    value: string
                  - name: secretVersion
                    value: string
        - name: deliveryPolicy
          value:
            - name: description
              value: string
            - name: rules
              value:
                - - name: name
                    value: string
                  - name: order
                    value: integer
                  - name: conditions
                    value:
                      - - name: name
                          value: string
                  - name: actions
                    value:
                      - - name: name
                          value: string
        - name: webApplicationFirewallPolicyLink
          value:
            - name: id
              value: string
        - name: hostName
          value: string
        - name: origins
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: hostName
                    value: string
                  - name: httpPort
                    value: integer
                  - name: httpsPort
                    value: integer
                  - name: originHostHeader
                    value: string
                  - name: priority
                    value: integer
                  - name: weight
                    value: integer
                  - name: enabled
                    value: boolean
                  - name: privateLinkAlias
                    value: string
                  - name: privateLinkResourceId
                    value: string
                  - name: privateLinkLocation
                    value: string
                  - name: privateLinkApprovalMessage
                    value: string
                  - name: privateEndpointStatus
                    value: []
        - name: originGroups
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: healthProbeSettings
                    value:
                      - name: probePath
                        value: string
                      - name: probeRequestType
                        value: string
                      - name: probeProtocol
                        value: string
                      - name: probeIntervalInSeconds
                        value: integer
                  - name: origins
                    value:
                      - - name: id
                          value: string
                  - name: trafficRestorationTimeToHealedOrNewEndpointsInMinutes
                    value: integer
                  - name: responseBasedOriginErrorDetectionSettings
                    value:
                      - name: responseBasedDetectedErrorTypes
                        value: string
                      - name: responseBasedFailoverThresholdPercentage
                        value: integer
                      - name: httpErrorRanges
                        value:
                          - - name: begin
                              value: integer
                            - name: end
                              value: integer
        - name: customDomains
          value:
            - - name: name
                value: string
              - name: properties
                value:
                  - name: hostName
                    value: string
                  - name: validationData
                    value: string
        - name: resourceState
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
UPDATE azure.cdn.endpoints
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.endpoints
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
