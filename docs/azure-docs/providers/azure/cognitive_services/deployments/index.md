---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - cognitive_services
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

Creates, updates, deletes, gets or lists a <code>deployments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cognitive_services.deployments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="call_rate_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="capabilities" /> | `text` | field from the `properties` object |
| <CopyableCode code="capacity_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_capacity" /> | `text` | field from the `properties` object |
| <CopyableCode code="deploymentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dynamic_throttling_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Resource Etag. |
| <CopyableCode code="model" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="rai_policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="rate_limits" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scale_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version_upgrade_option" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | Properties of Cognitive Services account deployment. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, deploymentName, resourceGroupName, subscriptionId" /> | Gets the specified deployments associated with the Cognitive Services account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the deployments associated with the Cognitive Services account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, deploymentName, resourceGroupName, subscriptionId" /> | Update the state of specified deployments associated with the Cognitive Services account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, deploymentName, resourceGroupName, subscriptionId" /> | Deletes the specified deployment associated with the Cognitive Services account. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, deploymentName, resourceGroupName, subscriptionId" /> | Update specified deployments associated with the Cognitive Services account. |

## `SELECT` examples

Gets the deployments associated with the Cognitive Services account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_deployments', value: 'view', },
        { label: 'deployments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
call_rate_limit,
capabilities,
capacity_settings,
current_capacity,
deploymentName,
dynamic_throttling_enabled,
etag,
model,
provisioning_state,
rai_policy_name,
rate_limits,
resourceGroupName,
scale_settings,
sku,
subscriptionId,
system_data,
tags,
version_upgrade_option
FROM azure.cognitive_services.vw_deployments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
properties,
sku,
systemData,
tags
FROM azure.cognitive_services.deployments
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO azure.cognitive_services.deployments (
accountName,
deploymentName,
resourceGroupName,
subscriptionId,
sku,
tags,
properties
)
SELECT 
'{{ accountName }}',
'{{ deploymentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
          value: string
        - name: capacity
          value: integer
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: model
          value:
            - name: format
              value: string
            - name: name
              value: string
            - name: version
              value: string
            - name: source
              value: string
            - name: callRateLimit
              value:
                - name: count
                  value: number
                - name: renewalPeriod
                  value: number
                - name: rules
                  value:
                    - - name: key
                        value: string
                      - name: renewalPeriod
                        value: number
                      - name: count
                        value: number
                      - name: minCount
                        value: number
                      - name: dynamicThrottlingEnabled
                        value: boolean
                      - name: matchPatterns
                        value:
                          - - name: path
                              value: string
                            - name: method
                              value: string
        - name: scaleSettings
          value:
            - name: scaleType
              value: string
            - name: capacity
              value: integer
            - name: activeCapacity
              value: integer
        - name: capabilities
          value: object
        - name: raiPolicyName
          value: string
        - name: rateLimits
          value:
            - - name: key
                value: string
              - name: renewalPeriod
                value: number
              - name: count
                value: number
              - name: minCount
                value: number
              - name: dynamicThrottlingEnabled
                value: boolean
              - name: matchPatterns
                value:
                  - - name: path
                      value: string
                    - name: method
                      value: string
        - name: versionUpgradeOption
          value: string
        - name: dynamicThrottlingEnabled
          value: boolean
        - name: currentCapacity
          value: integer
        - name: capacitySettings
          value:
            - name: designatedCapacity
              value: integer
            - name: priority
              value: integer

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>deployments</code> resource.

```sql
/*+ update */
UPDATE azure.cognitive_services.deployments
SET 
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>deployments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.cognitive_services.deployments
WHERE accountName = '{{ accountName }}'
AND deploymentName = '{{ deploymentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
