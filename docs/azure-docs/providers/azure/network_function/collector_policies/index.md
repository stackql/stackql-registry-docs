---
title: collector_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - collector_policies
  - network_function
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

Creates, updates, deletes, gets or lists a <code>collector_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>collector_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network_function.collector_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_collector_policies', value: 'view', },
        { label: 'collector_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="azureTrafficCollectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="collectorPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="emission_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ingestion_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Collection policy properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Gets the collector policy in a specified Traffic Collector |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="azureTrafficCollectorName, resourceGroupName, subscriptionId" /> | Return list of Collector policies in a Azure Traffic Collector |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Creates or updates a Collector Policy resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Deletes a specified Collector Policy resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId" /> | Updates the specified Collector Policy tags. |

## `SELECT` examples

Return list of Collector policies in a Azure Traffic Collector

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_collector_policies', value: 'view', },
        { label: 'collector_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azureTrafficCollectorName,
collectorPolicyName,
emission_policies,
etag,
ingestion_policy,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type
FROM azure.network_function.vw_collector_policies
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
systemData,
tags,
type
FROM azure.network_function.collector_policies
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>collector_policies</code> resource.

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
INSERT INTO azure.network_function.collector_policies (
azureTrafficCollectorName,
collectorPolicyName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ azureTrafficCollectorName }}',
'{{ collectorPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: ingestionPolicy
          value:
            - name: ingestionType
              value: string
            - name: ingestionSources
              value:
                - - name: sourceType
                    value: string
                  - name: resourceId
                    value: string
        - name: emissionPolicies
          value:
            - - name: emissionType
                value: string
              - name: emissionDestinations
                value:
                  - - name: destinationType
                      value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
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
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>collector_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network_function.collector_policies
WHERE azureTrafficCollectorName = '{{ azureTrafficCollectorName }}'
AND collectorPolicyName = '{{ collectorPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
