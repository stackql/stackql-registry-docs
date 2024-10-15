---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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

Creates, updates, deletes, gets or lists a <code>routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.routes" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routes', value: 'view', },
        { label: 'routes', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cache_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_domains" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="forwarding_protocol" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_redirect" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_to_default_domain" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="origin_path" /> | `text` | field from the `properties` object |
| <CopyableCode code="patterns_to_match" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_sets" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_protocols" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The JSON object that contains the properties of the Routes to create. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="list_by_endpoint" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> | Lists all of the existing origins within a profile. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Creates a new route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Deletes an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="endpointName, profileName, resourceGroupName, routeName, subscriptionId" /> | Updates an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |

## `SELECT` examples

Lists all of the existing origins within a profile.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routes', value: 'view', },
        { label: 'routes', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cache_configuration,
custom_domains,
deployment_status,
enabled_state,
endpointName,
endpoint_name,
forwarding_protocol,
https_redirect,
link_to_default_domain,
origin_group,
origin_path,
patterns_to_match,
profileName,
provisioning_state,
resourceGroupName,
routeName,
rule_sets,
subscriptionId,
supported_protocols
FROM azure.cdn.vw_routes
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.cdn.routes
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routes</code> resource.

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
INSERT INTO azure.cdn.routes (
endpointName,
profileName,
resourceGroupName,
routeName,
subscriptionId,
properties
)
SELECT 
'{{ endpointName }}',
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ routeName }}',
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
        - name: endpointName
          value: string
        - name: customDomains
          value:
            - - name: id
                value: string
              - name: isActive
                value: boolean
        - name: originGroup
          value:
            - name: id
              value: string
        - name: originPath
          value: string
        - name: ruleSets
          value:
            - - name: id
                value: string
        - name: supportedProtocols
          value:
            - []
        - name: patternsToMatch
          value:
            - string
        - name: cacheConfiguration
          value:
            - name: queryStringCachingBehavior
              value: string
            - name: queryParameters
              value: string
            - name: compressionSettings
              value:
                - name: contentTypesToCompress
                  value:
                    - string
                - name: isCompressionEnabled
                  value: boolean
        - name: forwardingProtocol
          value: string
        - name: linkToDefaultDomain
          value: string
        - name: httpsRedirect
          value: string
        - name: enabledState
          value: string
        - name: provisioningState
          value: string
        - name: deploymentStatus
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>routes</code> resource.

```sql
/*+ update */
UPDATE azure.cdn.routes
SET 
properties = '{{ properties }}'
WHERE 
endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND routeName = '{{ routeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>routes</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cdn.routes
WHERE endpointName = '{{ endpointName }}'
AND profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND routeName = '{{ routeName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
