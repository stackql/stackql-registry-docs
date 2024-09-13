---
title: region_health_check_services
hide_title: false
hide_table_of_contents: false
keywords:
  - region_health_check_services
  - compute
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

Creates, updates, deletes or gets an <code>region_health_check_service</code> resource or lists <code>region_health_check_services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_health_check_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_health_check_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| <CopyableCode code="name" /> | `string` | Name of the resource. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="fingerprint" /> | `string` | Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a HealthCheckService. An up-to-date fingerprint must be provided in order to patch/update the HealthCheckService; Otherwise, the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve the HealthCheckService. |
| <CopyableCode code="healthChecks" /> | `array` | A list of URLs to the HealthCheck resources. Must have at least one HealthCheck, and not more than 10 for regional HealthCheckService, and not more than 1 for global HealthCheckService. HealthCheck resources must have portSpecification=USE_SERVING_PORT or portSpecification=USE_FIXED_PORT. For regional HealthCheckService, the HealthCheck must be regional and in the same region. For global HealthCheckService, HealthCheck must be global. Mix of regional and global HealthChecks is not supported. Multiple regional HealthChecks must belong to the same region. Regional HealthChecks must belong to the same region as zones of NetworkEndpointGroups. For global HealthCheckService using global INTERNET_IP_PORT NetworkEndpointGroups, the global HealthChecks must specify sourceRegions, and HealthChecks that specify sourceRegions can only be used with global INTERNET_IP_PORT NetworkEndpointGroups. |
| <CopyableCode code="healthStatusAggregationPolicy" /> | `string` | Optional. Policy for how the results from multiple health checks for the same endpoint are aggregated. Defaults to NO_AGGREGATION if unspecified. - NO_AGGREGATION. An EndpointHealth message is returned for each pair in the health check service. - AND. If any health check of an endpoint reports UNHEALTHY, then UNHEALTHY is the HealthState of the endpoint. If all health checks report HEALTHY, the HealthState of the endpoint is HEALTHY. . This is only allowed with regional HealthCheckService. |
| <CopyableCode code="kind" /> | `string` | [Output only] Type of the resource. Always compute#healthCheckServicefor health check services. |
| <CopyableCode code="networkEndpointGroups" /> | `array` | A list of URLs to the NetworkEndpointGroup resources. Must not have more than 100. For regional HealthCheckService, NEGs must be in zones in the region of the HealthCheckService. For global HealthCheckServices, the NetworkEndpointGroups must be global INTERNET_IP_PORT. |
| <CopyableCode code="notificationEndpoints" /> | `array` | A list of URLs to the NotificationEndpoint resources. Must not have more than 10. A list of endpoints for receiving notifications of change in health status. For regional HealthCheckService, NotificationEndpoint must be regional and in the same region. For global HealthCheckService, NotificationEndpoint must be global. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the health check service resides. This field is not applicable to global health check services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="healthCheckService, project, region" /> | Returns the specified regional HealthCheckService resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists all the HealthCheckService resources that have been configured for the specified project in the given region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Creates a regional HealthCheckService resource in the specified project and region using the data included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="healthCheckService, project, region" /> | Deletes the specified regional HealthCheckService. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="healthCheckService, project, region" /> | Updates the specified regional HealthCheckService resource with the data included in the request. This method supports PATCH semantics and uses the JSON merge patch format and processing rules. |

## `SELECT` examples

Lists all the HealthCheckService resources that have been configured for the specified project in the given region.

```sql
SELECT
id,
name,
description,
creationTimestamp,
fingerprint,
healthChecks,
healthStatusAggregationPolicy,
kind,
networkEndpointGroups,
notificationEndpoints,
region,
selfLink
FROM google.compute.region_health_check_services
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_health_check_services</code> resource.

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
INSERT INTO google.compute.region_health_check_services (
project,
region,
kind,
id,
creationTimestamp,
selfLink,
name,
description,
region,
healthStatusAggregationPolicy,
healthChecks,
networkEndpointGroups,
notificationEndpoints,
fingerprint
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ kind }}',
'{{ id }}',
'{{ creationTimestamp }}',
'{{ selfLink }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ healthStatusAggregationPolicy }}',
'{{ healthChecks }}',
'{{ networkEndpointGroups }}',
'{{ notificationEndpoints }}',
'{{ fingerprint }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: kind
        value: '{{ kind }}'
      - name: id
        value: '{{ id }}'
      - name: creationTimestamp
        value: '{{ creationTimestamp }}'
      - name: selfLink
        value: '{{ selfLink }}'
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: region
        value: '{{ region }}'
      - name: healthStatusAggregationPolicy
        value: '{{ healthStatusAggregationPolicy }}'
      - name: healthChecks
        value: '{{ healthChecks }}'
      - name: networkEndpointGroups
        value: '{{ networkEndpointGroups }}'
      - name: notificationEndpoints
        value: '{{ notificationEndpoints }}'
      - name: fingerprint
        value: '{{ fingerprint }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a region_health_check_service only if the necessary resources are available.

```sql
UPDATE google.compute.region_health_check_services
SET 
kind = '{{ kind }}',
id = '{{ id }}',
creationTimestamp = '{{ creationTimestamp }}',
selfLink = '{{ selfLink }}',
name = '{{ name }}',
description = '{{ description }}',
region = '{{ region }}',
healthStatusAggregationPolicy = '{{ healthStatusAggregationPolicy }}',
healthChecks = '{{ healthChecks }}',
networkEndpointGroups = '{{ networkEndpointGroups }}',
notificationEndpoints = '{{ notificationEndpoints }}',
fingerprint = '{{ fingerprint }}'
WHERE 
healthCheckService = '{{ healthCheckService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```

## `DELETE` example

Deletes the specified region_health_check_service resource.

```sql
DELETE FROM google.compute.region_health_check_services
WHERE healthCheckService = '{{ healthCheckService }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
