---
title: public_cloud_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - public_cloud_connectors
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>public_cloud_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_cloud_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.public_cloud_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_cloud_connectors', value: 'view', },
        { label: 'public_cloud_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aws_cloud_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="connector_primary_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicCloudConnector" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of public cloud connectors. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publicCloudConnector, resourceGroupName, subscriptionId" /> | Get a PublicCloudConnector |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List PublicCloudConnector resources by resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List PublicCloudConnector resources by subscription ID |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="publicCloudConnector, resourceGroupName, subscriptionId" /> | Create a PublicCloudConnector |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="publicCloudConnector, resourceGroupName, subscriptionId" /> | Delete a PublicCloudConnector |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="publicCloudConnector, resourceGroupName, subscriptionId" /> | Update a PublicCloudConnector |
| <CopyableCode code="test_permissions" /> | `EXEC` | <CopyableCode code="publicCloudConnector, resourceGroupName, subscriptionId" /> | A long-running resource action. |

## `SELECT` examples

List PublicCloudConnector resources by subscription ID

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_cloud_connectors', value: 'view', },
        { label: 'public_cloud_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aws_cloud_profile,
connector_primary_identifier,
host_type,
location,
provisioning_state,
publicCloudConnector,
resourceGroupName,
subscriptionId,
tags
FROM azure.hybrid_connectivity.vw_public_cloud_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.hybrid_connectivity.public_cloud_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>public_cloud_connectors</code> resource.

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
INSERT INTO azure.hybrid_connectivity.public_cloud_connectors (
publicCloudConnector,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ publicCloudConnector }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
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
        - name: awsCloudProfile
          value:
            - name: accountId
              value: string
            - name: excludedAccounts
              value:
                - string
            - name: isOrganizationalAccount
              value: boolean
        - name: hostType
          value: []
        - name: provisioningState
          value: []
        - name: connectorPrimaryIdentifier
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>public_cloud_connectors</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_connectivity.public_cloud_connectors
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
publicCloudConnector = '{{ publicCloudConnector }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>public_cloud_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_connectivity.public_cloud_connectors
WHERE publicCloudConnector = '{{ publicCloudConnector }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
