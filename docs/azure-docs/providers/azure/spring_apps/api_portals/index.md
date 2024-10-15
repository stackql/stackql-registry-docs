---
title: api_portals
hide_title: false
hide_table_of_contents: false
keywords:
  - api_portals
  - spring_apps
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

Creates, updates, deletes, gets or lists a <code>api_portals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.api_portals" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_portals', value: 'view', },
        { label: 'api_portals', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiPortalName" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_try_out_enabled_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="gateway_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="https_only" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Sku of Azure Spring Apps |
| <CopyableCode code="source_urls" /> | `text` | field from the `properties` object |
| <CopyableCode code="sso_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | API portal properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId" /> | Get the API portal and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId" /> | Create the default API portal or update the existing API portal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId" /> | Delete the default API portal. |
| <CopyableCode code="validate_domain" /> | `EXEC` | <CopyableCode code="apiPortalName, resourceGroupName, serviceName, subscriptionId, data__name" /> | Check the domains are valid as well as not in use. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_api_portals', value: 'view', },
        { label: 'api_portals', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiPortalName,
api_try_out_enabled_state,
gateway_ids,
https_only,
instances,
provisioning_state,
public,
resourceGroupName,
resource_requests,
serviceName,
sku,
source_urls,
sso_properties,
subscriptionId,
url
FROM azure.spring_apps.vw_api_portals
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
sku
FROM azure.spring_apps.api_portals
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_portals</code> resource.

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
INSERT INTO azure.spring_apps.api_portals (
apiPortalName,
resourceGroupName,
serviceName,
subscriptionId,
properties,
sku
)
SELECT 
'{{ apiPortalName }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: public
          value: boolean
        - name: url
          value: string
        - name: httpsOnly
          value: boolean
        - name: gatewayIds
          value:
            - string
        - name: sourceUrls
          value:
            - string
        - name: ssoProperties
          value:
            - name: scope
              value:
                - string
            - name: clientId
              value: string
            - name: clientSecret
              value: string
            - name: issuerUri
              value: string
        - name: resourceRequests
          value:
            - name: cpu
              value: string
            - name: memory
              value: string
        - name: instances
          value:
            - - name: name
                value: string
              - name: status
                value: string
        - name: apiTryOutEnabledState
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>api_portals</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.api_portals
WHERE apiPortalName = '{{ apiPortalName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
