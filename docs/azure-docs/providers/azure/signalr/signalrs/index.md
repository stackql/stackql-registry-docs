---
title: signalrs
hide_title: false
hide_table_of_contents: false
keywords:
  - signalrs
  - signalr
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

Creates, updates, deletes, gets or lists a <code>signalrs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>signalrs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.signalrs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_signalrs', value: 'view', },
        { label: 'signalrs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_firewall" /> | `text` | field from the `properties` object |
| <CopyableCode code="cors" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_aad_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_local_auth" /> | `text` | field from the `properties` object |
| <CopyableCode code="external_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_name_prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | A class represent managed identities used for request and response |
| <CopyableCode code="kind" /> | `text` | The kind of the service |
| <CopyableCode code="live_trace_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_ac_ls" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_endpoint_connections" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_network_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="region_endpoint_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_log_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_stopped" /> | `text` | field from the `properties` object |
| <CopyableCode code="server_port" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverless" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_private_link_resources" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The billing information of the resource. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tls" /> | `text` | field from the `properties` object |
| <CopyableCode code="upstream" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | A class represent managed identities used for request and response |
| <CopyableCode code="kind" /> | `string` | The kind of the service |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of the resource |
| <CopyableCode code="sku" /> | `object` | The billing information of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get the resource and its properties. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create or update a resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Operation to delete a resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Operation to update an exiting resource. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks that the resource name is valid and is not already in use. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Operation to restart a resource. |

## `SELECT` examples

Handles requests to list all resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_signalrs', value: 'view', },
        { label: 'signalrs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_firewall,
cors,
disable_aad_auth,
disable_local_auth,
external_ip,
features,
host_name,
host_name_prefix,
identity,
kind,
live_trace_configuration,
location,
network_ac_ls,
private_endpoint_connections,
provisioning_state,
public_network_access,
public_port,
region_endpoint_enabled,
resourceGroupName,
resourceName,
resource_log_configuration,
resource_stopped,
server_port,
serverless,
shared_private_link_resources,
sku,
subscriptionId,
tags,
tls,
upstream,
version
FROM azure.signalr.vw_signalrs
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
sku,
tags
FROM azure.signalr.signalrs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>signalrs</code> resource.

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
INSERT INTO azure.signalr.signalrs (
resourceGroupName,
resourceName,
subscriptionId,
tags,
location,
sku,
properties,
kind,
identity
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ sku }}',
'{{ properties }}',
'{{ kind }}',
'{{ identity }}'
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
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: externalIP
          value: string
        - name: hostName
          value: string
        - name: publicPort
          value: integer
        - name: serverPort
          value: integer
        - name: version
          value: string
        - name: privateEndpointConnections
          value:
            - - name: properties
                value:
                  - name: groupIds
                    value:
                      - string
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
        - name: sharedPrivateLinkResources
          value:
            - - name: properties
                value:
                  - name: groupId
                    value: string
                  - name: privateLinkResourceId
                    value: string
                  - name: requestMessage
                    value: string
                  - name: fqdns
                    value:
                      - string
                  - name: status
                    value: []
        - name: tls
          value:
            - name: clientCertEnabled
              value: boolean
        - name: hostNamePrefix
          value: string
        - name: features
          value:
            - - name: flag
                value: []
              - name: value
                value: string
              - name: properties
                value: object
        - name: liveTraceConfiguration
          value:
            - name: enabled
              value: string
            - name: categories
              value:
                - - name: name
                    value: string
                  - name: enabled
                    value: string
        - name: resourceLogConfiguration
          value:
            - name: categories
              value:
                - - name: name
                    value: string
                  - name: enabled
                    value: string
        - name: cors
          value:
            - name: allowedOrigins
              value:
                - string
        - name: serverless
          value:
            - name: connectionTimeoutInSeconds
              value: integer
        - name: upstream
          value:
            - name: templates
              value:
                - - name: hubPattern
                    value: string
                  - name: eventPattern
                    value: string
                  - name: categoryPattern
                    value: string
                  - name: urlTemplate
                    value: string
                  - name: auth
                    value:
                      - name: type
                        value: []
                      - name: managedIdentity
                        value:
                          - name: resource
                            value: string
        - name: networkACLs
          value:
            - name: defaultAction
              value: []
            - name: publicNetwork
              value:
                - name: allow
                  value:
                    - []
                - name: deny
                  value:
                    - []
            - name: privateEndpoints
              value:
                - - name: allow
                    value:
                      - []
                  - name: deny
                    value:
                      - []
                  - name: name
                    value: string
            - name: ipRules
              value:
                - - name: value
                    value: string
        - name: applicationFirewall
          value:
            - name: clientConnectionCountRules
              value:
                - - name: type
                    value: string
        - name: publicNetworkAccess
          value: string
        - name: disableLocalAuth
          value: boolean
        - name: disableAadAuth
          value: boolean
        - name: regionEndpointEnabled
          value: string
        - name: resourceStopped
          value: string
    - name: kind
      value: []
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: object
        - name: principalId
          value: string
        - name: tenantId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>signalrs</code> resource.

```sql
/*+ update */
UPDATE azure.signalr.signalrs
SET 
tags = '{{ tags }}',
location = '{{ location }}',
sku = '{{ sku }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
identity = '{{ identity }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>signalrs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.signalr.signalrs
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
