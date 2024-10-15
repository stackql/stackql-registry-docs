---
title: orchestrator_instance_services
hide_title: false
hide_table_of_contents: false
keywords:
  - orchestrator_instance_services
  - delegated_network
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

Creates, updates, deletes, gets or lists a <code>orchestrator_instance_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>orchestrator_instance_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.delegated_network.orchestrator_instance_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | The kind of workbook. Choices are user and shared. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of orchestrator |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The type of resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the OrchestratorInstances resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the orchestratorInstance resources in a subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a orchestrator instance |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes the Orchestrator Instance |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Update Orchestrator Instance |

## `SELECT` examples

Get all the orchestratorInstance resources in a subscription.


```sql
SELECT
id,
name,
identity,
kind,
location,
properties,
tags,
type
FROM azure.delegated_network.orchestrator_instance_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>orchestrator_instance_services</code> resource.

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
INSERT INTO azure.delegated_network.orchestrator_instance_services (
resourceGroupName,
resourceName,
subscriptionId,
location,
kind,
identity,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ kind }}',
'{{ identity }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: kind
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: resourceGuid
          value: string
        - name: provisioningState
          value: string
        - name: orchestratorAppId
          value: string
        - name: orchestratorTenantId
          value: string
        - name: clusterRootCA
          value: string
        - name: apiServerEndpoint
          value: string
        - name: privateLinkResourceId
          value: string
        - name: controllerDetails
          value:
            - name: id
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>orchestrator_instance_services</code> resource.

```sql
/*+ update */
UPDATE azure.delegated_network.orchestrator_instance_services
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>orchestrator_instance_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.delegated_network.orchestrator_instance_services
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
