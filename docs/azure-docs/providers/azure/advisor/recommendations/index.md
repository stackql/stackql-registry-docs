---
title: recommendations
hide_title: false
hide_table_of_contents: false
keywords:
  - recommendations
  - advisor
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

Creates, updates, deletes, gets or lists a <code>recommendations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recommendations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.advisor.recommendations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommendations', value: 'view', },
        { label: 'recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="exposed_metadata_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="impact" /> | `text` | field from the `properties` object |
| <CopyableCode code="impacted_field" /> | `text` | field from the `properties` object |
| <CopyableCode code="impacted_value" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_updated" /> | `text` | field from the `properties` object |
| <CopyableCode code="learn_more_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="potential_benefits" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommendation_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="remediation" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="risk" /> | `text` | field from the `properties` object |
| <CopyableCode code="short_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suppression_ids" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The properties of the recommendation. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="recommendationId, resourceUri" /> | Obtains details of a cached recommendation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations. |
| <CopyableCode code="exec_get_generate_status" /> | `EXEC` | <CopyableCode code="operationId, subscriptionId" /> | Retrieves the status of the recommendation computation or generation process. Invoke this API after calling the generation recommendation. The URI of this API is returned in the Location field of the response header. |
| <CopyableCode code="generate" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Initiates the recommendation generation or computation process for a subscription. This operation is asynchronous. The generated recommendations are stored in a cache in the Advisor service. |
| <CopyableCode code="predict" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples

Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recommendations', value: 'view', },
        { label: 'recommendations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
actions,
category,
exposed_metadata_properties,
extended_properties,
impact,
impacted_field,
impacted_value,
label,
last_updated,
learn_more_link,
metadata,
potential_benefits,
recommendationId,
recommendation_type_id,
remediation,
resourceUri,
resource_metadata,
risk,
short_description,
subscriptionId,
suppression_ids,
system_data,
type
FROM azure.advisor.vw_recommendations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.advisor.recommendations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

