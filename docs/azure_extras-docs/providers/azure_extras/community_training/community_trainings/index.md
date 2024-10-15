---
title: community_trainings
hide_title: false
hide_table_of_contents: false
keywords:
  - community_trainings
  - community_training
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

Creates, updates, deletes, gets or lists a <code>community_trainings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>community_trainings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.community_training.community_trainings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_trainings', value: 'view', },
        { label: 'community_trainings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="communityTrainingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disaster_recovery_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="portal_admin_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_owner_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="portal_owner_organization_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The resource model definition representing SKU |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="zone_redundancy_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of the Community CommunityTraining. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Get a CommunityTraining |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List CommunityTraining resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List CommunityTraining resources by subscription ID |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Create a CommunityTraining |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Delete a CommunityTraining |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="communityTrainingName, resourceGroupName, subscriptionId" /> | Update a CommunityTraining |

## `SELECT` examples

List CommunityTraining resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_trainings', value: 'view', },
        { label: 'community_trainings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
communityTrainingName,
disaster_recovery_enabled,
identity_configuration,
location,
portal_admin_email_address,
portal_name,
portal_owner_email_address,
portal_owner_organization_name,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
zone_redundancy_enabled
FROM azure_extras.community_training.vw_community_trainings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure_extras.community_training.community_trainings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>community_trainings</code> resource.

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
INSERT INTO azure_extras.community_training.community_trainings (
communityTrainingName,
resourceGroupName,
subscriptionId,
properties,
sku,
tags,
location
)
SELECT 
'{{ communityTrainingName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ sku }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: portalName
          value: string
        - name: portalAdminEmailAddress
          value: string
        - name: portalOwnerOrganizationName
          value: string
        - name: portalOwnerEmailAddress
          value: string
        - name: identityConfiguration
          value:
            - name: identityType
              value: string
            - name: teamsEnabled
              value: boolean
            - name: tenantId
              value: string
            - name: domainName
              value: string
            - name: clientId
              value: string
            - name: clientSecret
              value: string
            - name: b2cAuthenticationPolicy
              value: string
            - name: b2cPasswordResetPolicy
              value: string
            - name: customLoginParameters
              value: string
        - name: zoneRedundancyEnabled
          value: boolean
        - name: disasterRecoveryEnabled
          value: boolean
        - name: provisioningState
          value: []
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
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>community_trainings</code> resource.

```sql
/*+ update */
UPDATE azure_extras.community_training.community_trainings
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
communityTrainingName = '{{ communityTrainingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>community_trainings</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.community_training.community_trainings
WHERE communityTrainingName = '{{ communityTrainingName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
