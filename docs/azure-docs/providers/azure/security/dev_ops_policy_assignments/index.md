---
title: dev_ops_policy_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_ops_policy_assignments
  - security
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

Creates, updates, deletes, gets or lists a <code>dev_ops_policy_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_ops_policy_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.dev_ops_policy_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_ops_policy_assignments', value: 'view', },
        { label: 'dev_ops_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assigned_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="descendant_behavior" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyAssignmentId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_status_update_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="securityConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of the DevOps policy assignment resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyAssignmentId, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceId, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyAssignmentId, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyAssignmentId, resourceGroupName, securityConnectorName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="policyAssignmentId, resourceGroupName, securityConnectorName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dev_ops_policy_assignments', value: 'view', },
        { label: 'dev_ops_policy_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
assigned_at,
descendant_behavior,
policy,
policyAssignmentId,
provisioning_state,
provisioning_status_message,
provisioning_status_update_time_utc,
resourceGroupName,
resourceId,
resource_id,
securityConnectorName,
subscriptionId,
system_data
FROM azure.security.vw_dev_ops_policy_assignments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceId = '{{ resourceId }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.security.dev_ops_policy_assignments
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceId = '{{ resourceId }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dev_ops_policy_assignments</code> resource.

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
INSERT INTO azure.security.dev_ops_policy_assignments (
policyAssignmentId,
resourceGroupName,
securityConnectorName,
subscriptionId,
systemData,
properties
)
SELECT 
'{{ policyAssignmentId }}',
'{{ resourceGroupName }}',
'{{ securityConnectorName }}',
'{{ subscriptionId }}',
'{{ systemData }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
        - name: provisioningStatusMessage
          value: string
        - name: provisioningStatusUpdateTimeUtc
          value: string
        - name: provisioningState
          value: []
        - name: resourceId
          value: string
        - name: descendantBehavior
          value: []
        - name: policy
          value:
            - name: policyName
              value: string
            - name: policyId
              value: string
            - name: policyVersion
              value: string
            - name: policyType
              value: []
        - name: assignedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dev_ops_policy_assignments</code> resource.

```sql
/*+ update */
UPDATE azure.security.dev_ops_policy_assignments
SET 
systemData = '{{ systemData }}',
properties = '{{ properties }}'
WHERE 
policyAssignmentId = '{{ policyAssignmentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dev_ops_policy_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.dev_ops_policy_assignments
WHERE policyAssignmentId = '{{ policyAssignmentId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
