---
title: dev_tool_portals
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_tool_portals
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

Creates, updates, deletes, gets or lists a <code>dev_tool_portals</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_tool_portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.dev_tool_portals" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_tool_portals', value: 'view', },
        { label: 'dev_tool_portals', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="components" /> | `text` | field from the `properties` object |
| <CopyableCode code="devToolPortalName" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sso_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="url" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Dev Tool Portal properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Live  and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Dev Tool Portal or update the existing Dev Tool Portal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Dev Tool Portal. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_tool_portals', value: 'view', },
        { label: 'dev_tool_portals', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
components,
devToolPortalName,
features,
provisioning_state,
public,
resourceGroupName,
serviceName,
sso_properties,
subscriptionId,
url
FROM azure.spring_apps.vw_dev_tool_portals
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.dev_tool_portals
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dev_tool_portals</code> resource.

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
INSERT INTO azure.spring_apps.dev_tool_portals (
devToolPortalName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ devToolPortalName }}',
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
        - name: provisioningState
          value: string
        - name: components
          value:
            - - name: name
                value: string
              - name: resourceRequests
                value:
                  - name: cpu
                    value: string
                  - name: memory
                    value: string
                  - name: instanceCount
                    value: integer
              - name: instances
                value:
                  - - name: name
                      value: string
                    - name: status
                      value: string
        - name: public
          value: boolean
        - name: url
          value: string
        - name: ssoProperties
          value:
            - name: scopes
              value:
                - string
            - name: clientId
              value: string
            - name: clientSecret
              value: string
            - name: metadataUrl
              value: string
        - name: features
          value:
            - name: applicationAccelerator
              value:
                - name: state
                  value: string
                - name: route
                  value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>dev_tool_portals</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.dev_tool_portals
WHERE devToolPortalName = '{{ devToolPortalName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
