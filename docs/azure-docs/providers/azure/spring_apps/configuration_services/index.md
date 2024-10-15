---
title: configuration_services
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_services
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

Creates, updates, deletes, gets or lists a <code>configuration_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.configuration_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_services', value: 'view', },
        { label: 'configuration_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="instances" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_requests" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Application Configuration Service properties payload |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Configuration Service and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Application Configuration Service or update the existing Application Configuration Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Application Configuration Service. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Check if the Application Configuration Service settings are valid. |
| <CopyableCode code="validate_resource" /> | `EXEC` | <CopyableCode code="configurationServiceName, resourceGroupName, serviceName, subscriptionId" /> | Check if the Application Configuration Service resource is valid. |

## `SELECT` examples

Handles requests to list all resources in a Service.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_services', value: 'view', },
        { label: 'configuration_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationServiceName,
generation,
instances,
provisioning_state,
resourceGroupName,
resource_requests,
serviceName,
settings,
subscriptionId
FROM azure.spring_apps.vw_configuration_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.spring_apps.configuration_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_services</code> resource.

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
INSERT INTO azure.spring_apps.configuration_services (
configurationServiceName,
resourceGroupName,
serviceName,
subscriptionId,
properties
)
SELECT 
'{{ configurationServiceName }}',
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
        - name: generation
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
        - name: settings
          value:
            - name: gitProperty
              value:
                - name: repositories
                  value: []
            - name: refreshIntervalInSeconds
              value: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>configuration_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.spring_apps.configuration_services
WHERE configurationServiceName = '{{ configurationServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
