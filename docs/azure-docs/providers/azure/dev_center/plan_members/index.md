---
title: plan_members
hide_title: false
hide_table_of_contents: false
keywords:
  - plan_members
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>plan_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plan_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.plan_members" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plan_members', value: 'view', },
        { label: 'plan_members', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="memberName" /> | `text` | field from the `properties` object |
| <CopyableCode code="member_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="member_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="planName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sync_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the devcenter plan member. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Gets a devcenter plan member. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="planName, resourceGroupName, subscriptionId" /> | Lists all of the members assigned to a devcenter plan. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Creates or updates a devcenter plan member resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Deletes a devcenter plan member |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="memberName, planName, resourceGroupName, subscriptionId" /> | Partially updates a devcenter plan member. |

## `SELECT` examples

Lists all of the members assigned to a devcenter plan.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_plan_members', value: 'view', },
        { label: 'plan_members', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
memberName,
member_id,
member_type,
planName,
provisioning_state,
resourceGroupName,
subscriptionId,
sync_status,
system_data,
tags,
type
FROM azure.dev_center.vw_plan_members
WHERE planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
tags,
type
FROM azure.dev_center.plan_members
WHERE planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plan_members</code> resource.

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
INSERT INTO azure.dev_center.plan_members (
memberName,
planName,
resourceGroupName,
subscriptionId,
properties,
tags
)
SELECT 
'{{ memberName }}',
'{{ planName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}'
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
    - name: properties
      value:
        - name: memberId
          value: string
        - name: memberType
          value: string
        - name: syncStatus
          value:
            - name: syncState
              value: string
            - name: lastSyncError
              value:
                - name: code
                  value: string
                - name: message
                  value: string
                - name: target
                  value: string
                - name: details
                  value:
                    - - name: code
                        value: string
                      - name: message
                        value: string
                      - name: target
                        value: string
                      - name: details
                        value:
                          - - name: code
                              value: string
                            - name: message
                              value: string
                            - name: target
                              value: string
                            - name: details
                              value:
                                - - name: code
                                    value: string
                                  - name: message
                                    value: string
                                  - name: target
                                    value: string
                                  - name: details
                                    value:
                                      - - name: code
                                          value: string
                                        - name: message
                                          value: string
                                        - name: target
                                          value: string
                                        - name: details
                                          value:
                                            - - name: code
                                                value: string
                                              - name: message
                                                value: string
                                              - name: target
                                                value: string
                                              - name: details
                                                value:
                                                  - - name: code
                                                      value: string
                                                    - name: message
                                                      value: string
                                                    - name: target
                                                      value: string
                                                    - name: details
                                                      value:
                                                        - - name: code
                                                            value: string
                                                          - name: message
                                                            value: string
                                                          - name: target
                                                            value: string
                                                          - name: details
                                                            value:
                                                              - []
                                                          - name: additionalInfo
                                                            value:
                                                              - []
                                                    - name: additionalInfo
                                                      value:
                                                        - - name: type
                                                            value: string
                                                          - name: info
                                                            value: object
                                              - name: additionalInfo
                                                value:
                                                  - - name: type
                                                      value: string
                                                    - name: info
                                                      value: object
                                        - name: additionalInfo
                                          value:
                                            - - name: type
                                                value: string
                                              - name: info
                                                value: object
                                  - name: additionalInfo
                                    value:
                                      - - name: type
                                          value: string
                                        - name: info
                                          value: object
                            - name: additionalInfo
                              value:
                                - - name: type
                                    value: string
                                  - name: info
                                    value: object
                      - name: additionalInfo
                        value:
                          - - name: type
                              value: string
                            - name: info
                              value: object
                - name: additionalInfo
                  value:
                    - - name: type
                        value: string
                      - name: info
                        value: object
            - name: lastSyncTime
              value: string
        - name: tags
          value: []
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>plan_members</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.plan_members
SET 
tags = '{{ tags }}'
WHERE 
memberName = '{{ memberName }}'
AND planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>plan_members</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.plan_members
WHERE memberName = '{{ memberName }}'
AND planName = '{{ planName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
