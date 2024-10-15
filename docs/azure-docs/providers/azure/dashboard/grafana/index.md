---
title: grafana
hide_title: false
hide_table_of_contents: false
keywords:
  - grafana
  - dashboard
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

Creates, updates, deletes, gets or lists a <code>grafana</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grafana</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dashboard.grafana" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_grafana', value: 'view', },
        { label: 'grafana', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ARM id of the grafana resource |
| <CopyableCode code="name" /> | `text` | Name of the grafana resource. |
| <CopyableCode code="api_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_generated_domain_name_label_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="deterministic_outbound_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="enterprise_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="grafana_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="grafana_integrations" /> | `text` | field from the `properties` object |
| <CopyableCode code="grafana_major_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="grafana_plugins" /> | `text` | field from the `properties` object |
| <CopyableCode code="grafana_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `text` | The geo-location where the grafana resource lives |
| <CopyableCode code="outbound_ips" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags for grafana resource. |
| <CopyableCode code="type" /> | `text` | The type of the grafana resource. |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="zone_redundancy" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the grafana resource |
| <CopyableCode code="name" /> | `string` | Name of the grafana resource. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the grafana resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the grafana resource. |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags for grafana resource. |
| <CopyableCode code="type" /> | `string` | The type of the grafana resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="check_enterprise_details" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="fetch_available_plugins" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_grafana', value: 'view', },
        { label: 'grafana', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
api_key,
auto_generated_domain_name_label_scope,
deterministic_outbound_ip,
endpoint,
enterprise_configurations,
grafana_configurations,
grafana_integrations,
grafana_major_version,
grafana_plugins,
grafana_version,
identity,
location,
outbound_ips,
private_endpoint_connections,
provisioning_state,
public_network_access,
resourceGroupName,
sku,
subscriptionId,
system_data,
tags,
type,
workspaceName,
zone_redundancy
FROM azure.dashboard.vw_grafana
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
sku,
systemData,
tags,
type
FROM azure.dashboard.grafana
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>grafana</code> resource.

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
INSERT INTO azure.dashboard.grafana (
resourceGroupName,
subscriptionId,
workspaceName,
sku,
properties,
identity,
systemData,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
'{{ sku }}',
'{{ properties }}',
'{{ identity }}',
'{{ systemData }}',
'{{ tags }}',
'{{ location }}'
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
    - name: sku
      value:
        - name: name
          value: string
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: grafanaVersion
          value: string
        - name: endpoint
          value: string
        - name: publicNetworkAccess
          value: []
        - name: zoneRedundancy
          value: []
        - name: apiKey
          value: []
        - name: deterministicOutboundIP
          value: []
        - name: outboundIPs
          value:
            - string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: []
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: groupIds
                    value:
                      - string
                  - name: provisioningState
                    value: []
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
        - name: autoGeneratedDomainNameLabelScope
          value: []
        - name: grafanaIntegrations
          value:
            - name: azureMonitorWorkspaceIntegrations
              value:
                - - name: azureMonitorWorkspaceResourceId
                    value: string
        - name: enterpriseConfigurations
          value:
            - name: marketplacePlanId
              value: string
            - name: marketplaceAutoRenew
              value: []
        - name: grafanaConfigurations
          value:
            - name: smtp
              value:
                - name: enabled
                  value: boolean
                - name: host
                  value: string
                - name: user
                  value: string
                - name: password
                  value: string
                - name: fromAddress
                  value: string
                - name: fromName
                  value: string
                - name: startTLSPolicy
                  value: []
                - name: skipVerify
                  value: boolean
        - name: grafanaPlugins
          value: object
        - name: grafanaMajorVersion
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>grafana</code> resource.

```sql
/*+ update */
UPDATE azure.dashboard.grafana
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>grafana</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dashboard.grafana
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
