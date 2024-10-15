---
title: partner_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>partner_namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_namespaces" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_namespaces', value: 'view', },
        { label: 'partner_namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="inbound_ip_rules" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="minimum_tls_version_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnerNamespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_registration_fully_qualified_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_topic_routing_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the partner namespace. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Get properties of a partner namespace. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner namespaces under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the partner namespaces under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Asynchronously creates a new partner namespace with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Delete existing partner namespace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | Asynchronously updates a partner namespace with the specified parameters. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId, data__keyName" /> | Regenerate a shared access key for a partner namespace. |

## `SELECT` examples

List all the partner namespaces under an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_namespaces', value: 'view', },
        { label: 'partner_namespaces', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
disable_local_auth,
endpoint,
inbound_ip_rules,
location,
minimum_tls_version_allowed,
partnerNamespaceName,
partner_registration_fully_qualified_id,
partner_topic_routing_mode,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
subscriptionId,
system_data,
tags
FROM azure.event_grid.vw_partner_namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.event_grid.partner_namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_namespaces</code> resource.

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
INSERT INTO azure.event_grid.partner_namespaces (
partnerNamespaceName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ partnerNamespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: privateEndpointConnections
          value:
            - - name: id
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
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string
        - name: provisioningState
          value: string
        - name: partnerRegistrationFullyQualifiedId
          value: string
        - name: minimumTlsVersionAllowed
          value: string
        - name: endpoint
          value: string
        - name: publicNetworkAccess
          value: string
        - name: inboundIpRules
          value:
            - - name: ipMask
                value: string
              - name: action
                value: string
        - name: disableLocalAuth
          value: boolean
        - name: partnerTopicRoutingMode
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>partner_namespaces</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.partner_namespaces
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
partnerNamespaceName = '{{ partnerNamespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>partner_namespaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.partner_namespaces
WHERE partnerNamespaceName = '{{ partnerNamespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
