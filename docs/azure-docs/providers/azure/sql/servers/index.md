---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - sql
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.servers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="administrator_login" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrator_login_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="administrators" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_governance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="federated_client_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fully_qualified_domain_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="is_ipv6_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="key_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Kind of sql server. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="minimal_tls_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_user_assigned_identity_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="restrict_outbound_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_feature" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Azure Active Directory identity configuration for a resource. |
| <CopyableCode code="kind" /> | `string` | Kind of sql server. This is metadata used for the Azure portal experience. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of a server. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of all servers in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of servers in a resource groups. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__location" /> | Creates or updates a server. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes a server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates a server. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Determines whether a resource can be created with the specified name. |
| <CopyableCode code="import_database" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, data__administratorLogin, data__administratorLoginPassword, data__storageKey, data__storageKeyType, data__storageUri" /> | Imports a bacpac into a new database. |
| <CopyableCode code="refresh_status" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Refresh external governance enablement status. |

## `SELECT` examples

Gets a list of all servers in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_servers', value: 'view', },
        { label: 'servers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
administrator_login,
administrator_login_password,
administrators,
external_governance_status,
federated_client_id,
fully_qualified_domain_name,
identity,
is_ipv6_enabled,
key_id,
kind,
location,
minimal_tls_version,
primary_user_assigned_identity_id,
private_endpoint_connections,
public_network_access,
resourceGroupName,
restrict_outbound_network_access,
serverName,
state,
subscriptionId,
tags,
version,
workspace_feature
FROM azure.sql.vw_servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
kind,
location,
properties,
tags
FROM azure.sql.servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>servers</code> resource.

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
INSERT INTO azure.sql.servers (
resourceGroupName,
serverName,
subscriptionId,
data__location,
location,
tags,
identity,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: location
      value: string
    - name: tags
      value: object
    - name: identity
      value:
        - name: principalId
          value: string
        - name: type
          value: string
        - name: tenantId
          value: string
    - name: kind
      value: string
    - name: properties
      value:
        - name: administratorLogin
          value: string
        - name: administratorLoginPassword
          value: string
        - name: version
          value: string
        - name: state
          value: string
        - name: fullyQualifiedDomainName
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
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
        - name: minimalTlsVersion
          value: string
        - name: publicNetworkAccess
          value: string
        - name: workspaceFeature
          value: string
        - name: primaryUserAssignedIdentityId
          value: string
        - name: federatedClientId
          value: string
        - name: keyId
          value: string
        - name: administrators
          value:
            - name: administratorType
              value: string
            - name: principalType
              value: string
            - name: login
              value: string
            - name: sid
              value: string
            - name: tenantId
              value: string
            - name: azureADOnlyAuthentication
              value: boolean
        - name: restrictOutboundNetworkAccess
          value: string
        - name: isIPv6Enabled
          value: string
        - name: externalGovernanceStatus
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>servers</code> resource.

```sql
/*+ update */
UPDATE azure.sql.servers
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
