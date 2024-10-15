---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
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

Creates, updates, deletes, gets or lists a <code>workflows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id. |
| <CopyableCode code="name" /> | `text` | Gets the resource name. |
| <CopyableCode code="access_control" /> | `text` | field from the `properties` object |
| <CopyableCode code="access_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="changed_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="definition" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoints_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity properties. |
| <CopyableCode code="integration_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="integration_service_environment" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The resource location. |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The resource tags. |
| <CopyableCode code="type" /> | `text` | Gets the resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workflowName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="identity" /> | `object` | Managed service identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The workflow properties. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Gets a workflow. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of workflows by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of workflows by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Creates or updates a workflow. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Deletes a workflow. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Updates a workflow. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Disables a workflow. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Enables a workflow. |
| <CopyableCode code="generate_upgraded_definition" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Generates the upgraded definition for a workflow. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Moves an existing workflow. |
| <CopyableCode code="regenerate_access_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Regenerates the callback URL access key for request triggers. |
| <CopyableCode code="validate_by_location" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, workflowName" /> | Validates the workflow definition. |
| <CopyableCode code="validate_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workflowName" /> | Validates the workflow. |

## `SELECT` examples

Gets a list of workflows by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workflows', value: 'view', },
        { label: 'workflows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
access_control,
access_endpoint,
changed_time,
created_time,
definition,
endpoints_configuration,
identity,
integration_account,
integration_service_environment,
location,
parameters,
provisioning_state,
resourceGroupName,
sku,
state,
subscriptionId,
tags,
type,
version,
workflowName
FROM azure.logic_apps.vw_workflows
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type
FROM azure.logic_apps.workflows
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workflows</code> resource.

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
INSERT INTO azure.logic_apps.workflows (
resourceGroupName,
subscriptionId,
workflowName,
properties,
identity,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workflowName }}',
'{{ properties }}',
'{{ identity }}',
'{{ location }}',
'{{ tags }}'
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
          value: []
        - name: createdTime
          value: string
        - name: changedTime
          value: string
        - name: state
          value: []
        - name: version
          value: string
        - name: accessEndpoint
          value: string
        - name: endpointsConfiguration
          value:
            - name: workflow
              value:
                - name: outgoingIpAddresses
                  value:
                    - - name: address
                        value: string
                - name: accessEndpointIpAddresses
                  value:
                    - - name: address
                        value: string
        - name: accessControl
          value:
            - name: triggers
              value:
                - name: allowedCallerIpAddresses
                  value:
                    - - name: addressRange
                        value: string
                - name: openAuthenticationPolicies
                  value:
                    - name: policies
                      value: object
        - name: sku
          value:
            - name: name
              value: []
            - name: plan
              value:
                - name: id
                  value: string
                - name: name
                  value: string
                - name: type
                  value: string
        - name: definition
          value: []
        - name: parameters
          value: object
    - name: identity
      value:
        - name: type
          value: string
        - name: tenantId
          value: string
        - name: principalId
          value: string
        - name: userAssignedIdentities
          value: object
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workflows</code> resource.

```sql
/*+ update */
UPDATE azure.logic_apps.workflows
SET 

WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```

## `DELETE` example

Deletes the specified <code>workflows</code> resource.

```sql
/*+ delete */
DELETE FROM azure.logic_apps.workflows
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```
