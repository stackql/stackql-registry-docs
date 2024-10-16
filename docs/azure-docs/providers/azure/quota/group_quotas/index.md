---
title: group_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - group_quotas
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

Creates, updates, deletes, gets or lists a <code>group_quotas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.group_quotas" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quotas', value: 'view', },
        { label: 'group_quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="additional_attributes" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="groupQuotaName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties and filters for ShareQuota. The request parameter is optional, if there are no filters specified. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Gets the GroupQuotas for the name passed. It will return the GroupQuotas properties only. The details on group quota can be access from the group quota APIs. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="managementGroupId" /> | Lists GroupQuotas for the scope passed. It will return the GroupQuotas QuotaEntity properties only.The details on group quota can be access from the group quota APIs. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Creates a new GroupQuota for the name passed. A RequestId will be returned by the Service. The status can be polled periodically. The status Async polling is using standards defined at - https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/async-api-reference.md#asynchronous-operations. Use the OperationsStatus URI provided in Azure-AsyncOperation header, the duration will be specified in retry-after header. Once the operation gets to terminal state - Succeeded \| Failed, then the URI will change to Get URI and full details can be checked. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Deletes the GroupQuotas for the name passed. All the remaining shareQuota in the GroupQuotas will be lost. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="groupQuotaName, managementGroupId" /> | Updates the GroupQuotas for the name passed. A GroupQuotas RequestId will be returned by the Service. The status can be polled periodically. The status Async polling is using standards defined at - https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/async-api-reference.md#asynchronous-operations. Use the OperationsStatus URI provided in Azure-AsyncOperation header, the duration will be specified in retry-after header. Once the operation gets to terminal state - Succeeded \| Failed, then the URI will change to Get URI and full details can be checked. 
 Any change in the filters will be applicable to the future quota assignments, existing quota allocated to subscriptions from the GroupQuotas remains unchanged. |

## `SELECT` examples

Lists GroupQuotas for the scope passed. It will return the GroupQuotas QuotaEntity properties only.The details on group quota can be access from the group quota APIs.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_group_quotas', value: 'view', },
        { label: 'group_quotas', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
additional_attributes,
display_name,
groupQuotaName,
managementGroupId,
provisioning_state
FROM azure.quota.vw_group_quotas
WHERE managementGroupId = '{{ managementGroupId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.quota.group_quotas
WHERE managementGroupId = '{{ managementGroupId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>group_quotas</code> resource.

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
INSERT INTO azure.quota.group_quotas (
groupQuotaName,
managementGroupId,
properties
)
SELECT 
'{{ groupQuotaName }}',
'{{ managementGroupId }}',
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
        - name: displayName
          value: string
        - name: additionalAttributes
          value:
            - name: groupId
              value:
                - name: groupingIdType
                  value: []
                - name: value
                  value: string
            - name: environment
              value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>group_quotas</code> resource.

```sql
/*+ update */
UPDATE azure.quota.group_quotas
SET 
properties = '{{ properties }}'
WHERE 
groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}';
```

## `DELETE` example

Deletes the specified <code>group_quotas</code> resource.

```sql
/*+ delete */
DELETE FROM azure.quota.group_quotas
WHERE groupQuotaName = '{{ groupQuotaName }}'
AND managementGroupId = '{{ managementGroupId }}';
```
