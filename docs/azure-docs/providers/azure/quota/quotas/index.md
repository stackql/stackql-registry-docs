---
title: quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - quotas
  - quota
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

Creates, updates, deletes, gets or lists a <code>quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="is_quota_applicable" /> | `text` | field from the `properties` object |
| <CopyableCode code="limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Quota properties for the specified resource. |
| <CopyableCode code="quota_period" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="unit" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | Quota properties for the specified resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceName, scope" /> | Get the quota limit of a resource. The response can be used to determine the remaining quota to calculate a new quota limit that can be submitted with a PUT request. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceName, scope" /> | Create or update the quota limit for the specified resource with the requested value. To update the quota, follow these steps:
1. Use the GET operation for quotas and usages to determine how much quota remains for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670).
2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceName, scope" /> | Update the quota limit for a specific resource to the specified value:
1. Use the Usages-GET and Quota-GET operations to determine the remaining quota for the specific resource and to calculate the new quota limit. These steps are detailed in [this example](https://techcommunity.microsoft.com/t5/azure-governance-and-management/using-the-new-quota-rest-api/ba-p/2183670).
2. Use this PUT operation to update the quota limit. Please check the URI in location header for the detailed status of the request. |

## `SELECT` examples

Get a list of current quota limits of all resources for the specified scope. The response from this GET operation can be leveraged to submit requests to update a quota.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_quotas', value: 'view', },
        { label: 'quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
is_quota_applicable,
limit,
properties,
quota_period,
resourceName,
resource_type,
scope,
type,
unit
FROM azure.quota.vw_quotas
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.quota.quotas
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>quotas</code> resource.

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
INSERT INTO azure.quota.quotas (
resourceName,
scope,
properties
)
SELECT 
'{{ resourceName }}',
'{{ scope }}',
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
    - name: type
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: limit
          value:
            - name: limitObjectType
              value: []
        - name: unit
          value: string
        - name: name
          value:
            - name: value
              value: string
            - name: localizedValue
              value: string
        - name: resourceType
          value: []
        - name: quotaPeriod
          value: string
        - name: isQuotaApplicable
          value: boolean
        - name: properties
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>quotas</code> resource.

```sql
/*+ update */
UPDATE azure.quota.quotas
SET 
properties = '{{ properties }}'
WHERE 
resourceName = '{{ resourceName }}'
AND scope = '{{ scope }}';
```
