---
title: application_live_views
hide_title: false
hide_table_of_contents: false
keywords:
  - application_live_views
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

Creates, updates, deletes, gets or lists a <code>application_live_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_live_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.application_live_views" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_live_views', value: 'view', },
        { label: 'application_live_views', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applicationLiveViewName" /> | `text` | field from the `properties` object |
| <CopyableCode code="components" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application Live View properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Live  and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Application Live View or update the existing Application Live View. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationLiveViewName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Application Live View. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_application_live_views', value: 'view', },
        { label: 'application_live_views', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
applicationLiveViewName,
components,
provisioning_state,
resourceGroupName,
serviceName,
subscriptionId
FROM azure.spring_apps.vw_application_live_views
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.application_live_views
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_live_views</code> resource.

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
INSERT INTO azure.spring_apps.application_live_views (
applicationLiveViewName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ applicationLiveViewName }}',
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>application_live_views</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.application_live_views
WHERE applicationLiveViewName = '{{ applicationLiveViewName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
