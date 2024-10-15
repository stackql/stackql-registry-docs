---
title: service_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - service_endpoints
  - intelligent_recommendations
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

Creates, updates, deletes, gets or lists a <code>service_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.intelligent_recommendations.service_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | ServiceEndpoint resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Returns ServiceEndpoint resources for a given name. |
| <CopyableCode code="list_by_account_resource" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Returns list of ServiceEndpoint resources for a given Account name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Creates or updates ServiceEndpoint resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Deletes ServiceEndpoint resources of a given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, resourceGroupName, serviceEndpointName, subscriptionId" /> | Updates ServiceEndpoint resource details. |

## `SELECT` examples

Returns list of ServiceEndpoint resources for a given Account name.


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure_extras.intelligent_recommendations.service_endpoints
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_endpoints</code> resource.

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
INSERT INTO azure_extras.intelligent_recommendations.service_endpoints (
accountName,
resourceGroupName,
serviceEndpointName,
subscriptionId,
tags,
location,
properties,
systemData
)
SELECT 
'{{ accountName }}',
'{{ resourceGroupName }}',
'{{ serviceEndpointName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ systemData }}'
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
    - name: properties
      value:
        - name: preAllocatedCapacity
          value: integer
        - name: pairedLocation
          value: string
        - name: url
          value: string
        - name: provisioningState
          value: string
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure_extras.intelligent_recommendations.service_endpoints
SET 
tags = '{{ tags }}'
WHERE 
accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceEndpointName = '{{ serviceEndpointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>service_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.intelligent_recommendations.service_endpoints
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceEndpointName = '{{ serviceEndpointName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
