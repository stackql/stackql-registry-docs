---
title: batch_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_deployments
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>batch_deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>batch_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.batch_deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_batch_deployments', value: 'view', },
        { label: 'batch_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="code_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="compute" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployment_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpointName" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_variables" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_threshold" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `text` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="logging_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_concurrency_per_instance" /> | `text` | field from the `properties` object |
| <CopyableCode code="mini_batch_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_action" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_file_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Batch inference settings per deployment. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="retry_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Batch inference settings per deployment. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_batch_deployments', value: 'view', },
        { label: 'batch_deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
code_configuration,
compute,
deploymentName,
deployment_configuration,
endpointName,
environment_id,
environment_variables,
error_threshold,
identity,
kind,
location,
logging_level,
max_concurrency_per_instance,
mini_batch_size,
model,
output_action,
output_file_name,
properties,
provisioning_state,
resourceGroupName,
resources,
retry_settings,
sku,
subscriptionId,
tags,
workspaceName
FROM azure.ml_services.vw_batch_deployments
WHERE endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
sku,
tags
FROM azure.ml_services.batch_deployments
WHERE endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>batch_deployments</code> resource.

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
INSERT INTO azure.ml_services.batch_deployments (
deploymentName,
endpointName,
resourceGroupName,
subscriptionId,
workspaceName,
data__location,
data__properties,
tags,
location,
identity,
kind,
properties,
sku
)
SELECT 
'{{ deploymentName }}',
'{{ endpointName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ identity }}',
'{{ kind }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: kind
      value: string
    - name: properties
      value:
        - name: codeConfiguration
          value:
            - name: codeId
              value: string
            - name: scoringScript
              value: string
        - name: description
          value: string
        - name: environmentId
          value: string
        - name: environmentVariables
          value: object
        - name: properties
          value: object
        - name: compute
          value: string
        - name: deploymentConfiguration
          value:
            - name: deploymentConfigurationType
              value: []
        - name: errorThreshold
          value: integer
        - name: loggingLevel
          value: []
        - name: maxConcurrencyPerInstance
          value: integer
        - name: miniBatchSize
          value: integer
        - name: model
          value:
            - name: referenceType
              value: []
        - name: outputAction
          value: []
        - name: outputFileName
          value: string
        - name: provisioningState
          value: []
        - name: resources
          value:
            - name: instanceCount
              value: integer
            - name: instanceType
              value: string
            - name: properties
              value: object
        - name: retrySettings
          value:
            - name: maxRetries
              value: integer
            - name: timeout
              value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: []
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>batch_deployments</code> resource.

```sql
/*+ update */
UPDATE azure.ml_services.batch_deployments
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
deploymentName = '{{ deploymentName }}'
AND endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>batch_deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.batch_deployments
WHERE deploymentName = '{{ deploymentName }}'
AND endpointName = '{{ endpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
