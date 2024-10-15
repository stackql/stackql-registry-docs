---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - traffic_manager
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_endpoint_record_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="dns_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="max_return" /> | `text` | field from the `properties` object |
| <CopyableCode code="monitor_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="profileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="profile_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="traffic_routing_method" /> | `text` | field from the `properties` object |
| <CopyableCode code="traffic_view_enrollment_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Traffic Manager profile properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Gets a Traffic Manager profile. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Traffic Manager profiles within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Traffic Manager profiles within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Create or update a Traffic Manager profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Deletes a Traffic Manager profile. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Update a Traffic Manager profile. |
| <CopyableCode code="check_traffic_manager_name_availability_v2" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks the availability of a Traffic Manager Relative DNS name. |
| <CopyableCode code="check_traffic_manager_relative_dns_name_availability" /> | `EXEC` | <CopyableCode code="" /> | Checks the availability of a Traffic Manager Relative DNS name. |

## `SELECT` examples

Lists all Traffic Manager profiles within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allowed_endpoint_record_types,
dns_config,
endpoints,
location,
max_return,
monitor_config,
profileName,
profile_status,
resourceGroupName,
subscriptionId,
tags,
traffic_routing_method,
traffic_view_enrollment_status
FROM azure.traffic_manager.vw_profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.traffic_manager.profiles
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO azure.traffic_manager.profiles (
profileName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ profileName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: profileStatus
          value: string
        - name: trafficRoutingMethod
          value: string
        - name: dnsConfig
          value:
            - name: relativeName
              value: string
            - name: fqdn
              value: string
            - name: ttl
              value: integer
        - name: monitorConfig
          value:
            - name: profileMonitorStatus
              value: string
            - name: protocol
              value: string
            - name: port
              value: integer
            - name: path
              value: string
            - name: intervalInSeconds
              value: integer
            - name: timeoutInSeconds
              value: integer
            - name: toleratedNumberOfFailures
              value: integer
            - name: customHeaders
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: expectedStatusCodeRanges
              value:
                - - name: min
                    value: integer
                  - name: max
                    value: integer
        - name: endpoints
          value:
            - - name: properties
                value:
                  - name: targetResourceId
                    value: string
                  - name: target
                    value: string
                  - name: endpointStatus
                    value: string
                  - name: weight
                    value: integer
                  - name: priority
                    value: integer
                  - name: endpointLocation
                    value: string
                  - name: endpointMonitorStatus
                    value: string
                  - name: minChildEndpoints
                    value: integer
                  - name: minChildEndpointsIPv4
                    value: integer
                  - name: minChildEndpointsIPv6
                    value: integer
                  - name: geoMapping
                    value:
                      - string
                  - name: subnets
                    value:
                      - - name: first
                          value: string
                        - name: last
                          value: string
                        - name: scope
                          value: integer
                  - name: customHeaders
                    value:
                      - - name: name
                          value: string
                        - name: value
                          value: string
                  - name: alwaysServe
                    value: string
        - name: trafficViewEnrollmentStatus
          value: string
        - name: allowedEndpointRecordTypes
          value:
            - []
        - name: maxReturn
          value: integer
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>profiles</code> resource.

```sql
/*+ update */
UPDATE azure.traffic_manager.profiles
SET 
properties = '{{ properties }}',
tags = '{{ tags }}',
location = '{{ location }}'
WHERE 
profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.traffic_manager.profiles
WHERE profileName = '{{ profileName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
