---
title: integration_service_environment_managed_apis
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environment_managed_apis
  - logic_apps
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

Creates, updates, deletes, gets or lists a <code>integration_service_environment_managed_apis</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_service_environment_managed_apis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.integration_service_environment_managed_apis" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_service_environment_managed_apis', value: 'view', },
        { label: 'integration_service_environment_managed_apis', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="apiName" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_definition_url" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_definitions" /> | `text` | field from the `properties` object |
| <CopyableCode code="backend_service" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="general_information" /> | `text` | field from the `properties` object |
| <CopyableCode code="integrationServiceEnvironmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_service_environment" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroup" /> | `text` | field from the `properties` object |
| <CopyableCode code="runtime_urls" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The integration service environment managed api properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the integration service environment managed Api. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Gets the integration service environment managed Apis. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Deletes the integration service environment managed Api. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="apiName, integrationServiceEnvironmentName, resourceGroup, subscriptionId" /> | Puts the integration service environment managed Api. |

## `SELECT` examples

Gets the integration service environment managed Apis.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_integration_service_environment_managed_apis', value: 'view', },
        { label: 'integration_service_environment_managed_apis', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
apiName,
api_definition_url,
api_definitions,
backend_service,
capabilities,
category,
connection_parameters,
deployment_parameters,
general_information,
integrationServiceEnvironmentName,
integration_service_environment,
location,
metadata,
policies,
provisioning_state,
resourceGroup,
runtime_urls,
subscriptionId,
tags,
type
FROM azure.logic_apps.vw_integration_service_environment_managed_apis
WHERE integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.logic_apps.integration_service_environment_managed_apis
WHERE integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>integration_service_environment_managed_apis</code> resource.

```sql
/*+ update */
REPLACE azure.logic_apps.integration_service_environment_managed_apis
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
apiName = '{{ apiName }}'
AND integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>integration_service_environment_managed_apis</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.integration_service_environment_managed_apis
WHERE apiName = '{{ apiName }}'
AND integrationServiceEnvironmentName = '{{ integrationServiceEnvironmentName }}'
AND resourceGroup = '{{ resourceGroup }}'
AND subscriptionId = '{{ subscriptionId }}';
```
